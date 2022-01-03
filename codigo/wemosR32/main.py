# main mqtt

v = '0.6.2'

import machine
import time

import config
import MQTT_test
import test_wifi
# import test_lcd
# import test_DHT22


if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

infoWifi = test_wifi.initWifi(config.SSID,config.PASSWD_WIFI)
msgWifi=f'ip: {infoWifi[0]}'
print(msgWifi)
# test_lcd.showLcd(msgWifi)



# MQTT_test.mainMQTT()

# test_lcd.test_forever()

# import testI2C
# testI2C.scan_I2C()

# import test_gy91