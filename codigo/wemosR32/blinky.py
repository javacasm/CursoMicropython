import machine
import time

import config

v = '0.4'



led = machine.Pin(config.pin_led_builtIn, machine.Pin.OUT)

while True:
    led.on()
    time.sleep(1)
    print('On')
    led.off()
    print('Off')
    time.sleep(1)