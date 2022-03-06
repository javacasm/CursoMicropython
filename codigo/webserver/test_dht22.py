import machine
import dht
import utime

v = 0.2

dht22 = dht.DHT22(machine.Pin(27)) # inicializamos el sensor dHT22

def getData():
    dht22.measure()  # Leemos el sensor
    tempDHT22 = dht22.temperature()
    humDHT22 = dht22.humidity()
    sFecha='{3:02}:{4:02}:{5:02} {2:02}/{1:02}/{0}'.format(*utime.localtime())
    return sFecha,tempDHT22,humDHT22

while True:
    try:
        sFecha,tempDHT22,humDHT22 = getData() 
        print(f'Temperatura:{tempDHT22} C Humedad:{humDHT22} {sFecha}')
        utime.sleep(5)
    except Exception as e:
        print(f'Error: {e}')
    
        