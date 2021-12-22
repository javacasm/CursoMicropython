# based in https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/
from machine import Pin, SoftI2C
import ssd1306
from time import sleep


v= '0.3.1'

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))


oled_width = 128
oled_height = 64
display = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c,addr=0x3c)

def text_test():
    for i in range(0, oled_height + 1 ,8):
        display.text(f'Hello, OLED {i}!', 0, i)
            
    display.show()
    
def scroll_test():
    for i in range(0, oled_width + 1,4):
        display.scroll(4,0)
        display.show()
