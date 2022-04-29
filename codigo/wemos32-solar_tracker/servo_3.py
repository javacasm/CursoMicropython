# Ejemplo 3 Servo
# Movemos despacio entre 2 posiciones

import machine
import time
import config

servov = machine.PWM(machine.Pin(config.pin_servoV),freq = 50)
servoh = machine.PWM(machine.Pin(config.pin_servoH),freq = 50)

print(f'servoV @ {config.pin_servoV} ')
print(f'servoH @ {config.pin_servoH} ')

minPos = 70
maxPos = 90
retardo = 5.0

def moveServos(servo, inicial, final, retardo):
    paso = 1
    # retardo /= 1000.0
    if final<inicial:
        paso = -1
    for i in range(inicial,final,paso):
        servo.duty(i)
        time.sleep_ms(retardo)    