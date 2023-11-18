# bit:s2
# neopixel test
# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html

import machine
import neopixel

import webbit

v = 0.8

print(f'test_neopixel {v}')

BLACK = (0,0,0)

leds = neopixel.NeoPixel(machine.Pin(webbit.PIN_NEOPIXEL), webbit.N_NEOPIXEL)


def color(colorRGB):
    for i in range(webbit.N_NEOPIXEL):
        leds[i] = colorRGB
    leds.write()    

def clear():
    color(BLACK)

def test_basic():

    leds[0]=(50,100,0)
    leds[5]=(0,100,50)
    leds[15]=(0,10,50)
    leds[10]=(50,10,100)
    leds[20]=(0,100,10)
    leds.write()

def rainbow():
    for i in range(5):
        for j in range(5):
            leds[i*5+j]=(i*30,0,j*30)
    leds.write()
    
    
def test_speed():
    for i in range(0,150,10):
        for j in range(0,150,10):
            for k in range(0,150,10):
                color((i,j,k))
                print(f'({i},{j},{k})',end='\r')