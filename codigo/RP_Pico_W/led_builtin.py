from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT) # WL_GPIO0 del chip Infineon 43439

tiempo = 0.5

while True:
    led.on()
    print('On')
    sleep(tiempo)
    led.off()
    print('Off')
    sleep(tiempo)