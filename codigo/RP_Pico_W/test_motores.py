# 4 motors robot using Kittronic PicoRobotic board

import PicoRobotics
import utime

v = 0.3
print(f'{v}')

board = PicoRobotics.KitronikPicoRobotics()

dirForward = 'f'
dirBackward = 'r'

# speed 0 - 100
SPEED_STOP = 0
SPEED_MIN = 30
SPEED_MAX = 100


def stop():
    for i in range(1,5):
        board.motorOn(i,dirForward, SPEED_STOP)

def dir4Sign(speed):
    if speed>0:
        return dirForward
    else:
        return dirBackward

def speedMotor(n,speed):
   board.motorOn(n,dir4Sign(speed), abs(speed)) 

def _motors(s1,s2,s3,s4):
    # tiene en cuenta la orientacion de los motores
    speedMotor(1, s1)
    speedMotor(2, s2)
    speedMotor(3, s3)
    speedMotor(4, s4)
    
def forward(speed):
    """  ^ ^
         ^ ^ """
    _motors(speed,speed,speed,speed)
        
def backward(speed):
    """  v v
         v v """
    _motors(-speed,-speed,-speed,-speed)

def turn_right(speed):
    """  v ^
         v ^ """    
    _motors(speed,speed, -speed, -speed)

def turn_left(speed):
    """  ^ v
         ^ v """    
    _motors(-speed,-speed, speed, speed)

