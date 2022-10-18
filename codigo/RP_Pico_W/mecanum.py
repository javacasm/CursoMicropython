import PicoRobotics
import utime


v = 0.6
print(f'mecanum v{v}')

board = PicoRobotics.KitronikPicoRobotics()

# speed 0 - 90 - 180
SPEED_STOP = 90
SPEED_MAXF = 180
SPEED_MAXB = 0

def _servos(s1,s2,s3,s4):
    # tiene en cuenta la orientacion de los motores
    board.servoWrite(1, 90 + s1)
    board.servoWrite(2, 90 - s2)
    board.servoWrite(3, 90 + s3)
    board.servoWrite(4, 90 - s4)
    
def forward(speed):
    """  ^ ^
         ^ ^ """
    _servos(speed,speed,speed,speed)

def q45_right(speed):
    """  ^ 
           ^ """    
    _servos(0,speed,speed,0)

def lateral_left(speed):
    """  v ^
         ^ v """    
    _servos(speed,-speed, -speed, speed)


def stop():
    for i in range(1,5):
        board.servoWrite(i, SPEED_STOP)

def lateral_right(speed):
    """  ^ v
         v ^ """    
    _servos(-speed,speed, speed, -speed)

def backward(speed):
    """  v v
         v v """
    _servos(-speed,-speed,-speed,-speed)

def rot_right_back(speed):
    """  ^ 
         ^  """    
    _servos(0,speed,0,speed)

def rot_center(speed):
    """  ^ v
         ^ v """    
    _servos(-speed,speed,-speed,speed)
    
def rot_back(speed):
    """  ^ v
             """    
    _servos(-speed,speed,0,0)
    
def testServos():
    while True:
        for degrees in range(0,180,10):
            for servo in range(1,5):
                board.servoWrite(servo, degrees)
            utime.sleep_ms(10) #ramp speed over 10x180ms => approx 2 seconds.
        for degrees in range(180,0,-10):
            for servo in range(1,5):
                board.servoWrite(servo, degrees)
            utime.sleep_ms(10) #ramp speed over 10x180ms => approx 2 seconds.

