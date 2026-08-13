import argparse,sys,time
from pathlib import Path
from collections import deque
import numpy as np
import pandas as pd
from PyQt5 import QtCore,QtWidgets
import pyqtgraph as pg
import serial,serial.tools.list_ports
from matplotlib import pyplot as plt
from response_metrics import step_metrics

COLS=['ms','mode','sp','position_deg','rpm_raw','rpm_ma','rpm_lpf','error','P','I','D','pid_pwm','pwm_cw','pwm_ccw','fault']

class SerialDevice:
    def __init__(self,port): self.ser=serial.Serial(port,115200,timeout=0);time.sleep(1.3)
    def send(self,s): self.ser.write((s+'\n').encode())
    def lines(self):
        out=[]
        for _ in range(50):
            if not self.ser.in_waiting: break
            out.append(self.ser.readline().decode(errors='ignore').strip())
        return out
    def close(self):
        try:self.send('RUN,0')
        except Exception:pass
        self.ser.close()

class DemoDevice:
    def __init__(self):
        self.t0=time.monotonic();self.last=self.t0;self.mode=1;self.sp=0;self.pos=0;self.rpm=0;self.ma=0;self.lpf=0
        self.kp=.45;self.ki=.08;self.kd=.002;self.integ=0;self.last_y=0;self.run=False;self.fault=0;self.maxpwm=180;self.alpha=.25
    def send(self,s):
        k,v=s.split(',',1);f=float(v) if v.replace('.','',1).replace('-','',1).isdigit() else 0
        if k=='RUN':self.run=int(f)!=0
        elif k=='MODE':self.run=False;self.mode=2 if int(f)==2 else 1;self.sp=0;self.integ=0
        elif k=='ZERO':self.pos=0;self.sp=0;self.run=False
        elif k=='SP':self.sp=f
        elif k=='KP':self.kp=f;self.integ=0
        elif k=='KI':self.ki=f;self.integ=0
        elif k=='KD':self.kd=f;self.integ=0
        elif k=='ALPHA':self.alpha=f
        elif k=='MAXPWM':self.maxpwm=int(f)
        elif k=='CLEAR':self.fault=0
    def lines(self):
        now=time.monotonic();dt=max(.001,now-self.last);self.last=now
        y=self.lpf if self.mode==1 else self.pos;e=self.sp-y
        if self.run:
            p=self.kp*e;self.integ+=self.ki*e*dt;d=-self.kd*(y-self.last_y)/dt;u=np.clip(p+self.integ+d,-self.maxpwm,self.maxpwm)
        else:p=self.integ=d=u=0
        self.last_y=y
        # pedagogic first-order motor demo, not a physical identification model
        target_rpm=float(u)*2.2;self.rpm+=(target_rpm-self.rpm)*min(1,dt*5);self.pos+=self.rpm*6*dt
        self.ma=.7*self.ma+.3*self.rpm;self.lpf=self.alpha*self.ma+(1-self.alpha)*self.lpf
        cw=max(0,int(u));ccw=max(0,int(-u));ms=int((now-self.t0)*1000)
        fb=self.lpf if self.mode==1 else self.pos;e=self.sp-fb
        return [f'{ms},{self.mode},{self.sp:.3f},{self.pos:.3f},{self.rpm:.3f},{self.ma:.3f},{self.lpf:.3f},{e:.3f},{p:.3f},{self.integ:.3f},{d:.3f},{u:.3f},{cw},{ccw},{self.fault}']
    def close(self):self.run=False

