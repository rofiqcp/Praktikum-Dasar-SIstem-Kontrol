from __future__ import annotations
import argparse
import math
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import serial
import serial.tools.list_ports
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
import matplotlib.pyplot as plt

from response_metrics import step_metrics

FIELDS=["ms","temp_C","sp_C","error","P","I","D","pid_pct","ssr","fault"]


class SerialDevice:
    def __init__(self, port: str, baud: int=115200):
        self.ser=serial.Serial(port,baud,timeout=0)
        time.sleep(1.3)
        self.ser.reset_input_buffer()
    def write(self,key,value):
        self.ser.write(f"{key},{value}\n".encode("ascii"))
    def lines(self):
        out=[]
        for _ in range(100):
            if not self.ser.in_waiting: break
            b=self.ser.readline()
            if b: out.append(b.decode(errors="ignore").strip())
        return out
    def close(self):
        try:self.write("RUN",0)
        except Exception:pass
        self.ser.close()


class DemoDevice:
    def __init__(self):
        self.t0=time.monotonic();self.last=self.t0;self.last_emit=self.t0
        self.temp=25.0;self.sp=45.0;self.kp=5.0;self.ki=.08;self.kd=2.0
        self.I=0.0;self.prev=self.temp;self.run=False;self.fault=0
        self.tmax=60;self.window=2000;self.u=0;self.ssr=0
    def write(self,key,value):
        key=key.upper()
        try:v=float(value)
        except Exception:v=0
        if key=="RUN": self.run=bool(int(v)); self.I=0
        elif key=="SP":self.sp=v
        elif key=="KP":self.kp=max(0,v)
        elif key=="KI":self.ki=max(0,v)
        elif key=="KD":self.kd=max(0,v)
        elif key=="TMAX":self.tmax=v
        elif key=="WIN":self.window=int(v)
        elif key=="CLEAR":self.fault=0
    def lines(self):
        now=time.monotonic();dt=min(.2,max(.001,now-self.last));self.last=now
        e=self.sp-self.temp
        p=self.kp*e
        d=-self.kd*(self.temp-self.prev)/dt;self.prev=self.temp
        cand=self.I+self.ki*e*dt
        if 0<=p+cand+d<=100 or (p+cand+d>100 and e<0) or (p+cand+d<0 and e>0):self.I=cand
        self.u=float(np.clip(p+self.I+d,0,100)) if self.run else 0
        # first-order thermal demo: ambient 25, 100% approaches ~75C
        target=25+0.5*self.u
        self.temp += dt*(target-self.temp)/12.0
        if self.temp>=self.tmax:self.fault=2;self.run=False;self.u=0
        self.ssr=1 if self.run and self.u>50 else 0
        if now-self.last_emit<.2:return []
        self.last_emit=now
        ms=int((now-self.t0)*1000)
        return [f"{ms},{self.temp:.3f},{self.sp:.3f},{e:.3f},{p:.3f},{self.I:.3f},{d:.3f},{self.u:.3f},{self.ssr},{self.fault}"]
    def close(self):self.run=False


