#include <Arduino.h>
#include <max6675.h>
const int SCK=52,SO=50,CS=49,SSR=8; MAX6675 tc(SCK,CS,SO);
float sp=50,kp=4,ki=.08,kd=1,integ=0,prevE=0;bool runFlag=false;uint32_t last=0,winStart=0;const uint32_t Ts=500,WINDOW=2000;float outPct=0;
void parse(String s){s.trim();if(s=="START")runFlag=true;else if(s=="STOP"){runFlag=false;digitalWrite(SSR,LOW);}else{int q=s.indexOf('=');if(q<0)return;String k=s.substring(0,q);float v=s.substring(q+1).toFloat();if(k=="SP")sp=constrain(v,25,80);else if(k=="KP")kp=max(0.0f,v);else if(k=="KI")ki=max(0.0f,v);else if(k=="KD")kd=max(0.0f,v);}}
void setup(){Serial.begin(115200);pinMode(SSR,OUTPUT);digitalWrite(SSR,LOW);delay(500);winStart=millis();}
void loop(){if(Serial.available())parse(Serial.readStringUntil('\n'));uint32_t now=millis();if(now-last>=Ts){float dt=(now-last)/1000.0f;last=now;float pv=tc.readCelsius();bool fault=isnan(pv)||pv<0||pv>90;if(fault||!runFlag){outPct=0;integ=0;}else{float e=sp-pv;integ=constrain(integ+e*dt,-500.0f,500.0f);float d=(e-prevE)/max(dt,0.001f);outPct=constrain(kp*e+ki*integ+kd*d,0.0f,100.0f);prevE=e;}Serial.print(now);Serial.print(',');Serial.print(sp);Serial.print(',');Serial.print(pv);Serial.print(',');Serial.println(outPct);}if(now-winStart>=WINDOW)winStart+=WINDOW;uint32_t onMs=(uint32_t)(WINDOW*outPct/100.0f);digitalWrite(SSR,(runFlag && (now-winStart)<onMs)?HIGH:LOW);}
