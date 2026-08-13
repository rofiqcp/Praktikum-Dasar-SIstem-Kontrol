import sys,time,csv
from pathlib import Path
from PyQt5 import QtWidgets,QtCore
import pyqtgraph as pg
import serial,serial.tools.list_ports
import pandas as pd
from matplotlib import pyplot as plt
from response_metrics import step_metrics

class App(QtWidgets.QWidget):
 def __init__(self):
  super().__init__(); self.setWindowTitle('PID Temperature - Arduino Mega'); self.resize(1400,800); self.ser=None; self.rows=[]
  root=QtWidgets.QHBoxLayout(self); panel=QtWidgets.QFormLayout(); right=QtWidgets.QVBoxLayout(); root.addLayout(panel,0);root.addLayout(right,1)
  self.port=QtWidgets.QComboBox();self.refresh(); panel.addRow('Port',self.port)
  br=QtWidgets.QPushButton('Refresh');br.clicked.connect(self.refresh);panel.addRow(br)
  self.btn=QtWidgets.QPushButton('Connect');self.btn.clicked.connect(self.connect);panel.addRow(self.btn)
  self.run=QtWidgets.QPushButton('Start');self.run.clicked.connect(self.toggle);panel.addRow(self.run)
  self.spin={}
  for k,v,lo,hi,step in [('SP',50,20,65,.1),('KP',6,0,100,.01),('KI',.08,0,10,.01),('KD',8,0,100,.01)]:
   s=QtWidgets.QDoubleSpinBox();s.setRange(lo,hi);s.setDecimals(3);s.setSingleStep(step);s.setValue(v);s.valueChanged.connect(lambda x,kk=k:self.send(f'{kk},{x}'));self.spin[k]=s;panel.addRow(k,s)
  save=QtWidgets.QPushButton('Save CSV + JPG');save.clicked.connect(self.save);panel.addRow(save)
  clear=QtWidgets.QPushButton('Clear');clear.clicked.connect(lambda:self.rows.clear());panel.addRow(clear)
  self.g1=pg.PlotWidget(title='Temperature');self.g2=pg.PlotWidget(title='PID');self.g1.addLegend();self.g2.addLegend();right.addWidget(self.g1);right.addWidget(self.g2)
  self.timer=QtCore.QTimer();self.timer.timeout.connect(self.poll);self.timer.start(50)
 def refresh(self):
  if hasattr(self,'port'): self.port.clear(); self.port.addItems([p.device for p in serial.tools.list_ports.comports()])
 def connect(self):
  if self.ser: self.ser.close();self.ser=None;self.btn.setText('Connect');return
  try:self.ser=serial.Serial(self.port.currentText(),115200,timeout=0);time.sleep(1.5);self.btn.setText('Disconnect')
  except Exception as e:QtWidgets.QMessageBox.critical(self,'Serial',str(e))
 def send(self,s):
  if self.ser:self.ser.write((s+'\n').encode())
 def toggle(self):
  on=self.run.text()=='Start';self.send('RUN,1' if on else 'RUN,0');self.run.setText('Stop' if on else 'Start')
 def poll(self):
  if not self.ser:return
  for _ in range(20):
   if not self.ser.in_waiting:break
   try:
    q=self.ser.readline().decode(errors='ignore').strip().split(',')
    if len(q)!=9 or not q[0].isdigit():continue
    r=list(map(float,q));self.rows.append(r);self.rows=self.rows[-5000:]
   except:pass
  if not self.rows:return
  a=self.rows[-1000:];t0=self.rows[0][0];t=[(r[0]-t0)/1000 for r in a]
  self.g1.clear();self.g1.plot(t,[r[1] for r in a],pen='y',name='PV');self.g1.plot(t,[r[2] for r in a],pen='c',name='SP')
  self.g2.clear();
  for idx,pen,name in [(4,'r','P'),(5,'g','I'),(6,'b','D'),(7,'w','PID')]:self.g2.plot(t,[r[idx] for r in a],pen=pen,name=name)
 def save(self):
  if not self.rows:return
  cols=['ms','temp_C','sp_C','error','P','I','D','pid_pct','ssr'];df=pd.DataFrame(self.rows,columns=cols);stamp=time.strftime('%Y%m%d_%H%M%S');df.to_csv(f'temp_{stamp}.csv',index=False)
  t=(df.ms-df.ms.iloc[0])/1000;plt.figure(figsize=(10,5));plt.plot(t,df.temp_C,label='PV');plt.plot(t,df.sp_C,'--',label='SP');plt.grid();plt.legend();plt.xlabel('Time (s)');plt.ylabel('Temperature (C)');plt.tight_layout();jpg=f'temp_{stamp}.jpg';plt.savefig(jpg,dpi=150);plt.close();m=step_metrics(t,df.temp_C,df.sp_C);msg='\n'.join(f'{k}: {v:.3f}' for k,v in m.items());QtWidgets.QMessageBox.information(self,'Saved + response metrics',f'CSV: temp_{stamp}.csv\nJPG: {jpg}\n\n{msg}')

app=QtWidgets.QApplication(sys.argv);w=App();w.show();sys.exit(app.exec_())
