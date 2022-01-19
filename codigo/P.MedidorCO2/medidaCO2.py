import esp8266_i2c_lcd
import machine
import dht
import time
import ccs811
import network

from umqttsimple import MQTTClient, MQTTException

v = '0.6.5'

# Inicializacion de componentes
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

lcd = esp8266_i2c_lcd.I2cLcd(i2c, 0x27,2,16)

lcd.putstr('Medidor CO2')

ccs= ccs811.CCS811(i2c)

dht22 = dht.DHT22(machine.Pin(14))



# Nombre de los feeds/topic

topic_user = b'javacasm'
topic_sub = topic_user + b'/feeds'
topic_subTemp = topic_sub + b'/Temp_CO2py'
topic_subHum = topic_sub + b'/Hum_CO2py'
topic_subCO2 = topic_sub + b'/CO2_CO2py'

def sub_CheckTopics(topic, msg):
    print((topic, msg))
"""    if topic == topic_subLed:     # Check for Led Topic
        if msg == b'On':
            print('Led:On')
"""

def connect_and_subscribe(client_id, mqtt_server, mqtt_port, mqtt_user, mqtt_passwd):
    client = MQTTClient(client_id, mqtt_server, port = mqtt_port, user = mqtt_user, password = mqtt_passwd)
    client.set_callback(sub_CheckTopics)
    try:
        client.connect()
        print(f'Connected to {mqtt_server} MQTT broker as {mqtt_user}' )
        return client
    except MQTTException as me: # https://www.vtscada.com/help/Content/D_Tags/D_MQTT_ErrMsg.htm
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

def initWifi(ssid,passwd):

    w = network.WLAN(network.STA_IF)
    if not w.active():
        w.active(True)
    if not w.isconnected():
        w.connect(ssid,passwd)

        while not w.isconnected() :
            time.sleep(1)
            print('.', end = '')
            
    msg = f'{w.ifconfig()}'
    return msg
mqtt_client = None
def test_forever(delay = 10):
    global mqtt_client
    while True:
        try:
            
            dht22.measure()

            tempDHT22 = dht22.temperature()

            humDHT22 = dht22.humidity()

            lcd.clear()
            
            sLCDMsg = f'T:{tempDHT22} H:{humDHT22}'
            sMsg = f'{tempDHT22} {humDHT22}'
            lcd.move_to(0,0)
            lcd.putstr(sLCDMsg)
            print(sMsg, end=' ')
            
            ccs.put_envdata(humDHT22, tempDHT22)

            if ccs.data_ready():
                eCO2 = ccs.eCO2
                sLCDMsg = f'eC02:{eCO2}'
                sMsg = f'{eCO2}'
                lcd.move_to(0,1)
                lcd.putstr(sLCDMsg)
                print(sMsg)
            else:
                print()
                
            if mqtt_client != None:
                mqtt_client.publish(topic_subTemp, f'{tempDHT22}')
                mqtt_client.publish(topic_subHum, f'{humDHT22}')
                mqtt_client.publish(topic_subCO2, f'{eCO2}')
        except Exception as e:
            lcd.clear()
            lcd.putstr(str(e))
            print(e)
            time.sleep(2)
            
        time.sleep(delay)

