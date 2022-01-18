import machine
import ubinascii
import medidaCO2

v = '0.4'

msg = medidaCO2.initWifi('RED_WIFI','CLAVE_WIFI')
print(f'IP:{msg}')

client_id = ubinascii.hexlify(machine.unique_id())

mqtt_server = 'io.adafruit.com'
mqtt_port =  1883

print(f'Conectando a {mqtt_server}@{mqtt_port}')
clientMQTT = medidaCO2.connect_and_subscribe(client_id, mqtt_server, mqtt_port, 'USUARIO_ADAFRUIT','KEY_ADAFRUIT')



medidaCO2.test_forever(clientMQTT)