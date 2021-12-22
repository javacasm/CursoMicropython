# main 

v = '0.6.5'

import machine
import time

import config
# import MQTT_test
import test_wifi
# import test_lcd
import test_DHT22
# import echoServer


if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

infoWifi = test_wifi.initWifi(config.SSID,config.PASSWD_WIFI)

msgWifi=f'ip: {infoWifi[0]}'
print(msgWifi)

# test_lcd.showLcd(msgWifi)

# redes = test_wifi.scan_wifi()

# MQTT_test.mainMQTT()

# test_lcd.test_forever()

# echoServer.listen()

# import testI2C
# testI2C.scan_I2C()

# import test_hmc5883l
# test_hmc5883l.test_forever()


import telemetria
telemetria.test_forever(espera = 0.1)
