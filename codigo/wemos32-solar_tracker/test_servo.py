# Ejemplo 3 Servo
# Movemos despacio entre 2 posiciones

import machine
import time
import config

v = '0.5.1'

servoV = machine.PWM(machine.Pin(config.pin_servoV),freq = 50)
servoH = machine.PWM(machine.Pin(config.pin_servoH),freq = 50)

print(f'servoV @ {config.pin_servoV} ' + f'servoH @ {config.pin_servoH} ')
print(f'ADCs: {config.pin_ldr00} {config.pin_ldr01} {config.pin_ldr10} {config.pin_ldr11} ')

minPos = 30
maxPos = 90
retardo = 5

adc00 = machine.ADC(machine.Pin(config.pin_ldr00))
adc01 = machine.ADC(machine.Pin(config.pin_ldr01))
adc10 = machine.ADC(machine.Pin(config.pin_ldr10))
adc11 = machine.ADC(machine.Pin(config.pin_ldr11))


def readLDRs():
    return adc00.read(), adc01.read(), adc10.read(), adc11.read()

def moveRangoServo(servo, inicial = minPos, final = maxPos, retardo = retardo):
    paso = 1
    if final<inicial:
        paso = -1
    for i in range(inicial,final,paso):
        servo.duty(i)
        time.sleep_ms(retardo)

def pos2grados(pos):
    return int(180.0*(pos-minPos)/(maxPos-minPos))

def grados2pos(grados):
    return int((maxPos-minPos)*grados/180+minPos)

def moveServos(gV,gH):
    servoH.duty(grados2pos(gH))
    servoV.duty(grados2pos(gV))

def testRangos(minV = 0,maxV=180, minH = 0,maxH=180):
    for h in range(minH,maxH,10):
        for v in range(minV, maxV,10):
            moveServos(v,h)
            time.sleep_ms(retardo*10)
            print(h,v,readLDRs())
        moveRangoServo(servoV,inicial=pos2grados(180),final = pos2grados(0))

# moveServos(90,90)


