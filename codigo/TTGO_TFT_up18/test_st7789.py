import time
import random
import machine
import st7789py

# turn on backlight
bl = machine.Pin(4, machine.Pin.OUT)
bl.value(1)

spi = machine.SPI(
    2,
    baudrate=20000000,
    polarity=1,
    phase=1,
    sck=machine.Pin(18),
    mosi=machine.Pin(19))

display = st7789py.ST7789(
    spi, 135, 240,
    reset=machine.Pin(23, machine.Pin.OUT),
    cs=machine.Pin(5, machine.Pin.OUT),
    dc=machine.Pin(16, machine.Pin.OUT))

display.init()

while True:
    display.fill(
        st7789py.color565(
            random.getrandbits(8),
            random.getrandbits(8),
            random.getrandbits(8),
        ),
    )
    time.sleep(2)