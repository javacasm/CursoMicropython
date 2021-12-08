# MQTT test 
# basado en https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/



from umqttsimple import MQTTClient, MQTTException
import ubinascii
import machine
import time         # Para las esperas
import utime
import test_DHT22

import MyDateTime

v = '0.5.4'

client_id = ubinascii.hexlify(machine.unique_id())

topic_sub = b'javacasm/feeds'
topic_subSensor = topic_sub + b'/DHT22_1'
topic_subTemp = topic_subSensor + b'_Temp'
topic_subHum = topic_subSensor + b'_Hum'

mqtt_server = 'io.adafruit.com'
mqtt_port =  1883
mqtt_user = 'javacasm'
mqtt_password = 'aio_hvvc26NtGcmt3LcujvhJ0d5BfPcl'

def sub_CheckTopics(topic, msg):
    print((topic, msg))
"""    if topic == topic_subLed:     # Check for Led Topic
        if msg == b'On':
            print('Led:On')
"""

def connect_and_subscribe():
    global client, client_id, mqtt_server
    client = MQTTClient(client_id, mqtt_server, port = mqtt_port, user = mqtt_user, password = mqtt_password)
    client.set_callback(sub_CheckTopics)
    try:
        client.connect()
        # client.subscribe(topic_subFree)
        print(f'Connected to {mqtt_server} MQTT broker as {mqtt_user}' )
        return client
    except MQTTException as me:
        value = f'{me}'
        if value == '5':
            print('Authorization error')
        elif value == '4':
            print('Login error')
        else:
            print(f'Connecting error: {me}')
        return None        
    except Exception as e:
        print(f'Connecting error: {e}')
        return None

def restart_and_reconnect():
    print(f'Failed to connect to MQTT broker {mqtt_server}. Reconnecting...')
    time.sleep(10)
    machine.reset()

def mainMQTT(everySeconds = 30):
    connect_and_subscribe() # connect and get a client reference
    if client == None:
        restart_and_reconnect()
        
    last_Temp = 0 # utime.ticks_ms()
    while True :
        # client.check_msg() # Check por new messages and call the callBack function
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_Temp) > (everySeconds*1000):
            msgTime = MyDateTime.getLocalTimeHumanFormat()
            try:
                temp, hum = test_DHT22.getData()
                print(f'{msgTime} Hum:{hum} Temp:{temp}')
                try:
                    client.publish(topic_subTemp, f'{temp}')
                    client.publish(topic_subHum, f'{hum}')
                    test_DHT22.tick(0.1)
                    print(f'Published {topic_subTemp} & {topic_subHum}')
                    print(f'deepsleep({everySeconds*1000})')
                    machine.deepsleep(everySeconds*1000)
                except Exception as e:
                    print(f'{msgTime} Error publishing sensor data')
                    print(f'Error: {e} {type(e)}')
                    test_DHT22.doudoubleTick(0.1)                
            except Exception as e:
                print(f'{msgTime} Error getting sensor data')
                print(f'Error: {e} {type(e)}')
                test_DHT22.doudoubleTick(0.1)                
              
            last_Temp = now
        time.sleep_ms(100)
