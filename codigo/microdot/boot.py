# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

from network import WLAN,STA_IF
from time import sleep

v = '0.2'

w=WLAN(STA_IF)
if w.active() == False:
    w.active(True)
if not w.isconnected():
    w.connect('OpenWrt','qazxcvbgtrewsdf')
    while not w.isconnected():
        print('.',end='')
        sleep(1)
print(f'IP: {w.ifconfig()[0]}')

#import webrepl
#webrepl.start()
