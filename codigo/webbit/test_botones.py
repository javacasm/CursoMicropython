# test botones

import machine
import time
import webbit

v = 0.2

print(f'test botones {v}')

botonA = machine.Pin(webbit.PIN_BOTON_A)
botonB = machine.Pin(webbit.PIN_BOTON_B)

while True:
    print(f'A:{botonA.value()} B:{botonB.value()}      ',end='\r')
    time.sleep_ms(100)
        