import machine
import time

import wemosR32
import elegoCar
import motor


v = '0.4.2'

pinServo = 25 # D3

minServo = 45
centralServo = 80
maxServo = 115

enA = 16 # D5
in1 = 14 # D7
in2 = 12 # D8
in3 = 13 # D9
in4 = 23 # D11
enB = 27 # D6

maxSpeed = 1023

servoUS = machine.PWM(machine.Pin(pinServo), freq = 50)
servoUS.duty(centralServo)


m1 = motor.motor(in1, in2, enA)
m1.stop()
m2 = motor.motor(in4, in3, enB)
m2.stop()

# sensor siguelineas

SL_L = 26 # D2
SL_C = 17 # D4
SL_R = 5  # D10

sensorSL_L = machine.Pin(SL_L, machine.Pin.IN)
sensorSL_C = machine.Pin(SL_C, machine.Pin.IN)
sensorSL_R = machine.Pin(SL_R, machine.Pin.IN)

def testSL():
    while True:
        print(f'{sensorSL_L.value()} - {sensorSL_C.value()} - {sensorSL_R.value()}')
        time.sleep(0.5)


def testM1():
    testMotor(m1)

def testMotor(m):
    for speed in range(-1 * maxSpeed, maxSpeed, 100):
        print(f'Speed:{speed}')
        m.move(speed)
        time.sleep(0.2)
    m.stop()

def adelante(speed):
    m1.move(speed)
    m2.move(speed)

def testRobot():
    for speed in range(-1 * maxSpeed, maxSpeed, 100):
        print(f'Speed:{speed}')
        adelante(speed)
        time.sleep(0.2)
    adelante(0)
    

def testServo():
    for pos in range (minServo,maxServo):
        servoUS.duty(pos)
        print(pos)
        time.sleep(0.02)
    for pos in range (maxServo,minServo,-1):
        servoUS.duty(pos)
        print(pos)
        time.sleep(0.02)        
    servoUS.duty(centralServo)
    time.sleep(0.5)
    print('centrado')
    
