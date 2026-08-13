#include <Arduino.h>

static constexpr uint8_t ENC_A=2, ENC_B=3, ADC_PIN=A1;
static float countsPerRev=600.0f;
static uint16_t sampleMs=50;
static float alpha=.25f;
static uint8_t maN=8;

volatile int32_t encoderCount=0;
volatile uint8_t prevState=0;
static const int8_t QDEC[16]={0,-1,1,0,1,0,0,-1,-1,0,0,1,0,1,-1,0};

// Estimator state is global so ZERO can reset count and speed history
// together. This prevents a false RPM spike after changing the reference.
static int32_t lastCount=0;
static float rpmRing[16]={0};
static uint8_t ringIndex=0,ringSamples=0;
static float rpmLpf=0;

void encoderISR(){
  const uint8_t s=(digitalRead(ENC_A)<<1)|digitalRead(ENC_B);
  encoderCount+=QDEC[(prevState<<2)|s];
  prevState=s;
}

int32_t readCount(){
  noInterrupts();
  const int32_t c=encoderCount;
  interrupts();
  return c;
}

void resetEncoderEstimator(){
  noInterrupts();
  encoderCount=0;
  lastCount=0;
  interrupts();
  for(uint8_t i=0;i<16;i++)rpmRing[i]=0;
  ringIndex=0;
  ringSamples=0;
  rpmLpf=0;
}

void handleCommand(String line){
  line.trim();
  const int comma=line.indexOf(',');
  if(comma<0)return;
  String key=line.substring(0,comma),val=line.substring(comma+1);
  key.toUpperCase();

  if(key=="ZERO"&&val.toInt()!=0)resetEncoderEstimator();
  else if(key=="TS")sampleMs=constrain(val.toInt(),10,300);
  else if(key=="ALPHA")alpha=constrain(val.toFloat(),0.0f,1.0f);
  else if(key=="MA")maN=constrain(val.toInt(),1,16);
  else if(key=="CPR")countsPerRev=max(1.0f,val.toFloat());
  else if(key=="STATUS"){
    Serial.print("#STATUS,TS=");Serial.print(sampleMs);
    Serial.print(",ALPHA=");Serial.print(alpha,3);
    Serial.print(",MA=");Serial.print(maN);
    Serial.print(",CPR=");Serial.println(countsPerRev,3);
  }
}

void setup(){
  pinMode(ENC_A,INPUT_PULLUP);
  pinMode(ENC_B,INPUT_PULLUP);
  prevState=(digitalRead(ENC_A)<<1)|digitalRead(ENC_B);
  attachInterrupt(digitalPinToInterrupt(ENC_A),encoderISR,CHANGE);
  attachInterrupt(digitalPinToInterrupt(ENC_B),encoderISR,CHANGE);
  Serial.begin(115200);
  Serial.setTimeout(5);
  Serial.println("#PROTO,IO_MONITOR,2");
  Serial.println("#ms,adc_raw,voltage,count,position_deg,rpm_raw,rpm_ma,rpm_lpf");
}

void loop(){
  while(Serial.available())handleCommand(Serial.readStringUntil('\n'));

  static uint32_t last=0;
  const uint32_t now=millis();
  if(now-last<sampleMs)return;
  const float dt=(now-last)/1000.0f;
  last=now;

  const int adc=analogRead(ADC_PIN);
  const float voltage=adc*(5.0f/1023.0f);
  const int32_t c=readCount();
  const int32_t dc=c-lastCount;
  lastCount=c;
  const float rpm=(dc/countsPerRev)*60.0f/dt;

  rpmRing[ringIndex]=rpm;
  ringIndex=(ringIndex+1)%16;
  if(ringSamples<16)ringSamples++;
  const uint8_t n=min(maN,ringSamples);
  float sum=0;
  for(uint8_t k=0;k<n;k++){
    int idx=(int)ringIndex-1-k;
    if(idx<0)idx+=16;
    sum+=rpmRing[idx];
  }
  const float ma=sum/(n?n:1);
  rpmLpf=alpha*ma+(1.0f-alpha)*rpmLpf;
  const float deg=(c/countsPerRev)*360.0f;

  Serial.print(now);Serial.print(',');Serial.print(adc);Serial.print(',');
  Serial.print(voltage,4);Serial.print(',');Serial.print(c);Serial.print(',');
  Serial.print(deg,4);Serial.print(',');Serial.print(rpm,4);Serial.print(',');
  Serial.print(ma,4);Serial.print(',');Serial.println(rpmLpf,4);
}
