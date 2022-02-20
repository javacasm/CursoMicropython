# test ADC en esp8266, usando un nodeMCU

import machine
import time

v= 0.2

a0=machine.ADC(0)

while True:
    print(a0.read(),end=' \r')
    time.sleep_ms(200)