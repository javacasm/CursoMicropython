from machine import Pin,SPI
import st7789

bl=Pin(4, Pin.OUT)

tft = st7789.ST7789(
    SPI(2, baudrate=30000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(19)),
    135,
    240,
    reset=Pin(23, Pin.OUT),
    cs=Pin(5, Pin.OUT),
    dc=Pin(16, Pin.OUT),
    backlight=bl)

tft.init()


# bl.on()

tft.fill(st7789.RED)

