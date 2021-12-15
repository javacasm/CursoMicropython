import dht
import machine
import time
import MyDateTime
import config

sensorDHT22 = dht.DHT22(machine.Pin(config.pinDHT22))

v = '0.6.15'

led = machine.Pin(config.pin_led_builtIn, machine.Pin.OUT)
print(f'Using {"Inverted" if config.LED_INVERTED else ""} led @ {config.pin_led_builtIn} ')
def ledOn():
    # print(f'led({config.pin_led_builtIn}) on')
    if config.LED_INVERTED: led.off()
    else: led.on()
    
def ledOff():
    # print(f'led({config.pin_led_builtIn}) off')
    if config.LED_INVERTED: led.on()
    else: led.off()
    


ledOff()

def tick(duracion):
    ledOn()
    time.sleep(duracion)
    ledOff()

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
        print(f'{MyDateTime.getLocalTimeHumanFormat()} ' + f'Hum:{hum} Temp:{temp}')
        print('antes de tick')
        tick(0.1)
        print('despues de tick')
    except:
        print('Error de lectura')
        doubleTick(0.1)
    
def test_forever():
    while True:
        printData()
        time.sleep(5)
