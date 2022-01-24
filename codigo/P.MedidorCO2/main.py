import machine
import ubinascii
import medidaCO2

v = '0.4.2'

mqtt_client = None

def connnectMQTT(p):
    global mqtt_client
    if mqtt_client == None:
        msg = medidaCO2.initWifi('OpenWrt','qazxcvbgtrewsdf')
        print(f'IP:{msg}')

        client_id = ubinascii.hexlify(machine.unique_id())

        mqtt_server = 'io.adafruit.com'
        mqtt_port =  1883

        print(f'Conectando a {mqtt_server}@{mqtt_port}')
        mqtt_client = medidaCO2.connect_and_subscribe(client_id, mqtt_server, mqtt_port, 'javacasm','aio_jCLm54QfTsjzr4s2ccoNoUokwyPt')
    else:
        print('Connected yet')
        
def pulsado(p):
    print('Pulsado')

# button = machine.Pin(23, machine.Pin.IN, machine.Pin.PULL_UP)

# button.irq(trigger = machine.Pin.IRQ_FALLING, handler = connnectMQTT)

medidaCO2.test_forever(delay = 3)