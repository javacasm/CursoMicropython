import machine
import time

'''
Pines ESP32: 0-19, 21-23, 25-27, 32-39
Pins 1 and 3 are REPL UART TX and RX respectively

Pins 6, 7, 8, 11, 16, and 17 are used for connecting the embedded flash, and are not recommended for other uses

Pins 34-39 are input only, and also do not have internal pull-up resistors

'''

v = 0.2

pins = (0,2,4,5,9,10,12,13,14,15, 18, 19, 21,22,23,25,26,27,32,33)

leds = []

def test_all(espera = 500):
    for pin in pins:
        led = machine.Pin(pin, machine.Pin.OUT)
        leds.append(led)
        print(f' {pin} On ',end = '')
        led.on()
        time.sleep_ms(espera)
        print(' Off')
        led.off()
    
