"""Offline smoke-test simulator for the final integrated control trainer.
Runs HEATER, MOTOR_SPEED, and MOTOR_POSITION modes without hardware.
"""
import math
from dataclasses import dataclass

@dataclass
class PID:
    kp: float; ki: float; kd: float; lo: float; hi: float
    integ: float = 0.0; prev: float = 0.0
    def step(self, sp, pv, dt):
        e = sp - pv
        d = (e-self.prev)/dt
        candidate = self.integ + e*dt
        u0 = self.kp*e + self.ki*candidate + self.kd*d
        u = max(self.lo, min(self.hi, u0))
        if u == u0 or (u == self.hi and e < 0) or (u == self.lo and e > 0):
            self.integ = candidate
        self.prev = e
        return u

def heater_demo():
    dt=0.2; temp=25.0; ambient=25.0; sp=50.0
    pid=PID(7.0,0.12,0.0,0,100)
    for k in range(int(180/dt)):
        u=pid.step(sp,temp,dt)
        temp += dt*(0.055*u - 0.055*(temp-ambient))
    return temp, u

def motor_speed_demo():
    dt=0.01; speed=0.0; sp=180.0
    pid=PID(1.1,0.9,0.01,-255,255)
    for _ in range(int(5/dt)):
        u=pid.step(sp,speed,dt)
        speed += dt*((1.15*u)-speed)/0.18
    return speed, u

def motor_position_demo():
    dt=0.01; pos=0.0; speed=0.0; sp=360.0
    pid=PID(2.0,0.12,0.12,-255,255)
    for _ in range(int(8/dt)):
        u=pid.step(sp,pos,dt)
        speed += dt*((0.8*u)-speed)/0.12
        pos += speed*dt
    return pos, u

if __name__ == '__main__':
    ht,hu=heater_demo(); ms,mu=motor_speed_demo(); mp,pu=motor_position_demo()
    print(f'HEATER       PV={ht:7.2f} C   output={hu:7.2f} %')
    print(f'MOTOR_SPEED  PV={ms:7.2f}     output={mu:7.2f}')
    print(f'MOTOR_POS    PV={mp:7.2f}     output={pu:7.2f}')
    checks=[abs(ht-50)<2.5, abs(ms-180)<10, abs(mp-360)<15]
    print('SMOKE_TEST:', 'PASS' if all(checks) else 'CHECK_TUNING')
