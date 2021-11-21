import machine
import time

import wemosR32
import elegoCar
import motor


v = '0.3.2'

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

m1 = motor.motor(in1, in2, enA)
m2 = motor.motor(in4, in3, enB)

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
    
