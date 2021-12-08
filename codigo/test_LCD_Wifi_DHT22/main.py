# main mqtt

v = '0.6.1'

import machine
import time

import config
import MQTT_test
import test_wifi
import test_lcd
import test_DHT22


if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

msgWifi = test_wifi.initWifi(config.SSID,config.PASSWD_WIFI)

print(msgWifi)
test_lcd.showLcd(msgWifi)
time.sleep(5)


# MQTT_test.mainMQTT()

test_lcd.test_forever()