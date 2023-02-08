# bit:s2
# neopixel test
# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html

leds = neopixel.NeoPixel(machine.Pin(18),25)

leds[0]=(50,100,0)
leds[5]=(0,100,50)
leds[15]=(0,10,50)
leds[10]=(50,10,100)
leds[20]=(0,100,10)
leds.show()
