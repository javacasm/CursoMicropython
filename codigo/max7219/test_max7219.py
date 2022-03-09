# test max7219

import max7219
import Wemos
import Wemos

from machine import Pin, SPI
spi = SPI(1)

display = max7219.Matrix8x8(spi,Pin(Wemos.D8),4)
display.text('1234',0,0,1)
display.show()