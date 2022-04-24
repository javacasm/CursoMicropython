# IMPORTS
import utime as time
from machine import SoftI2C, Pin, RTC
from random import getrandbits
from ht16k33matrixfeatherwing import HT16K33MatrixFeatherWing

# CONSTANTS
DELAY = 0.01
PAUSE = 3

# START
def test():
    i2c = SoftI2C(sda = Pin(21),scl = Pin(22),freq=100000)
    print(i2c.scan())
    display = HT16K33MatrixFeatherWing(i2c)
    display.set_brightness(2)

    # Show some charset characters on the LED
    
    sync_text = "BOO"
    print(sync_text)
    col = 0
    for i in range(len(sync_text)):
        display.set_character(ord(sync_text[i]), col)
        col += 5
    display.draw()
    time.sleep(PAUSE)

    # Store custom characters
    print('Custom char')
    icon = b"\x3C\x42\xA9\x85\x85\xA9\x42\x3C"
    display.clear().set_icon(icon, 4).draw()
    time.sleep(PAUSE)

    # Store custom characters
    print('More custom char')
    icon = b"\x00\x00\x0E\x18\xBE\x6D\x3D\x3C"
    display.define_character(icon, 0)
    icon = b"\x3C\x3D\x6D\xBE\x18\x0E\x00\x00"
    display.define_character(icon, 1)
    display.clear().set_character(0, 0).set_character(1, 8).draw()
    time.sleep(PAUSE)

    # Scroll text
    print('Scroll!')
    display.clear().draw()
    text = "        0123456789 abcdefghijklmnopqrstuvwxyz !$%&*() \x00\x01        "
    display.scroll_text(text)
    time.sleep(PAUSE)

    # Plot random spots
    print('Random points')
    display.clear().draw()
    for i in range(32):
        while True:
            x = getrandbits(4)
            y = getrandbits(3)
            if not display.is_set(x, y): break
        display.plot(x, y).draw()
        time.sleep(0.5)
    time.sleep(PAUSE)

    # Invert the LED
    print('Invert!')
    display.set_inverse().draw()
    time.sleep(PAUSE)

    # De-invert the LED
    print('DeInvert!')
    display.set_inverse().draw()

    # And flash the display
    print('Flash')
    display.set_blink_rate(1)