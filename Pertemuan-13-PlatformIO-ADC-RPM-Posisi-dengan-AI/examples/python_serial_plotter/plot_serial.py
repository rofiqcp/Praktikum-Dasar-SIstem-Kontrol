import sys,time,csv
import serial
import matplotlib.pyplot as plt
port=sys.argv[1] if len(sys.argv)>1 else 'COM5'
s=serial.Serial(port,115200,timeout=1); time.sleep(2)
t=[];rpm=[];pos=[]
plt.ion(); fig,ax=plt.subplots()
while plt.fignum_exists(fig.number):
 line=s.readline().decode(errors='ignore').strip().split(',')
 if len(line)!=6 or not line[0].isdigit(): continue
 t.append(float(line[0])/1000); pos.append(float(line[4])); rpm.append(float(line[5]));
 t=t[-500:];pos=pos[-500:];rpm=rpm[-500:]
 ax.clear();ax.plot(t,rpm,label='rpm');ax.plot(t,pos,label='deg');ax.grid();ax.legend();plt.pause(.01)
