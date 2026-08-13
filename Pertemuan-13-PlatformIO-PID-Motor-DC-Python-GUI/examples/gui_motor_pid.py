import sys,csv,time
from PyQt5 import QtWidgets,QtCore
import pyqtgraph as pg
import serial,serial.tools.list_ports
class App(QtWidgets.QWidget):
 def __init__(self):
  super().__init__();self.ser=None;self.t=[];self.y=[];self.setWindowTitle('PID Motor DC - Arduino Mega');self.resize(1200,700)
  lay=QtWidgets.QGridLayout(self);self.port=QtWidgets.QComboBox();self.refresh();self.btn=QtWidgets.QPushButton('Connect');self.btn.clicked.connect(self.conn);self.sp=QtWidgets.QDoubleSpinBox();self.sp.setRange(-600,600);self.sp.setSingleStep(.1);self.sp.valueChanged.connect(lambda v:self.send(f'SP={v}'));self.mode=QtWidgets.QComboBox();self.mode.addItems(['Speed','Position']);self.mode.currentIndexChanged.connect(lambda i:self.send(f'MODE={i}'));self.start=QtWidgets.QPushButton('START');self.start.clicked.connect(lambda:self.send('START'));self.stop=QtWidgets.QPushButton('STOP');self.stop.clicked.connect(lambda:self.send('STOP'));self.plot=pg.PlotWidget();self.curve=self.plot.plot();
  for r,(name,w) in enumerate([('Port',self.port),('Connect',self.btn),('Setpoint',self.sp),('Mode',self.mode),('Start',self.start),('Stop',self.stop)]):lay.addWidget(QtWidgets.QLabel(name),r,0);lay.addWidget(w,r,1)
  lay.addWidget(self.plot,0,2,10,1);self.timer=QtCore.QTimer();self.timer.timeout.connect(self.poll);self.timer.start(20)
 def refresh(self):self.port.clear();self.port.addItems([p.device for p in serial.tools.list_ports.comports()])
 def conn(self):
  if self.ser:self.ser.close();self.ser=None;self.btn.setText('Connect');return
  self.ser=serial.Serial(self.port.currentText(),115200,timeout=0);self.btn.setText('Disconnect')
 def send(self,s):
  if self.ser:self.ser.write((s+'\n').encode())
 def poll(self):
  if not self.ser:return
  try:
   while self.ser.in_waiting:
    v=self.ser.readline().decode(errors='ignore').strip().split(',')
    if len(v)==10:self.t.append(float(v[0])/1000);self.y.append(float(v[4]));self.curve.setData(self.t[-1000:],self.y[-1000:])
  except Exception as e:print(e)
app=QtWidgets.QApplication(sys.argv);w=App();w.show();sys.exit(app.exec_())
