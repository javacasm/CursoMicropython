import time
from motor import *
from motor import motorL298 as motor
from machine import SoftI2C, Pin
from BME280 import BME280

import config
import u_ina219

v = 0.7

def command(r):
    factor = 100    
    if ',' in r:
        rs=r.split(',')
        speedl=int(eval(rs[0]))
        speedr=int(eval(rs[1]))
    elif r == 'R':
        speedl = 0
        speedr = MED_SPEED
    elif r == 'L':
        speedr = 0
        speedl = MED_SPEED        
    else:
        speedl=speedr = int(eval(r))
    ml.go(speedl*factor)
    mr.go(speedr*factor)    

devs = []

def get_consum():
    global devs
    if devs == []:
        devs= u_ina219.init_all(config.SDA,config.SCL)
    return u_ina219.read_all(devs)

myi2c = None

def get_meteo():
    global myi2c
    if myi2c==None:
        myi2c = SoftI2C(scl = Pin(config.SCL), sda = Pin(config.SDA))
    bme = BME280(i2c = myi2c, address=0x76) 
    return bme.temperature, bme.humidity, bme.pressure
    


def control():
    while True:
        try:
            r = input(f'\r{get_consum()} {get_meteo()} speed: ').upper()
            if r == 'Q':
                print('bye')
                break;
            else:
                command(r)
        except Exception as e:
            print(e,end='\r')
            time.sleep_ms(500)
        

ml = motor(config.IN3, config.IN4, config.ENB)
mr = motor(config.IN1, config.IN2, config.ENA)
    
