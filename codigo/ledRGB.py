import machine


led_red = machine.PWM(machine.Pin(12), freq = 500)
led_green = machine.PWM(machine.Pin(13), freq = 500)
led_blue = machine.PWM(machine.Pin(5), freq = 500)

def color(r,g,b):
    led_red.duty(r)
    led_green.duty(g)
    led_blue.duty(b)

def gray(bright):
    color(bright,bright,bright)

def black():
    gray(0)

def white():
    gray(1023)
