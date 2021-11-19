# Ejemplo 3 Servo
# Movemos despacio entre 2 posiciones

import machine
import time

D7 = 14

servo7 = machine.PWM(machine.Pin(D7),freq = 50)

minPos = 70
maxPos = 90
retardo = 5.0

def moveServo(pin, inicial, final, retardo):
    paso = 1
    if final<inicial:
        paso = -1
    for i in range(inicial,final,paso):
        servo7.duty(i)
        time.sleep(retardo)    