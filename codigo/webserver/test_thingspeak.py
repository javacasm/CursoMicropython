import machine
import dht
import utime
import urequests

api_key = 'NBGMD53XIKGDVX45'

v = 0.4

dht22 = dht.DHT22(machine.Pin(27)) # inicializamos el sensor dHT22

def getData():
    dht22.measure()  # Leemos el sensor
    tempDHT22 = dht22.temperature()
    humDHT22 = dht22.humidity()
    sFecha='{3:02}:{4:02}:{5:02} {2:02}/{1:02}/{0}'.format(*utime.localtime())
    return sFecha,tempDHT22,humDHT22

while True:
    try:
        sFecha, tempDHT22, humDHT22 = getData() 
        print(f'Temperatura:{tempDHT22} C Humedad:{humDHT22} {sFecha}')
        
        dict_datos = {'field1':tempDHT22, 'field2':humDHT22}
        
        request_headers = {'Content-Type': 'application/json'}

        request = urequests.post(
            'http://api.thingspeak.com/update?api_key=' + api_key,
            json = dict_datos,
            headers = request_headers)
        if request.text == '0':
            print('Error sendinng: ',reques.text)
        else:
            print(request.text)
        request.close()
        
        utime.sleep(30)
    except Exception as e:
        print(f'Error: {e}')
    
        

