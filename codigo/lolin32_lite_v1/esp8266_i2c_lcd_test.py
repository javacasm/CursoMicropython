"""Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from time import sleep_ms, ticks_ms
from machine import SoftI2C, Pin
from esp8266_i2c_lcd import I2cLcd

v = '0.3'

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 39 # 0x27

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = SoftI2C(sda = Pin(21),scl=Pin(22),freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 4, 20)
    lcd.putstr("It Works!\n     Second Line\n       3rd line\n          4th & last")
    sleep_ms(3000)
    lcd.clear()
    count = 0
    while True:
        lcd.move_to(0, 0)
        lcd.putstr("%7d" % (ticks_ms() // 1000))
        sleep_ms(1000)
        count += 1
        if count % 10 == 3:
            print("Turning backlight off")
            lcd.backlight_off()
        if count % 10 == 4:
            print("Turning backlight on")
            lcd.backlight_on()
        if count % 10 == 5:
            print("Turning display off")
            lcd.display_off()
        if count % 10 == 6:
            print("Turning display on")
            lcd.display_on()
        if count % 10 == 7:
            print("Turning display & backlight off")
            lcd.backlight_off()
            lcd.display_off()
        if count % 10 == 8:
            print("Turning display & backlight on")
            lcd.backlight_on()
            lcd.display_on()

#if __name__ == "__main__":
test_main()
