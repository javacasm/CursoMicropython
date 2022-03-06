import machine
import ubinascii
import medidaCO2

v = '0.4.2'

mqtt_client = None

def connnectMQTT(p):
    global mqtt_client
    if mqtt_client == None:
        msg = medidaCO2.initWifi('WIFI_SSID','WIFI_PASSWD')
        print(f'IP:{msg}')

        client_id = ubinascii.hexlify(machine.unique_id())

        mqtt_server = 'io.adafruit.com'
        mqtt_port =  1883

        print(f'Conectando a {mqtt_server}@{mqtt_port}')
        mqtt_client = medidaCO2.connect_and_subscribe(client_id, mqtt_server, mqtt_port, 'IO_USER','aio_ADAFRUIT_KEY')
    else:
        print('Connected yet')
        

medidaCO2.test_forever(delay = 30)