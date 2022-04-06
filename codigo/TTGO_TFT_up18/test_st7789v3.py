import machine
import st7789py as st7789
import random
import time

v = 0.3

'''
Pines SPI
GPIO 19  - Din / MOSI
GPIO 18  - Clk / SCLK

CS: 5
DC: 16
RST: 23
BL: 14
'''
MOSI_PIN = 19
SCLK_PIN = 18
CS_PIN = 5 
RES_PIN = 23 
DC_PIN = 16 
BL_PIN = 14

bl = machine.Pin(4, machine.Pin.OUT)
tft_width = 135
tft_height = 240
spi = machine.SPI(1, baudrate=30000000, polarity=1, phase=1, sck=machine.Pin(SCLK_PIN), mosi=machine.Pin(MOSI_PIN))
tft = st7789.ST7789(spi,
                    tft_width,
                    tft_height,
                    reset = machine.Pin(RES_PIN, machine.Pin.OUT),
                    cs = machine.Pin(CS_PIN, machine.Pin.OUT),
                    dc = machine.Pin(DC_PIN, machine.Pin.OUT),
                    backlight=bl,
                    rotation=0)
tft.init()


# bl.on()

while True:
    tft.fill(
        st7789.color565(
            random.getrandbits(8),
            random.getrandbits(8),
            random.getrandbits(8),
        ),
    )
    time.sleep_ms(500)