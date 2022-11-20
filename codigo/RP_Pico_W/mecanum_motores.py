# 4 motors robot using mecanum wheels

import PicoRobotics
import utime


v = 0.2
print(f'mecanum_motores v{v}')

board = PicoRobotics.KitronikPicoRobotics()

dirForward = 'f'
dirBackward = 'r'

# speed 0 - 100
SPEED_STOP = 0
SPEED_MIN = 30
SPEED_MAX = 100


def stop():
    _motors(SPEED_STOP,SPEED_STOP,SPEED_STOP,SPEED_STOP)

def dir4Sign(speed):
    if speed>0:
        return dirForward
    else:
        return dirBackward

def speedMotor(n,speed):
   board.motorOn(n,dir4Sign(speed), abs(speed)) 

def _motors(s1,s2,s3,s4):
    '''   1 2
          4 3 '''
    # tiene en cuenta la orientacion de los motores
    speedMotor(1, s1)
    speedMotor(2, s2)
    speedMotor(4, -s3)
    speedMotor(3, -s4)
    
def forward(speed):
    """  ^ ^
         ^ ^ """
    _motors(speed,speed,speed,speed)

def q45_right(speed):
    """  ^ 
           ^ """    
    _motors(0,speed,speed,0)

def lateral_left(speed):
    """  v ^
         ^ v """    
    _motors(speed,-speed, -speed, speed)

def lateral_right(speed):
    """  ^ v
         v ^ """    
    _motors(-speed,speed, speed, -speed)

def backward(speed):
    """  v v
         v v """
    _motors(-speed,-speed,-speed,-speed)

def rot_right_back(speed):
    """  ^ 
         ^  """    
    _motors(0,speed,0,speed)

def rot_center(speed):
    """  ^ v
         ^ v """    
    _motors(-speed,speed,-speed,speed)
    
def rot_back(speed):
    """  ^ v
             """    
    _motors(-speed,speed,0,0)
