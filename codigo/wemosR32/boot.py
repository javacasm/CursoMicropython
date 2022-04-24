# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

centro = 'CEP de Priego-Montilla'
print('Placa de Pepe')
print('curso del ', centro)

import network
import time
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('SALON-ACTOS','CEPMONTILLA')
while not wifi.isconnected():
    print(". ", end = "")
    time.sleep(1)

print (wifi.ifconfig())