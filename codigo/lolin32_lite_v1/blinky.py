import machine
import time

import config

v = '0.5.3'

led = machine.Pin(config.pin_led_builtIn, machine.Pin.OUT)
print('Led @ {config.pin_led_builtIn}')

def ledOn():
    # print(f'led({config.pin_led_builtIn}) on')
    if config.LED_INVERTED: led.off()
    else: led.on()
    
def ledOff():
    # print(f'led({config.pin_led_builtIn}) off')
    if config.LED_INVERTED: led.on()
    else: led.off()
    
def tick(duracion):
    ledOn()
    time.sleep(duracion)
    ledOff()

def doubleTick(duracion):
    tick(duracion)
    time.sleep(duracion)
    tick(duracion)

def blink(espera=1):
    while True:
        ledOn()
        print('On')        
        time.sleep(espera)
        ledOff()
        print('Off')
        time.sleep(espera)

print(f'Using {"Inverted" if config.LED_INVERTED else ""} led @ {config.pin_led_builtIn} ')
ledOff()