# Fichero de configuracion

v = '0.6.3'

SSID = 'OpenWrt' # 'jazzBajo' 
PASSWD_WIFI = 'qazxcvbgtrewsdf'

net_timeout = 2
telemetry_server = '192.168.1.136' # '192.168.1.76' # toshibaL4
telemetry_port = 10086

pin_servo = 22

mqtt_server = 'io.adafruit.com'
mqtt_port =  1883
mqtt_user = 'javacasm'
mqtt_password = 'aio_CLAVE_ADAFRUIT_IO'

BOARD = 'Lolin32 Lite'

LED_INVERTED = True
pin_led_builtIn = 22

pinRele = 17

pinTouch = 12
pinDHT22 = 14

pinSDA = 23
pinSCL = 19

# Usual i2c sda:21 scl:22

lcd_i2c_address = 0x27

'''
16 para Wemos battery
2 para Wemos R32 D1
22 para Lolin32 Lite
'''

print(f'Using config for board: {BOARD}')
