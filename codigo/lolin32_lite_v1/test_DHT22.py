import dht
import machine
import time
import MyDateTime
import config
import blinky

sensorDHT22 = dht.DHT22(machine.Pin(config.pinDHT22))
print(f'DHT22 @ {config.pinDHT22}')

v = '0.7.1'

def getData():
    sensorDHT22.measure()
    return (sensorDHT22.temperature(), sensorDHT22.humidity())

def printData():
    try:
        temp,hum = getData()
        print(f'{MyDateTime.getLocalTimeHumanFormat()} ' + f'Hum:{hum} Temp:{temp}')
        blinky.tick(0.02)
    except:
        print('Error de lectura')
        blinky.doubleTick(0.1)
    
def test_forever(espera=5):
    while True:
        printData()
        time.sleep(espera)
