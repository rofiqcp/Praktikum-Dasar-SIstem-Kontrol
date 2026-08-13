// P11 Arduino Mega speed PID, supervised/logged by MATLAB.
const uint8_t PWM_CW=5, PWM_CCW=6, ENC_A=2, ENC_B=3;
const float COUNTS_PER_REV=600.0f;
const uint32_t SAMPLE_MS=50;
const uint32_t HOST_TIMEOUT_MS=2500;

volatile long enc=0;
volatile uint8_t prevState=0;
const int8_t QDEC[16]={0,-1,1,0,1,0,0,-1,-1,0,0,1,0,1,-1,0};

float sp=0,kp=.5f,ki=.2f,kd=0,maxPwm=180;
float integral=0,prevPv=0,lpf=0;
bool running=false,pidInit=false,timeoutReported=false;
uint32_t lastPing=0;

// Speed-estimator state is global so ZERO can reset it atomically and avoid
// a false RPM spike on the sample immediately after encoder zeroing.
long lastCount=0;
float rpmBuf[8]={0};
float rpmSum=0;
uint8_t rpmBufIndex=0,rpmBufCount=0;

void encISR(){
  uint8_t st=(digitalRead(ENC_A)<<1)|digitalRead(ENC_B);
  enc+=QDEC[(prevState<<2)|st];
  prevState=st;
}

void motorStop(){
  analogWrite(PWM_CW,0);
  analogWrite(PWM_CCW,0);
}

void motorWrite(float u){
  int pwm=(int)constrain(fabs(u),0,maxPwm);
  if(u>0){analogWrite(PWM_CCW,0);analogWrite(PWM_CW,pwm);}
  else if(u<0){analogWrite(PWM_CW,0);analogWrite(PWM_CCW,pwm);}
  else motorStop();
}

void resetPID(){
  integral=0;
  pidInit=false;
}

void resetSpeedEstimator(){
  noInterrupts();
  enc=0;
  lastCount=0;
  interrupts();
  for(uint8_t i=0;i<8;i++)rpmBuf[i]=0;
  rpmSum=0;
  rpmBufIndex=0;
  rpmBufCount=0;
  lpf=0;
  prevPv=0;
}

void stopControl(){
  running=false;
  motorStop();
  resetPID();
}

void command(String s){
  s.trim();
  int p=s.indexOf(',');
  if(p<0)return;
  String k=s.substring(0,p),v=s.substring(p+1);
  k.toUpperCase();

  if(k=="RUN"){
    if(v.toInt()!=0){running=true;lastPing=millis();timeoutReported=false;resetPID();}
    else stopControl();
  }
  else if(k=="PING"){lastPing=millis();timeoutReported=false;}
  else if(k=="SP")sp=constrain(v.toFloat(),-600.0f,600.0f);
  else if(k=="KP")kp=max(0.0f,v.toFloat());
  else if(k=="KI"){ki=max(0.0f,v.toFloat());if(ki==0)integral=0;}
  else if(k=="KD")kd=max(0.0f,v.toFloat());
  else if(k=="MAXPWM")maxPwm=constrain(v.toFloat(),0.0f,255.0f);
  else if(k=="ZERO" && v.toInt()!=0){
    // A reference change is performed only while stopped. Resetting the
    // estimator together with count prevents one artificial delta-count.
    stopControl();
    resetSpeedEstimator();
  }
}

void setup(){
  pinMode(PWM_CW,OUTPUT);pinMode(PWM_CCW,OUTPUT);motorStop();
  pinMode(ENC_A,INPUT_PULLUP);pinMode(ENC_B,INPUT_PULLUP);
  prevState=(digitalRead(ENC_A)<<1)|digitalRead(ENC_B);
  attachInterrupt(digitalPinToInterrupt(ENC_A),encISR,CHANGE);
  attachInterrupt(digitalPinToInterrupt(ENC_B),encISR,CHANGE);
  Serial.begin(115200);Serial.setTimeout(5);
  Serial.println("#PROTO,SPEED_PID,1");
  Serial.println("#ms,sp,rpm,error,P,I,D,pid_pwm,count");
  lastPing=millis();
}

void loop(){
  while(Serial.available())command(Serial.readStringUntil('\n'));

  if(running&&millis()-lastPing>HOST_TIMEOUT_MS){
    stopControl();
    if(!timeoutReported){Serial.println("#FAULT,HOST_TIMEOUT");timeoutReported=true;}
  }

  static uint32_t last=0;
  uint32_t now=millis();
  if(now-last<SAMPLE_MS)return;
  float dt=(now-last)/1000.0f;
  last=now;

  noInterrupts();long c=enc;interrupts();
  long dc=c-lastCount;
  lastCount=c;
  float raw=(dc/COUNTS_PER_REV)*60.0f/dt;

  float old=rpmBuf[rpmBufIndex];
  rpmBuf[rpmBufIndex]=raw;
  rpmSum+=raw-old;
  rpmBufIndex=(rpmBufIndex+1)%8;
  if(rpmBufCount<8)rpmBufCount++;
  float ma=rpmSum/(rpmBufCount?rpmBufCount:1);
  lpf=.25f*ma+.75f*lpf;

  float e=sp-lpf;
  float P=kp*e,D=0,u=0;
  if(!pidInit){prevPv=lpf;pidInit=true;}
  D=-kd*(lpf-prevPv)/dt;
  prevPv=lpf;

  float candI=integral+ki*e*dt;
  float cand=P+candI+D;
  bool hi=cand>maxPwm,lo=cand<-maxPwm;
  if((!hi&&!lo)||(hi&&e<0)||(lo&&e>0))integral=candI;

  if(running){u=constrain(P+integral+D,-maxPwm,maxPwm);motorWrite(u);}
  else{u=0;integral=0;motorStop();}

  Serial.print(now);Serial.print(',');Serial.print(sp,3);Serial.print(',');
  Serial.print(lpf,3);Serial.print(',');Serial.print(e,3);Serial.print(',');
  Serial.print(P,3);Serial.print(',');Serial.print(integral,3);Serial.print(',');
  Serial.print(D,3);Serial.print(',');Serial.print(u,3);Serial.print(',');Serial.println(c);
}