class MainWindow(QtWidgets.QWidget):
    def __init__(self,demo=False):
        super().__init__()
        self.demo=demo;self.dev=None;self.rows=[];self.running=False
        self.setWindowTitle("P14 PID Temperature — Arduino Mega")
        self.resize(1500,900)

        root=QtWidgets.QHBoxLayout(self)
        left=QtWidgets.QVBoxLayout();root.addLayout(left,0)
        right=QtWidgets.QVBoxLayout();root.addLayout(right,1)

        self.port=QtWidgets.QComboBox();self.refresh_ports()
        btn_refresh=QtWidgets.QPushButton("Refresh Port");btn_refresh.clicked.connect(self.refresh_ports)
        self.btn_connect=QtWidgets.QPushButton("Demo Connect" if demo else "Connect");self.btn_connect.clicked.connect(self.connect_toggle)
        left.addWidget(QtWidgets.QLabel("Serial Port"));left.addWidget(self.port);left.addWidget(btn_refresh);left.addWidget(self.btn_connect)

        form=QtWidgets.QFormLayout();left.addLayout(form)
        self.ctrl={}
        specs={
          "SP":(45.0,20,70,.1),"KP":(5.0,0,100,.01),"KI":(.08,0,20,.01),
          "KD":(2.0,0,100,.01),"TMAX":(60.0,25,100,.5),"WIN":(2000,500,10000,100)
        }
        for key,(val,lo,hi,step) in specs.items():
            s=QtWidgets.QDoubleSpinBox();s.setRange(lo,hi);s.setValue(val);s.setSingleStep(step);s.setDecimals(3 if key!="WIN" else 0)
            s.valueChanged.connect(lambda value,k=key:self.send(k,value))
            self.ctrl[key]=s;form.addRow(key,s)

        self.btn_run=QtWidgets.QPushButton("Start");self.btn_run.clicked.connect(self.run_toggle)
        self.btn_clear_fault=QtWidgets.QPushButton("Clear Fault");self.btn_clear_fault.clicked.connect(lambda:self.send("CLEAR",1))
        self.btn_clear_data=QtWidgets.QPushButton("Clear Data");self.btn_clear_data.clicked.connect(self.clear_data)
        self.btn_save=QtWidgets.QPushButton("Save CSV + XLSX + JPG");self.btn_save.clicked.connect(self.save)
        left.addWidget(self.btn_run);left.addWidget(self.btn_clear_fault);left.addWidget(self.btn_clear_data);left.addWidget(self.btn_save)

        self.status=QtWidgets.QLabel("DISCONNECTED");self.status.setWordWrap(True);left.addWidget(self.status)

        self.g1=pg.PlotWidget(title="Temperature");self.g1.showGrid(x=True,y=True);self.g1.addLegend()
        self.g2=pg.PlotWidget(title="PID terms / Output");self.g2.showGrid(x=True,y=True);self.g2.addLegend()
        right.addWidget(self.g1);right.addWidget(self.g2)

        checkrow=QtWidgets.QHBoxLayout();right.addLayout(checkrow);self.check={}
        for name in ["PV","SP","P","I","D","PID"]:
            c=QtWidgets.QCheckBox(name);c.setChecked(True);self.check[name]=c;checkrow.addWidget(c)

        self.metrics=QtWidgets.QPlainTextEdit();self.metrics.setReadOnly(True);self.metrics.setMaximumHeight(150);right.addWidget(self.metrics)

        self.timer=QtCore.QTimer(self);self.timer.timeout.connect(self.tick);self.timer.start(50)
        self.heartbeat=QtCore.QElapsedTimer();self.heartbeat.start()

    def refresh_ports(self):
        if not hasattr(self,"port"):return
        current=self.port.currentText();self.port.clear()
        ports=[p.device for p in serial.tools.list_ports.comports()]
        self.port.addItems(ports)
        if current in ports:self.port.setCurrentText(current)

    def connect_toggle(self):
        if self.dev:
            self.disconnect();return
        try:
            self.dev=DemoDevice() if self.demo else SerialDevice(self.port.currentText())
            self.btn_connect.setText("Disconnect")
            self.status.setText("CONNECTED" + (" (DEMO)" if self.demo else ""))
            for k,w in self.ctrl.items():self.send(k,w.value())
            self.send("HOST",1);self.send("PING",1)
        except Exception as exc:
            self.dev=None;QtWidgets.QMessageBox.critical(self,"Connect",str(exc))

    def disconnect(self):
        if self.dev:
            try:self.dev.write("RUN",0)
            except Exception:pass
            self.dev.close()
        self.dev=None;self.running=False;self.btn_run.setText("Start");self.btn_connect.setText("Demo Connect" if self.demo else "Connect");self.status.setText("DISCONNECTED")

    def send(self,key,value):
        if self.dev:
            try:self.dev.write(key,value)
            except Exception as exc:self.status.setText(f"SERIAL ERROR: {exc}")

    def run_toggle(self):
        if not self.dev:
            QtWidgets.QMessageBox.warning(self,"Run","Connect first");return
        self.running=not self.running;self.send("RUN",1 if self.running else 0);self.btn_run.setText("Stop" if self.running else "Start")

    def clear_data(self):
        self.rows.clear();self.g1.clear();self.g2.clear();self.metrics.clear()

    def tick(self):
        if not self.dev:return
        if self.heartbeat.elapsed()>500:
            self.send("PING",1);self.heartbeat.restart()
        try:lines=self.dev.lines()
        except Exception as exc:self.status.setText(f"READ ERROR: {exc}");return
        for line in lines:
            if not line:continue
            if line.startswith("#"):
                if "STATUS" in line:self.status.setText(line)
                continue
            parts=line.split(",")
            if len(parts)!=len(FIELDS):continue
            try:row=[float(x) for x in parts]
            except ValueError:continue
            if not all(math.isfinite(x) for x in row):continue
            self.rows.append(row)
        if len(self.rows)>20000:self.rows=self.rows[-20000:]
        if self.rows:self.redraw()

    def redraw(self):
        a=np.asarray(self.rows[-3000:],dtype=float);t=(a[:,0]-self.rows[0][0])/1000.0
        self.g1.clear();self.g2.clear()
        if self.check["PV"].isChecked():self.g1.plot(t,a[:,1],name="PV")
        if self.check["SP"].isChecked():self.g1.plot(t,a[:,2],name="SP")
        for label,idx in [("P",4),("I",5),("D",6),("PID",7)]:
            if self.check[label].isChecked():self.g2.plot(t,a[:,idx],name=label)
        fault=int(a[-1,9]);self.status.setText(f"{'RUN' if self.running else 'STOP'} | PV={a[-1,1]:.2f} C | SP={a[-1,2]:.2f} C | OUT={a[-1,7]:.1f}% | FAULT={fault}")
        if fault:self.running=False;self.btn_run.setText("Start")

    def save(self):
        if len(self.rows)<3:return
        df=pd.DataFrame(self.rows,columns=FIELDS);df["time_s"]=(df.ms-df.ms.iloc[0])/1000
        stamp=time.strftime("%Y%m%d_%H%M%S");out=Path(__file__).resolve().parent/"output";out.mkdir(exist_ok=True)
        csv=out/f"temp_{stamp}.csv";xlsx=out/f"temp_{stamp}.xlsx";jpg=out/f"temp_{stamp}.jpg"
        df.to_csv(csv,index=False);df.to_excel(xlsx,index=False)
        m=step_metrics(df.time_s,df.temp_C,df.sp_C)
        pd.DataFrame([m]).to_csv(out/f"metrics_{stamp}.csv",index=False)
        plt.figure(figsize=(11,5));plt.plot(df.time_s,df.temp_C,label="PV");plt.plot(df.time_s,df.sp_C,"--",label="SP");plt.grid();plt.legend();plt.xlabel("Time (s)");plt.ylabel("Temperature (C)");plt.tight_layout();plt.savefig(jpg,dpi=180);plt.close()
        self.metrics.setPlainText("\n".join(f"{k}: {v}" for k,v in m.items()))
        QtWidgets.QMessageBox.information(self,"Saved",f"{csv.name}\n{xlsx.name}\n{jpg.name}")

    def closeEvent(self,event):
        self.disconnect();event.accept()


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--demo",action="store_true");args=ap.parse_args()
    q=QtWidgets.QApplication(sys.argv);w=MainWindow(demo=args.demo);w.show();sys.exit(q.exec_())

if __name__=="__main__":main()
