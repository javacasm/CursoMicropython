# trabajando con varios leds
import machine

v = 0.1 

pin_leds = (26, 25, 17, 16, 27, 14, 12, 13)
leds = []

def inicializar():
    for pin in pin_leds:
       print(pin)
       led = machine.Pin(pin, machine.Pin.OUT)
       leds.append(led)

def encenderTodos():
    for led in range(0,7+1):
        leds[led].on() 

def apagarTodos():
    for led in range(0,7+1):
        leds[led].off()    