class App(QtWidgets.QWidget):
    def __init__(self,demo=False):
        super().__init__();self.setWindowTitle('P15 PID Motor DC — Arduino Mega');self.resize(1900,960)
        self.demo=demo;self.dev=DemoDevice() if demo else None;self.rows=[];self.last_ping=0
        root=QtWidgets.QHBoxLayout(self);left=QtWidgets.QWidget();left.setFixedWidth(690);form=QtWidgets.QFormLayout(left);right=QtWidgets.QVBoxLayout();root.addWidget(left);root.addLayout(right,1)
        self.port=QtWidgets.QComboBox();self.refresh();form.addRow('Port',self.port)
        row=QtWidgets.QHBoxLayout();self.refreshBtn=QtWidgets.QPushButton('Refresh');self.conn=QtWidgets.QPushButton('Connect' if not demo else 'Demo Connected');row.addWidget(self.refreshBtn);row.addWidget(self.conn);form.addRow(row);self.refreshBtn.clicked.connect(self.refresh);self.conn.clicked.connect(self.connect)
        self.mode=QtWidgets.QComboBox();self.mode.addItems(['SPEED','POSITION']);self.mode.currentIndexChanged.connect(self.change_mode);form.addRow('Mode',self.mode)
        self.run=QtWidgets.QPushButton('Start');self.run.clicked.connect(self.toggle);form.addRow(self.run)
        self.controls={}
        specs=[('SP',0,-600,600,.1,3),('KP',.45,0,3,.01,3),('KI',.08,0,3,.01,3),('KD',.002,0,3,.01,4),('ALPHA',.25,0,1,.01,2),('MA',8,1,16,1,0),('TS',20,10,300,10,0),('CPR',600,1,100000,1,1),('MAXPWM',180,20,255,5,0)]
        for k,val,lo,hi,step,dec in specs:
            s=QtWidgets.QDoubleSpinBox();s.setRange(lo,hi);s.setDecimals(dec);s.setSingleStep(step);s.setValue(val);s.valueChanged.connect(lambda x,kk=k:self.send(f'{kk},{x}'));self.controls[k]=s;form.addRow(k,s)
        btnrow=QtWidgets.QHBoxLayout();self.zero=QtWidgets.QPushButton('Zero encoder');self.clearFault=QtWidgets.QPushButton('Clear fault');btnrow.addWidget(self.zero);btnrow.addWidget(self.clearFault);form.addRow(btnrow);self.zero.clicked.connect(lambda:self.send('ZERO,1'));self.clearFault.clicked.connect(lambda:self.send('CLEAR,1'))
        self.status=QtWidgets.QLabel('DEMO' if demo else 'DISCONNECTED');form.addRow('Status',self.status)
        self.metrics=QtWidgets.QPlainTextEdit();self.metrics.setReadOnly(True);self.metrics.setMaximumHeight(160);form.addRow('Response',self.metrics)
        self.checks={};grid=QtWidgets.QGridLayout();names=['SP','Position','RPM raw','RPM MA','RPM LPF','Error','P','I','D','PID','PWM CW','PWM CCW']
        defaults={'SP','Position','RPM LPF','Error','PID'}
        for i,n in enumerate(names):
            c=QtWidgets.QCheckBox(n);c.setChecked(n in defaults);self.checks[n]=c;grid.addWidget(c,i//3,i%3)
        form.addRow('Curves',grid)
        actions=QtWidgets.QHBoxLayout();save=QtWidgets.QPushButton('Save CSV + XLSX + JPG');clear=QtWidgets.QPushButton('Clear data');actions.addWidget(save);actions.addWidget(clear);form.addRow(actions);save.clicked.connect(self.save);clear.clicked.connect(self.clear_data)
        self.g1=pg.PlotWidget(title='Feedback: setpoint / position / speed');self.g2=pg.PlotWidget(title='Controller: error / P / I / D / PID / PWM');self.g1.addLegend();self.g2.addLegend();right.addWidget(self.g1);right.addWidget(self.g2)
        self.timer=QtCore.QTimer();self.timer.timeout.connect(self.poll);self.timer.start(40)
    def refresh(self):
        if not hasattr(self,'port'):return
        self.port.clear();self.port.addItems([p.device for p in serial.tools.list_ports.comports()])
    def connect(self):
        if self.demo:return
        if self.dev:
            self.dev.close();self.dev=None;self.conn.setText('Connect');self.status.setText('DISCONNECTED');return
        try:
            self.dev=SerialDevice(self.port.currentText());self.conn.setText('Disconnect');self.status.setText('CONNECTED')
            self.send(f'MODE,{2 if self.mode.currentIndex() else 1}')
            for k,w in self.controls.items(): self.send(f'{k},{w.value()}')
            self.send('HOST,1');self.send('PING,1');self.send('STATUS,1')
        except Exception as e:QtWidgets.QMessageBox.critical(self,'Serial',str(e));self.dev=None
    def send(self,s):
        if self.dev:
            try:self.dev.send(s)
            except Exception as e:self.status.setText('SERIAL ERROR: '+str(e))
    def toggle(self):
        on=self.run.text()=='Start';self.send('RUN,1' if on else 'RUN,0');self.run.setText('Stop' if on else 'Start')
    def change_mode(self,idx):
        self.send('RUN,0');self.run.setText('Start');self.send(f'MODE,{2 if idx else 1}')
        self.controls['SP'].blockSignals(True);self.controls['SP'].setValue(0);self.controls['SP'].blockSignals(False)
        if idx:self.send('ZERO,1')
        self.clear_data()
    def clear_data(self):self.rows.clear();self.g1.clear();self.g2.clear();self.metrics.clear()
    def poll(self):
        if not self.dev:return
        now=time.monotonic()
        if now-self.last_ping>.8:self.send('PING,1');self.last_ping=now
        try:lines=self.dev.lines()
        except Exception as e:self.status.setText('SERIAL LOST: '+str(e));self.run.setText('Start');return
        for line in lines:
            if not line or line.startswith('#'):continue
            q=line.split(',')
            if len(q)!=15:continue
            try:r=[float(x) for x in q]
            except ValueError:continue
            self.rows.append(r)
        self.rows=self.rows[-20000:]
        if not self.rows:return
        r=self.rows[-1];fault=int(r[14]);self.status.setText(('DEMO ' if self.demo else 'CONNECTED ')+f'| mode={int(r[1])} fault={fault} pwm={r[11]:.1f}')
        a=self.rows[-2500:];t0=a[0][0];t=[(x[0]-t0)/1000 for x in a]
        self.g1.clear();self.g2.clear();
        curve1=[('SP',2),('Position',3),('RPM raw',4),('RPM MA',5),('RPM LPF',6)]
        curve2=[('Error',7),('P',8),('I',9),('D',10),('PID',11),('PWM CW',12),('PWM CCW',13)]
        for name,idx in curve1:
            if self.checks[name].isChecked():self.g1.plot(t,[x[idx] for x in a],name=name)
        for name,idx in curve2:
            if self.checks[name].isChecked():self.g2.plot(t,[x[idx] for x in a],name=name)
    def save(self):
        if len(self.rows)<5:return
        df=pd.DataFrame(self.rows,columns=COLS);stamp=time.strftime('%Y%m%d_%H%M%S');out=Path.cwd()/f'motor_{stamp}'
        csvp=out.with_suffix('.csv');xlsx=out.with_suffix('.xlsx');jpg=out.with_suffix('.jpg');df.to_csv(csvp,index=False);df.to_excel(xlsx,index=False)
        t=(df.ms-df.ms.iloc[0])/1000;mode=int(round(df['mode'].iloc[-1]));y=df.rpm_lpf if mode==1 else df.position_deg;label='RPM LPF' if mode==1 else 'Position (deg)'
        plt.figure(figsize=(11,6));plt.plot(t,df.sp,label='SP');plt.plot(t,y,label=label);plt.xlabel('Time (s)');plt.ylabel(label);plt.grid(True);plt.legend();plt.tight_layout();plt.savefig(jpg,dpi=160);plt.close()
        m=step_metrics(t.to_numpy(),y.to_numpy(),df.sp.to_numpy());txt='\n'.join(f'{k}: {v:.4g}' for k,v in m.items());self.metrics.setPlainText(txt);QtWidgets.QMessageBox.information(self,'Saved',f'{csvp.name}\n{xlsx.name}\n{jpg.name}\n\n{txt}')
    def closeEvent(self,event):
        if self.dev:
            try:self.dev.send('RUN,0');self.dev.close()
            except Exception:pass
        event.accept()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demo',action='store_true');args=ap.parse_args();app=QtWidgets.QApplication(sys.argv);w=App(args.demo);w.show();sys.exit(app.exec_())
if __name__=='__main__':main()
