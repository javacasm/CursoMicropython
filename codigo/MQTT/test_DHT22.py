import dht
import machine
import time
import MyDateTime
import config

sensorDHT22 = dht.DHT22(machine.Pin(14))

v = '0.6.6'

led = machine.Pin(config.pin_led_builtIn, machine.Pin.OUT)
led.off()

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
        print(f'{MyDateTime.getLocalTimeHumanFormat()} '
            + f'Hum:{hum} Temp:{temp}')
        tick(0.1)
    except:
        print('Error de lectura')
        doubleTick(0.1)
    
def test_forever():
    while True:
        printData()
        time.sleep(5)
