# Ejemplo 3 Servo
# Movemos despacio entre 2 posiciones

import machine
import time
import config

servo = machine.PWM(machine.Pin(config.pin_servo),freq = 50)
print(f'servo @ {config.pin_servo} ')

minPos = 70
maxPos = 90
retardo = 5.0

def moveServo(inicial, final, retardo):
    paso = 1
    # retardo /= 1000.0
    if final<inicial:
        paso = -1
    for i in range(inicial,final,paso):
        servo.duty(i)
        time.sleep_ms(retardo)    