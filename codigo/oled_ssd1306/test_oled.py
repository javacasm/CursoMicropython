import machine  
import ssd1306
import time 
import random

v= '0.5'

# Creamos el objeto i2c con los pines 21 (SCL)  y 22 (SDA)
i2c = machine.SoftI2C(scl = machine.Pin(21), sda = machine.Pin(22))


oled_width = 128 # ancho
oled_height = 64 # alto
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c, addr=0x3c) # Podria ser tambien 0x34

def show_text():
    for i in range(0, oled_height + 1 ,8):
        oled.text(f'Linea numero {i}', 0, i) # altura del texto 8 pixels
            
    oled.show() # Mostramos el contenido
    
def scroll_display(scroll_x = -4, scroll_y = -2):
    for i in range(0, oled_width + 1,4):
        oled.scroll(scroll_x, scroll_y)
        oled.show()

def slow_fill(finalShow = False,color = 1):
    for x in range(oled_width):
        for y in range(oled_height):
            oled.pixel(x,y,color)
            if not finalShow:
                oled.show()
    if finalShow:
        oled.show()

def randomLines(N=100,finalShow = False):
    for i in range(N):
        oled.line(random.randrange(oled_width),random.randrange(oled_height),
                  random.randrange(oled_width),random.randrange(oled_height),
                  1)
        if not finalShow:
            oled.show()
    if finalShow:
        oled.show()

def randomRects(N=100,finalShow = False):
    for i in range(N):
        oled.rect(random.randrange(oled_width),random.randrange(oled_height),
                  random.randrange(oled_width),random.randrange(oled_height),
                  1)
        if not finalShow:
            oled.show()
    if finalShow:
        oled.show()
