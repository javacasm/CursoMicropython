# control of mk3 robotic arm with 4 servos using Kitronik PicoRobotics board
 
import PicoRobotics
import utime

v = 0.2
print(f'{v}')

board = PicoRobotics.KitronikPicoRobotics()

pinza = 4

base = 1
minBase = 10
maxBase = 165

sr = 2
minSr = 30
maxSr = 140

sl= 3
minSr = 100
maxSr = 140


def posicionServos(pBase,pSl,pSr,pPinza):
    board.servoWrite(base, pBase)
    board.servoWrite(sl, pSl)
    board.servoWrite(sr, pSr)
    board.servoWrite(pinza, pPinza)

def barridoServo(servo,delay=50):
    for g in range(10,170):
        board.servoWrite(servo,g)
        print(g, end='\r')
        utime.sleep_ms(delay)

def path1d(servo,min,max,step = 1,delay=50):
    print("rango:",min," ",max)
    for g in range(min,max+1,step):
        board.servoWrite(servo,g)
        print(g, end='\r')
        utime.sleep_ms(delay)
        
        

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

path1d(base,minBase,maxBase,1)
path1d(base,maxBase,minBase,-1)
path1d(sr,minSr,maxSr,1)
path1d(sl,minSl,maxSl,1)
path1d(base,minBase,maxBase,1)
path1d(base,maxBase,minBase,-1)


