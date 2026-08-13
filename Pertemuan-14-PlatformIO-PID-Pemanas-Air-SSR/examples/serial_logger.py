import serial,csv,sys,time
port=sys.argv[1] if len(sys.argv)>1 else 'COM5'; ser=serial.Serial(port,115200,timeout=1)
with open('heater_log.csv','w',newline='') as f:
 w=csv.writer(f);w.writerow(['time_ms','setpoint_c','temp_c','output_percent'])
 while True:
  line=ser.readline().decode(errors='ignore').strip();
  if not line:continue
  print(line);v=line.split(',')
  if len(v)==4:w.writerow(v);f.flush()
