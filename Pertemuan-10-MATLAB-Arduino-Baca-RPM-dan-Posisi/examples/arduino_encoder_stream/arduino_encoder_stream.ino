const uint8_t ENC_A=2, ENC_B=3;
const float COUNTS_PER_REV=600.0f; // CHANGE to measured encoder value
const uint32_t SAMPLE_MS=50;

volatile long encoderCount=0;
volatile uint8_t prevState=0;

const int8_t QDEC[16]={
   0,-1, 1, 0,
   1, 0, 0,-1,
  -1, 0, 0, 1,
   0, 1,-1, 0
};

void encoderISR(){
  uint8_t a=digitalRead(ENC_A);
  uint8_t b=digitalRead(ENC_B);
  uint8_t state=(a<<1)|b;
  uint8_t idx=(prevState<<2)|state;
  encoderCount += QDEC[idx];
  prevState=state;
}

void setup(){
  pinMode(ENC_A,INPUT_PULLUP); pinMode(ENC_B,INPUT_PULLUP);
  prevState=(digitalRead(ENC_A)<<1)|digitalRead(ENC_B);
  attachInterrupt(digitalPinToInterrupt(ENC_A),encoderISR,CHANGE);
  attachInterrupt(digitalPinToInterrupt(ENC_B),encoderISR,CHANGE);
  Serial.begin(115200);
  Serial.println("#PROTO,ENCODER_STREAM,1");
  Serial.println("#ms,count,position_deg,rpm_raw,rpm_ma,rpm_lpf");
}

void loop(){
  static uint32_t last=0;
  static long lastCount=0;
  static float maBuf[8]={0}, maSum=0, lpf=0;
  static uint8_t maIdx=0, maN=0;
  uint32_t now=millis();
  if(now-last<SAMPLE_MS) return;
  float dt=(now-last)/1000.0f; last=now;

  noInterrupts(); long c=encoderCount; interrupts();
  long dc=c-lastCount; lastCount=c;
  float rpm=(dc/COUNTS_PER_REV)*60.0f/dt;
  float old=maBuf[maIdx]; maBuf[maIdx]=rpm; maSum += rpm-old;
  maIdx=(maIdx+1)%8; if(maN<8)maN++;
  float ma=maSum/maN;
  const float alpha=0.25f;
  lpf = alpha*ma+(1-alpha)*lpf;
  float deg=(c/COUNTS_PER_REV)*360.0f;

  Serial.print(now);Serial.print(',');
  Serial.print(c);Serial.print(',');
  Serial.print(deg,4);Serial.print(',');
  Serial.print(rpm,4);Serial.print(',');
  Serial.print(ma,4);Serial.print(',');
  Serial.println(lpf,4);
}
