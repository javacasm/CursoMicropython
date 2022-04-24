import dht
import machine
import time

DHT_pin = 14

sensor = dht.DHT22(machine.Pin(DHT_pin))
def showSensorData():
    sensor.measure()
    print("Temperatura = ",sensor.temperature(),"Humedad = ",sensor.humidity())
   
def showSensorData_forever():
    while True:
        showSensorData()
        time.sleep_ms(1000)
    
