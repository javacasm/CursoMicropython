# Ejemplo 3 Servo
# Movemos despacio entre 2 posiciones

import machine
import time
import config

v = '0.7.6'

adc00 = adc01 = adc10 = adc11 = None
servoH = servoV = None
joyX = joyY = None

minPos = 40
maxPos = 115
retardo = 5


def initServos():
    global servoV,servoH
    servoV = machine.PWM(machine.Pin(config.pin_servoV),freq = 50)
    servoH = machine.PWM(machine.Pin(config.pin_servoH),freq = 50)
    print(f'servoV @ {config.pin_servoV} ' + f'servoH @ {config.pin_servoH} ')
    # print(f'ADCs: {config.pin_ldr00} {config.pin_ldr01} {config.pin_ldr10} {config.pin_ldr11} ')


def setupADC(pin):
    adc = machine.ADC(machine.Pin(pin))
    adc.width(machine.ADC.WIDTH_10BIT)
    adc.atten(machine.ADC.ATTN_11DB)
    return adc

def initADCs():
    global adc00, adc01, adc10, adc11
    adc00 = setupADC(config.pin_ldr00)
    adc01 = setupADC(config.pin_ldr01)
    adc10 = setupADC(config.pin_ldr10)
    adc11 = setupADC(config.pin_ldr11)

def initJoys():
    global joyX, joyY
    joyX = setupADC(config.pin_joyX)
    joyY = setupADC(config.pin_joyY)

def readJoys():
    global joyX, joyY
    if joyX == None:
        initJoys()
    return joyX.read(), joyY.read()

def readLDRs():
    global adc00, adc01, adc10, adc11
    if adc00 == None:
        initADCs()
    return adc00.read(), adc01.read(), adc10.read(), adc11.read()

def moveRangoServo(servo, inicial = minPos, final = maxPos, retardo = retardo):
    global servoH, servoV
    paso = 1
    if final<inicial:
        paso = -1
    for i in range(inicial,final,paso):
        servo.duty(i)
        time.sleep_ms(retardo)

def adc2grado(v):
    return v * 180 // 1023

def pos2grados(pos):
    return int(180.0*(pos-minPos)/(maxPos-minPos))

def grados2pos(grados):
    return int((maxPos-minPos)*grados/180+minPos)

def moveServos(gV, gH):
    global servoH, servoV
    if servoH == None:
        initServos()
    servoH.duty(grados2pos(gH))
    servoV.duty(grados2pos(gV))

def testRangos(minV = 0,maxV=180, minH = 0,maxH=180):
    global servoH, servoV
    for h in range(minH,maxH,10):
        for v in range(minV, maxV,10):
            moveServos(v,h)
            time.sleep_ms(retardo*10)
            print(h,v,readLDRs())
        moveRangoServo(servoV,inicial=pos2grados(180),final = pos2grados(0))


def controlServosWithJoys_forever():
    while True:
        controlServosWithJoys()
        
def controlServosWithJoys(show = True):
    jx,jy = readJoys()
    gx = adc2grado(jx)
    gy = adc2grado(jy)
    if show:
        print(f'{jx:3d} > {gx:3d} {jy:3d} > {gy:3d} \r',end='')
    moveServos(gy,gx)

def readLDRs_forever(pausa = 50):
    while True:
        print(f'{readLDRs()  }  ',end='\r')
        time.sleep_ms(pausa)    


def fullControl(pausa=50):
    while True:
        print(f'{readLDRs()}  ',end='\r')
        controlServosWithJoys(show = False)
        

# moveServos(50,50)


