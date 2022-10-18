import PicoRobotics
import utime

board = PicoRobotics.KitronikPicoRobotics()

# speed 0 - 90 - 180
SPEED_STOP = 90
SPEED_MAXF = 180
SPEED_MAXB = 0

def stop():
    for i in range(1,5):
        board.servoWrite(i, SPEED_STOP)


def forward(speed):
    """  ^ ^
         ^ ^ """
    for i in range(1,5):
        board.servoWrite(i,speed)
        
def backward(speed):
    """  v v
         v v """
    for i in range(1,5):
        board.servoWrite(i,90 - speed)

def right(speed):    
    board.servoWrite(1, speed)
    board.servoWrite(2, 90-speed)
    board.servoWrite(3, speed)
    board.servoWrite(4, 90-speed)

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

