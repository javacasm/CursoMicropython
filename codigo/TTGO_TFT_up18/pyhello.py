import sys
import time
import machine
import st7789py as st7789
import uos
import random

v = '1.1'

sys.path.append('/pyfonts')
'''
import astrol
import cyrilc
import gotheng
import gothger
import gothita
import greeks
import italicc
import italiccs
import meteo
import music
'''
import romanc
import romancs
import romand
import romanp
import romans
import romant
import scriptc
import scripts

import pytext
'''
fonts = [astrol, cyrilc, gotheng, greeks, italicc, italiccs,
         italiccs, meteo, music, romanc,
         romancs, romand, romanp, romans,
         romant, scriptc, scripts]
'''

fonts = [ romanc, romancs, romand, romanp, romans,
         romant, scriptc, scripts]

def pick_item(sequence):
    div = 0x3fffffff // len(sequence)
    return sequence[random.getrandbits(30) // div]

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
    1,
    baudrate=30000000,
    polarity=1,
    phase=1,
    sck=machine.Pin(SCK_PIN),
    mosi=machine.Pin(MOSI_PIN))

tft = st7789.ST7789(
    spi, tft_width, tft_height,
    reset=machine.Pin(RESET_PIN, machine.Pin.OUT),
    cs=machine.Pin(CS_PIN, machine.Pin.OUT),
    dc=machine.Pin(DC_PIN, machine.Pin.OUT),
    backlight=bl)

tft.init()
tft.fill(st7789.BLACK)

def test_text():
    row = 0
    again = True
    while again:
        color = st7789.color565(
            random.getrandbits(8),
            random.getrandbits(8),
            random.getrandbits(8))

        row += 32

        pytext.text(tft, pick_item(fonts), "Hello!", row, 0, color)

        if row > 192:
            tft.fill(st7789.BLACK)
            row = 0
