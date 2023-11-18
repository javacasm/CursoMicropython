# test botones

import machine
import time
import webbit

v = 0.6

print(f'test botones {v}')

def polling():

    botonA = machine.Pin(webbit.PIN_BOTON_A, Pin.IN)
    botonB = machine.Pin(webbit.PIN_BOTON_B, Pin.IN)

    while True:
        print(f'A:{botonA.value()} B:{botonB.value()}      ',end='\r')
        time.sleep_ms(100)

def pin_change(p):
    pin_n = int(str(p)[4:6])
    if pin_n == webbit.PIN_BOTON_A:
        print('Boton A change')
    elif pin_n == webbit.PIN_BOTON_B:
        print('Boton B change')
    else:
        print('pin change', pin_n)
    
def irqs():
    machine.Pin(webbit.PIN_BOTON_B, machine.Pin.IN).irq(trigger=machine.Pin.IRQ_RISING, handler = pin_change)    
    machine.Pin(webbit.PIN_BOTON_A, machine.Pin.IN).irq(trigger=machine.Pin.IRQ_RISING, handler = pin_change)
    