import machine
import time

v = 0.5

pins = (5, 18, 19, 23)

buttons = []

last = time.ticks_ms()
def irq(value):
    global last
    now = time.ticks_ms()
    if now - last > 200:
        last = now
        print(f'press {time.ticks_ms()} {value} es {pins[buttons.index(value)]}')
        
for pin in pins:
    boton = machine.Pin(pin, machine.Pin.IN)
    boton.irq(trigger=machine.Pin.IRQ_RISING, handler=irq)
    buttons.append(boton)
    






