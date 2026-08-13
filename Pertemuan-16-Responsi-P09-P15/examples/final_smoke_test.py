import argparse,json,time
from pathlib import Path
import serial

ap=argparse.ArgumentParser(description='Passive P16 serial acceptance test')
ap.add_argument('--port',required=True);ap.add_argument('--seconds',type=float,default=8);ap.add_argument('--baud',type=int,default=115200);args=ap.parse_args()
ser=serial.Serial(args.port,args.baud,timeout=.2);time.sleep(1.5)
# Safety first: never command heat/motion in smoke test.
for cmd in ('RUN,0','PING,1','STATUS,1'):
    ser.write((cmd+'\n').encode());time.sleep(.05)
start=time.monotonic();proto=[];telemetry=0;field_counts={};sample=[]
while time.monotonic()-start<args.seconds:
    ser.write(b'PING,1\n')
    until=time.monotonic()+.25
    while time.monotonic()<until:
        line=ser.readline().decode(errors='ignore').strip()
        if not line:continue
        if line.startswith('#'):
            if line.startswith('#PROTO'):proto.append(line)
            continue
        n=len(line.split(','));field_counts[n]=field_counts.get(n,0)+1;telemetry+=1
        if len(sample)<5:sample.append(line)
ser.write(b'RUN,0\n');ser.close()
result={'port':args.port,'proto':sorted(set(proto)),'telemetry_lines':telemetry,'field_counts':field_counts,'sample':sample,'safe_command':'RUN,0'}
result['pass']=telemetry>=3 and any(k in field_counts for k in (10,15))
out=Path(f'smoke_test_{time.strftime("%Y%m%d_%H%M%S")}.json');out.write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));print('saved',out)
raise SystemExit(0 if result['pass'] else 2)
