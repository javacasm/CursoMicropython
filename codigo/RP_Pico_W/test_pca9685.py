# control of Kiktronik robotic board for Raspi Pico  using  pca9655 code of adafruit 

from machine import SoftI2C,Pin
# Kiktronik robotic board for Raspi Pico
i2c = SoftI2C(sda = Pin(8),scl=Pin(9))
print(i2c.scan())

## Servos index 0-7

from servo import Servos
servos = Servos(i2c,address=108)

for i in range(8):
    print(i)
    servos.position(i,degrees=0)
    sleep(0.3)
    servos.position(i,degrees=90)
    sleep(0.3)
    servos.position(i,degrees=45)
    sleep(0.3)

## Motores 8 - 15
    
from motor_L298 import DCMotors
motores = DCMotors(i2c,address=108)
motores.duty(8,0)
motores.duty(9,4095)    