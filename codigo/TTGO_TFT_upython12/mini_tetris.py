# Tetris

v = '0.6'

import time
import machine
import st7789py as st7789

BL_PIN = 4
SCK_PIN = 18
MOSI_PIN = 19
RESET_PIN = 23
CS_PIN = 5
DC_PIN = 16

tft_width = 135
tft_height = 240

bl = machine.Pin(BL_PIN, machine.Pin.OUT)
bl.on()


spi = machine.SPI(
    2,
    baudrate=30000000,
    polarity=1,
    phase=1,
    sck=machine.Pin(SCK_PIN),
    mosi=machine.Pin(MOSI_PIN))


tft = st7789.ST7789(
    spi, tft_width, tft_height,
    reset=machine.Pin(RESET_PIN, machine.Pin.OUT),
    cs=machine.Pin(CS_PIN, machine.Pin.OUT),
    dc=machine.Pin(DC_PIN, machine.Pin.OUT))

tft.init()


def clear(back_color = st7789.color565(10,10,10)):
    tft.fill(back_color)

## frame
def frame(frame_color = st7789.WHITE, back_color=st7789.color565(10,10,10)):
    tft.fill(back_color)
    tft.vline(0, 0, tft_height-1, frame_color )
    tft.vline(tft_width-1, 0, tft_height-1, frame_color)
    tft.hline(0, tft_height-1, tft_width-1, frame_color)

def tile(x,y,l,r,g,b,ancho = 3):
    tft.fill_rect(x, y ,l, l, st7789.color565(r,g,b))
    c50 = st7789.color565(r+50,g+50,b+50)
    c100 = st7789.color565(r+100,g+100,b+100)
    c3 = st7789.color565(r//3,g//3,b//3)
    c2 = st7789.color565(r//2,g//2,b//2)
    for i in range(1,ancho):
        tft.hline(x + i, y + i, l - 2 * i, c50)
        tft.vline(x + i, y + i, l - 2 * i, c100)
        tft.vline(x + l -i, y + i, l - 2 * i, c3)
        tft.hline(x + i, y + l - i , l - 2 * i, c2)

def test_fill(l = 25 ):
    for x in range(0,tft_width//l):
        for y in range(0,tft_height//l):
            tile(x*l + tft_width%l//2, y*l + tft_height%l//2, l,  x*l,y*l,(x+y)*l//2)

def full():
    clear(st7789.color565(10,10,10))
    frame()
    test_fill()
