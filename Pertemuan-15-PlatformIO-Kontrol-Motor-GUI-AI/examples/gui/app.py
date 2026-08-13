import sys,time
from PyQt5 import QtWidgets,QtCore
import pyqtgraph as pg
import serial,serial.tools.list_ports
import pandas as pd
from matplotlib import pyplot as plt
import sys as _sys
from pathlib import Path
_sys.path.append(str(Path(__file__).resolve().parents[3]/'shared'))
from control_metrics import step_metrics
class App(QtWidgets.QWidget):
 def __init__(self):
  super().__init__();self.resize(1500,850);self.setWindowTitle('Arduino Mega Motor PID');self.ser=None;self.rows=[]
  root=QtWidgets.QHBoxLayout(self);left=QtWidgets.QFormLayout();right=QtWidgets.QVBoxLayout();root.addLayout(left,0);root.addLayout(right,1)
  self.port=QtWidgets.QComboBox();left.addRow('Port',self.port);self.refresh();b=QtWidgets.QPushButton('Refresh');b.clicked.connect(self.refresh);left.addRow(b)
  self.con=QtWidgets.QPushButton('Connect');self.con.clicked.connect(self.connect);left.addRow(self.con);self.run=QtWidgets.QPushButton('Start');self.run.clicked.connect(self.toggle);left.addRow(self.run)
  self.mode=QtWidgets.QComboBox();self.mode.addItems(['SPEED','POSITION']);self.mode.currentTextChanged.connect(lambda x:self.send('MODE,'+x));left.addRow('Mode',self.mode)
  z=QtWidgets.QPushButton('Zero position');z.clicked.connect(lambda:self.send('ZERO'));left.addRow(z)
  self.spins={}
  for k,val,lo,hi,step in [('SP',100,-600,600,.1),('KP',.8,0,3,.01),('KI',.4,0,3,.01),('KD',.01,0,3,.01),('ALPHA',.25,0,1,.01)]:
   s=QtWidgets.QDoubleSpinBox();s.setRange(lo,hi);s.setDecimals(3);s.setSingleStep(step);s.setValue(val);s.valueChanged.connect(lambda x,kk=k:self.send(f'{kk},{x}'));self.spins[k]=s;left.addRow(k,s)
  sv=QtWidgets.QPushButton('Save CSV + JPG');sv.clicked.connect(self.save);left.addRow(sv);cl=QtWidgets.QPushButton('Clear');cl.clicked.connect(lambda:self.rows.clear());left.addRow(cl)
  self.g1=pg.PlotWidget(title='SP / speed / position');self.g2=pg.PlotWidget(title='P I D PID');self.g1.addLegend();self.g2.addLegend();right.addWidget(self.g1);right.addWidget(self.g2);self.tm=QtCore.QTimer();self.tm.timeout.connect(self.poll);self.tm.start(50)
 def refresh(self):self.port.clear();self.port.addItems([p.device for p in serial.tools.list_ports.comports()])
 def connect(self):
  if self.ser:self.ser.close();self.ser=None;self.con.setText('Connect');return
  try:self.ser=serial.Serial(self.port.currentText(),115200,timeout=0);time.sleep(1.5);self.con.setText('Disconnect')
  except Exception as e:QtWidgets.QMessageBox.critical(self,'Serial',str(e))
 def send(self,s):
  if self.ser:self.ser.write((s+'\n').encode())
 def toggle(self):
  on=self.run.text()=='Start';self.send('RUN,1' if on else 'RUN,0');self.run.setText('Stop' if on else 'Start')
 def poll(self):
  if not self.ser:return
  for _ in range(30):
   if not self.ser.in_waiting:break
   q=self.ser.readline().decode(errors='ignore').strip().split(',')
   if len(q)!=13 or not q[0].isdigit():continue
   try:self.rows.append([float(q[0]),q[1]]+[float(x) for x in q[2:]])
   except:pass
  self.rows=self.rows[-8000:]
  if not self.rows:return
  a=self.rows[-1200:];t0=self.rows[0][0];t=[(r[0]-t0)/1000 for r in a];self.g1.clear();self.g1.plot(t,[r[2] for r in a],pen='c',name='SP');self.g1.plot(t,[r[7] for r in a],pen='y',name='RPM LPF');self.g1.plot(t,[r[4] for r in a],pen='g',name='Position');self.g2.clear();
  for idx,pen,name in [(9,'r','P'),(10,'g','I'),(11,'b','D'),(12,'w','PID')]:self.g2.plot(t,[r[idx] for r in a],pen=pen,name=name)
 def save(self):
  if not self.rows:return
  cols=['ms','mode','sp','count','pos_deg','rpm_raw','rpm_ma','rpm_lpf','error','P','I','D','pid'];df=pd.DataFrame(self.rows,columns=cols);stamp=time.strftime('%Y%m%d_%H%M%S');csvf=f'motor_{stamp}.csv';jpg=f'motor_{stamp}.jpg';df.to_csv(csvf,index=False);t=(df.ms-df.ms.iloc[0])/1000;plt.figure(figsize=(10,5));plt.plot(t,df.sp,label='SP');plt.plot(t,df.rpm_lpf,label='RPM LPF');plt.plot(t,df.pos_deg,label='Position');plt.grid();plt.legend();plt.xlabel('Time (s)');plt.tight_layout();plt.savefig(jpg,dpi=150);plt.close();latest=df.mode.iloc[-1];mask=df.mode==latest;d=df[mask];tt=(d.ms-d.ms.iloc[0])/1000;feedback=d.rpm_lpf if latest=='SPEED' else d.pos_deg;m=step_metrics(tt,feedback,d.sp);msg='\n'.join(f'{k}: {v:.3f}' for k,v in m.items());QtWidgets.QMessageBox.information(self,'Saved + response metrics',f'CSV: {csvf}\nJPG: {jpg}\nMode: {latest}\n\n{msg}')
app=QtWidgets.QApplication(sys.argv);w=App();w.show();sys.exit(app.exec_())
