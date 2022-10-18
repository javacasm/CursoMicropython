## modulo para controlar maqueen desde micro:bit

# License CC by SA @javacasm 2022

# basado en el codigo de la extension original de DFRobot
# de https://github.com/DFRobot/pxt-maqueen/blob/master/maqueen.ts

from microbit import *

v = 0.4

motor_driver_address = 0x10

motor_left = 0
motor_right = 2

CCW = 1
CW = 0

S1 = 0x14
S2 = 0x15

led_left = pin8
led_right = pin12

line_left = pin13
line_right = pin14

def test_i2c():

    print('i2c.scan')

    devs = i2c.scan()
    for dev in devs:
        print(hex(dev))
   
    if len(devs)>0 and devs[0] == motor_driver_address:
        print('devices found @ ',devs, end='')
        if motor_driver_address in devs:
            print(' maqueen found @ ',motor_driver_address)
        else:
            print('no maqueen found')
            
    else:
        print('no device')
    
def mover(dir_left,speed_left,dir_right,speed_right):
    data = bytearray(3)
    data[0] = motor_right # motor: 0 = left, 2 = right
    data[1] = dir_right # direction: 0 = CW, 1 = CCW
    data[2] = speed_right # speed: 0  - 255
    i2c.write(motor_driver_address,data) # 
    data[0] = motor_left
    data[1] = dir_left
    data[2] = speed_left
    i2c.write(motor_driver_address,data)
  

def stop():
    mover(0,0,0,0)


def straight(speed):
    if speed > 0:
        mover(CW,speed,CW,speed)
    else:
        mover(CCW,-speed,CCW,-speed)
        
def turn(speed):
    if speed > 0:
        mover(CW,speed,CCW,speed)
    else:
        mover(CCW,-speed,CW,-speed)    


def servo(s,angle):
    data = bytearray(2)
    data[0] = s
    data[1] = angle
    i2c.write(motor_driver_address,data) #     

def testMove():
    display.show(Image.ARROW_N)
    straight(150)
    sleep(2000)
    turn(-100)
    display.show(Image.ARROW_W)
    sleep(2000)
    turn(100)
    display.show(Image.ARROW_E)
    sleep(2000)
    straight(-150)
    display.show(Image.ARROW_S)
    sleep(2000)
    stop()
    display.clear()

def testLeds():
    pin8.write_digital(1) # left led 
    pin12.write_digital(1) # right led
    sleep(1000)
    pin8.write_digital(0)
    pin12.write_digital(0)

def testServo():
    servo(S1,0)
    sleep(2000)
    servo(S1,90)
    sleep(2000)
    servo(S1,180)
    
def getLines():
    return line_left.read_digital(), line_right.read_digital()

def showLines_forever():
    while True:
        print(getLines(),end='\r')
        sleep(100)



