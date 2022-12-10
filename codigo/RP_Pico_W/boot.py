from network import WLAN,STA_IF
from time import sleep

wl = WLAN(STA_IF)

if wl.active() == False:
    wl.active(True)
    
if wl.isconnected() == False:
    wl.connect('OpenWrt','qazxcvbgtrewsdf')
    
while wl.isconnected() == False:
    print('.', end='')
    sleep(1)

print(f'IP: {wl.ifconfig()[0]}')
