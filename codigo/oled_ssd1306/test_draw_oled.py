import machine
import time

v = 0.3

import ssd1306

# Configuramos i2c

i2c = machine.SoftI2C(scl = machine.Pin(21), sda = machine.Pin(22))

# Configuracion del oled
oled_width = 128
oled_height = 64
display = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c,addr=0x3c)

# Declaramos el joystick

joyX = machine.ADC(machine.Pin(35))
joyX.atten(machine.ADC.ATTN_11DB)

joyX.width(machine.ADC.WIDTH_9BIT)
joyY = machine.ADC(machine.Pin(32))
joyY.width(machine.ADC.WIDTH_9BIT)
joyY.atten(machine.ADC.ATTN_11DB)

# El pulsador del joystick
switch = machine.Pin(34,machine.Pin.IN, machine.Pin.PULL_DOWN)

def control_dot():

    display.fill(0)
    display.show()
    x = 0
    y = 0
    while True:
        joyx = joyX.read()
        joyy = joyY.read()
        print(f'{switch.value()} ({joyx},{joyy}) ',end = '\r')
        time.sleep_ms(100)
        display.pixel(x,y,0)
        x = int(oled_width * (511-joyx)/512)
        y = int(oled_height * (511-joyy)/512)
        display.pixel(x,y,1)
        display.show()

def movePixel(borra = True):
    display.fill(0)
    display.show()
    x = oled_width//2
    y = oled_height//2
    while True:
        joyx = (511-joyX.read())//10-23
        joyy = joyY.read()//10-23
        if borra :
            display.pixel(x,y,0)
        x += int(joyx/10)
        y += int(joyy/10)
        x = x%oled_width
        y = y%oled_height
        print(f'{switch.value()} ({joyx:2d},{joyy:2d}) -> ({x:3d},{y:3d})',end = '\r')
        display.pixel(x,y,1)
        display.show()