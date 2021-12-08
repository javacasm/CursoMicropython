# Fichero de configuracion

v = '0.4'

SSID = 'NOMBRE_WIFI'
PASSWD_WIFI = 'CLAVE_WIFI'

mqtt_server = 'io.adafruit.com'
mqtt_port =  1883
mqtt_user = 'javacasm'
mqtt_password = 'aio_CLAVE_ADAFRUIT_IO'

BOARD = 'Wemos Battery'

LED_INVERTED = True
pin_led_builtIn = 16
'''
16 para wemos battery
2 para wemos R32 D1
'''

print(f'Using config for board: {BOARD}')
