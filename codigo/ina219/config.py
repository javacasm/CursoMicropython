# Fichero de configuracion

v = '0.5'

SSID = 'OpenWrt'
PASSWD_WIFI = 'qazxcvbgtrewsdf'

DEEP_SLEEP = True

mqtt_server = 'io.adafruit.com'
mqtt_port =  1883
mqtt_user = 'javacasm'
mqtt_password = 'aio_jXDO12ZCCbhnIvWhZifK0o7J43zh'

BOARD = 'ESP32 dev kit'

DHT22_PIN = 32

pinDHT = DHT22_PIN
pinDS = 33

thingSpeak_api_key = '6WTOP32JXRWJJBN0'

DEEP_SLEEP = True

everySeconds = 15

pinSCL = 26
pinSDA = 27

LED_INVERTED = True
pin_led_builtIn = 16

'''
16 para wemos battery
2 para wemos R32 D1
22 para Lolin32 Lite
'''

print(f'Using config for board: {BOARD}')

