import dht
import machine
import time
import MyDateTime
import config
from esp8266_i2c_lcd import I2cLcd


v = '0.4.1'

led = machine.Pin(config.pin_led_builtIn, machine.Pin.OUT)

sensorDHT22 = dht.DHT22(machine.Pin(14))

i2c = machine.SoftI2C(sda = machine.Pin(21), scl=machine.Pin(22),freq=100000)
lcd = I2cLcd(i2c, 0x27, 4, 20)

def showLcd(texto):
    lcd.putstr(texto)

def lcdClear():
    lcd.clear()

def tick(duracion):
    led.on()
    time.sleep(duracion)
    led.off()

def doubleTick(duracion):
    tick(duracion)
    time.sleep(duracion)
    tick(duracion)

def getData():
    sensorDHT22.measure()
    return (sensorDHT22.temperature(), sensorDHT22.humidity())

def printData():
    try:
        temp,hum = getData()
        msg1 = f'{MyDateTime.getLocalTimeHumanFormat()} '
        msg2 =  f'Hum:{hum} Temp:{temp}'
        print(msg1 + msg2)
        lcd.clear()
        lcd.putstr(msg1 + '\n' + msg2)
        tick(0.1)
    except Exception as e:
        print(f'Error de lectura {e}')
        doubleTick(0.1)
    
def test_forever():
    lcd.display_on()
    while True:
        lcd.backlight_on()
        printData()
        time.sleep(2)
        lcd.backlight_off()
        time.sleep(3)
