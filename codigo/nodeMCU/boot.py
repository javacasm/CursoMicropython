# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import network
import time

wl = network.WLAN(network.STA_IF)

wl.active(True)

wl.connect('OpenWrt','qazxcvbgtrewsdf')

while not wl.isconnected():
    print('.', end='')
    time.sleep(1)

print(f'IP: {wl.ifconfig()[0]}')

import webrepl
webrepl.start()
