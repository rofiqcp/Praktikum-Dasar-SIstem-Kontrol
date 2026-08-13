#include <Arduino.h>
const uint8_t PWM_CW=5, PWM_CCW=6, ENC_A=2, ENC_B=3, SSR=8;
volatile long enc=0;
void isrEnc(){ enc += (digitalRead(ENC_A)==digitalRead(ENC_B))?1:-1; }
void motor(int pwm){ pwm=constrain(pwm,-80,80); analogWrite(PWM_CW,pwm>0?pwm:0); analogWrite(PWM_CCW,pwm<0?-pwm:0); }
void setup(){ Serial.begin(115200); pinMode(PWM_CW,OUTPUT); pinMode(PWM_CCW,OUTPUT); pinMode(ENC_A,INPUT_PULLUP); pinMode(ENC_B,INPUT_PULLUP); pinMode(SSR,OUTPUT); attachInterrupt(digitalPinToInterrupt(ENC_A),isrEnc,CHANGE); attachInterrupt(digitalPinToInterrupt(ENC_B),isrEnc,CHANGE); digitalWrite(SSR,LOW); Serial.println("MEGA CONTROL TRAINER BRING-UP"); }
void loop(){ static uint32_t t=0; if(millis()-t>=500){t=millis(); Serial.print("ENC=");Serial.println(enc);} motor(0); digitalWrite(SSR,LOW); }
