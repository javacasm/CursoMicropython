import umqttsimple
import ubinascii
import machine
import time

v = 0.4

client_id = ubinascii.hexlify(machine.unique_id())

topic_Temp = b'/salon/DHT22_TEMP'
topic_Hum = b'/salon/DHT22_HUM'
topic_errors = b'/errors'

def sub_CheckTopics(topic, msg):
    print(f'Topic:{topic} msg:{msg}')
"""    if topic == topic_subLed:     # Check for Led Topic
        if msg == b'On':
            print('Led:On')
"""

client = umqttsimple.MQTTClient(client_id, 'raspi4', port = 1883)
client.set_callback(sub_CheckTopics)
try:
    client.connect()
    print(f'Suscrito a {topic_errors}')
    client.subscribe(topic_errors)
except umqttsimple.MQTTException as me: # https://www.vtscada.com/help/Content/D_Tags/D_MQTT_ErrMsg.htm
    value = f'{me}'
    if value == '5':
        print('Error de autorizacion')
    elif value == '4':
        print('Login error')
    else:
        print(f'Error conectando: {me}')
    time.sleep(10)
    machine.reset()
except Exception as e:
    print(f'Error conectando (ex): {e}')
    time.sleep(10)
    machine.reset()

try:
    client.check_msg() # comprobamos si hay mensajes para nosotros
    temp = '18.5 C'
    hum = '50%'
    client.publish(topic_Temp, f'{temp}')
    client.publish(topic_Hum, f'{hum}')
    print( f'Publicado {topic_Temp} / {temp}')
    print( f'Publicado {topic_Hum} / {hum}')
except Exception as e:
    print(f'Error publicando: {e}')
    time.sleep(10)
    machine.reset()  
