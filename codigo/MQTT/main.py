# main mqtt

v = '0.3'

import machine
import test_DHT22
import MQTT_test
import test_wifi

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

test_wifi.test_wifi()

MQTT_test.mainMQTT()