# Fichero boot.py 
v = 0.3

# Conectamos al wifi
import time
import network
wl = network.WLAN(network.STA_IF)
wl.active(True)
if not wl.isconnected():
    wl.connect('OpenWrt','qazxcvbgtrewsdf')
    while not wl.isconnected():
        print('.',end='')
        time.sleep(1)
    
print(f'IP: {wl.ifconfig()[0]}')

# Actualizamos la fecha

import ntptime
import utime
try:
    ntptime.settime()
    sFecha='{3:02}:{4:02}:{5:02} {2:02}/{1:02}/{0}'.format(*utime.localtime())
    print(sFecha)
except Exception as e:
    print(f'Error: {e}')
# Arrancamos webrepl
import webrepl
webrepl.start()
