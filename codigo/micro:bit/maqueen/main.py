from microbit import *

print('i2c.scan')

devs = i2c.scan()
for dev in devs:
    print(hex(dev))
    

motor_driver_address = 0x10

motor_left = 0
motor_right = 2

CCW = 1
CW = 0

S1 = 0x14
S2 = 0x15

if len(devs)>0 and devs[0] == motor_driver_address:
    print('device found @ ',devs[0])
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

servo(S1,0)
sleep(2000)
servo(S1,90)
sleep(2000)
servo(S1,180)

