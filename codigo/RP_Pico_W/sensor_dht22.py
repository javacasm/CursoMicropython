# DHT22 test
from dht import DHT22
from machine import Pin
from time import sleep

sensor = DHT22(Pin(2))



while True:
    sensor.measure()
    print(f'T: {sensor.temperature()} H: {sensor.humidity()}')
    
    sleep(1)    