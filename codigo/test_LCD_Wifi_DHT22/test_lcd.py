import dht
import machine
import time
import utime
import MyDateTime
import config
from esp8266_i2c_lcd import I2cLcd
import test_DHT22
import test_touch

v = '0.7.5'


i2c = machine.SoftI2C(sda = machine.Pin(config.pinSDA), scl=machine.Pin(config.pinSCL),freq=100000)
lcd = I2cLcd(i2c, config.lcd_i2c_address, 4, 20)
print(f'Using I2C @ SDA:{config.pinSDA} SCL:{config.pinSCL}')


def showLcd(texto):
    lcd.putstr(texto)

def lcdClear():
    lcd.clear()


def printData():
    try:
        temp,hum = test_DHT22.getData()
        msg1 = f'{MyDateTime.getLocalTimeHumanFormat()} '
        msg2 =  f'Hum:{hum:.2f} Temp:{temp:.2f} '
        print(msg1 + msg2)
        #lcd.clear()
        lcd.move_to(0,1)
        lcd.putstr(msg1 + '\n' + msg2)
        test_DHT22.tick(0.1)
    except Exception as e:
        print(f'Error de lectura {e}')
        test_DHT22.doubleTick(0.1)
    
def is_lcd_detected():
    i2c_devices = i2c.scan()
    if len(i2c_devices) < 1 or i2c_devices[0] != config.lcd_i2c_address:
        print(f'No lcd detected at {config.lcd_i2c_address}')
        return False
    else:
        print(f'Lcd detected @ {config.lcd_i2c_address}')
        return True


def test_forever(everySeconds = 30):
    if not is_lcd_detected():
        return
    lcd.display_on()
    lcd.hide_cursor()
    
    last_Temp = 0 # utime.ticks_ms()
    while True :
        now = utime.ticks_ms()
        if test_touch.tPad.read() < 400:
            last_Temp = 0
            lcd.backlight_on()
        else :
            lcd.backlight_off()
        if  last_Temp == 0 or utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            printData()
            last_Temp = now
