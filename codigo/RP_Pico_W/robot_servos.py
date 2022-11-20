# 4 servomotors 360 Robot
#  
import PicoRobotics
import utime


v = 0.1
print(f'robot servos v{v}')

board = PicoRobotics.KitronikPicoRobotics()

# speed 0 - 90 - 180
SPEED_STOP = 90

def _servos(s1,s2,s3,s4):
    ''' tiene en cuenta la orientacion de los motores
    2 1
    4 3
    '''    
    board.servoWrite(1, SPEED_STOP - s1)
    board.servoWrite(2, SPEED_STOP + s2)
    board.servoWrite(3, SPEED_STOP - s3)
    board.servoWrite(4, SPEED_STOP + s4)
    
def forward(speed):
    """  ^ ^
         ^ ^ """
    _servos(speed,speed,speed,speed)

def stop():
    _servos(0,0,0,0)

def backward(speed):
    """  v v
         v v """
    _servos(-speed,-speed,-speed,-speed)


def right(speed):
    """  ^ v
         ^ v """    
    _servos(-speed,speed,-speed,speed)
  
def left(speed):
    """  v ^ 
         v ^ """    
    _servos(speed,-speed,speed,-speed)  
  
