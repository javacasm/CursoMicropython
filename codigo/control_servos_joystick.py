import machine
import time
import config

joyYUp = 740
joyYDown = 725

v = '0.1'

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

def initJoys():
    global joyX, joyY
    joyX = setupADC(config.pin_joyX)
    joyY = setupADC(config.pin_joyY)

def readJoys():
    global joyX, joyY
    if joyX == None:
        initJoys()
    return joyX.read(), joyY.read()

def readJoys_forever(espera = 100):
    while True:
        print(f'{readJoys()}  ',end='\r')
        time.sleep_ms(espera)


def setupADC(pin):
    adc = machine.ADC(machine.Pin(pin))
    adc.width(machine.ADC.WIDTH_10BIT)
    adc.atten(machine.ADC.ATTN_11DB)
    return adc

def grados2pos(grados):
    return int((maxPos-minPos)*grados/180+minPos)

def moveServosGrados(gV, gH):
    global servoH, servoV
    if servoH == None:
        initServos()
    servoH.duty(grados2pos(gH))
    servoV.duty(grados2pos(gV))

posicionV = 50
posicionH = 50

def controlServosJoys(espera = 20):
    global posicionH,posicionV
    while True:
        moveServosGrados(posicionV,posicionH)
        jx,jy = readJoys()
        if jy > joyYUp:
            posicionV+=1
        if jy < joyYDown:
            posicionV-=1
        print(f' {jy} {grados2pos(posicionV)} {posicionV} ',end='\r')
        time.sleep_ms(espera)


