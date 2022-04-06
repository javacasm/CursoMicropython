from machine import Pin, SPI
import st7789
import dht
import time
import machine
import random

v = 0.4
#Importa fuentes
import vga1_bold_16x32 as font1
import vga1_16x16 as font2

tft_width = 135
tft_height = 240

spi = SPI(1, baudrate=30000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(19))
tft = st7789.ST7789(
     spi,
     tft_width,
     tft_height,
     reset=Pin(23, Pin.OUT),
     cs=Pin(5, Pin.OUT),
     dc=Pin(16, Pin.OUT),
     backlight=Pin(4, Pin.OUT),
     rotation=0)
tft.init()

def test_sensor_forever():
    tft.rotation(3)

    while True:
        # dht11.measure()
        # temp = dht11.temperature()
        # hum = dht11.humidity()
        temp = 21.3
        hum = 25.1
        print('Temperatura: ',temp,'ºC Humedad: ',hum,'%')
        tft.text (font1, "Temperatura:", 0, 0)
        tft.text (font1, str(temp)+' C', 0,34)
        tft.text (font1, "Humedad:", 0, 68)
        tft.text (font1, str(hum)+'%', 0,102)
        time.sleep(1)
 
def randomLines(N=1000):
    for i in range(N):
        tft.line(random.randrange(tft_width),random.randrange(tft_height),
                  random.randrange(tft_width),random.randrange(tft_height),
                  st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8),
                    ))
