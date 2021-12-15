# Fichero de configuracion

v = '0.6.1'

SSID = 'OpenWrt'
PASSWD_WIFI = 'qazxcvbgtrewsdf'

mqtt_server = 'io.adafruit.com'
mqtt_port =  1883
mqtt_user = 'javacasm'
mqtt_password = 'aio_CLAVE_ADAFRUIT_IO'

BOARD = 'Lolin32 Lite'

LED_INVERTED = True
pin_led_builtIn = 22

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
