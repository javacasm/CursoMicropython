import telemetria
import config
import blinky
import test_rele
import test_DHT22
import test_hmc5883l

def sendData(server = config.telemetry_server, port = config.telemetry_port):
    global paquetes, errores
    data = {}
    try:
        temp,hum = test_DHT22.getData()
        data['temp'] = temp
        data['hum'] = hum
    except Exception as exDHT22:
        print(f'Error getting DHT22 data {exDHT22}')
        
    try:    
        x,y,z,heading_gr,heading_min = test_hmc5883l.read_compas()
        data['heading'] = heading_gr
    except Exception as exCompass:
        print(f'Error getting compass data {exCompass}')

    data['v'] = v
    data[f'rele{config.pinRele}'] = f"{'On' if test_rele.rele.value()>0 else 'Off'}"
    timestamp = MyDateTime.getLocalTimeHumanFormat()    
    data['time'] = timestamp
    data['board'] = MY_ID
    data['count'] = paquetes
    data['errors'] = errores
    sendDict(data,server,port)

def test_forever(espera=5):
    while True:
         sendData()
         blinky.tick(0.1)
         time.sleep(espera)

        