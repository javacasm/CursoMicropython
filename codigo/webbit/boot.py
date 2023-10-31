# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import network
import time

v = 0.5

print(f'boot webbit {v}')

sta_if = network.WLAN(network.STA_IF)
if sta_if.active == False:
    sta_if.active(True)
# print(sta_if.scan()) # Scan for available access points

if not sta_if.isconnected():
    sta_if.connect("Digifibra_4BB8_EXT", "wbbmZZCM3qejbx") # Connect to an AP
    while sta_if.isconnected():
        print('.',end='')
        time.sleep_ms(500)
print(f'IP: {sta_if.ifconfig()[0]}')

#import webrepl
#webrepl.start()
