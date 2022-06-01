# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)


import network
import time
import config
import machine
import ntptime

v = 0.6

try:
    w = network.WLAN(network.STA_IF)
    if not w.active():
        w.active(True)
    if not w.isconnected():
        print(config.SSID, config.WIFI_PASSWD)
        w.connect(config.SSID, config.WIFI_PASSWD)

        while not w.isconnected() :
            time.sleep(1)
            print('.', end = '')
        
    print(f'IP: {w.ifconfig()[0]}')
    
    ntptime.settime()
    rtc = machine.RTC()
    print(rtc.datetime() )
except Exception as e:
    print(f'Error {e}. \nReset in 10 seconds')
    time.sleep(10)
    machine.reset()

#import webrepl
#webrepl.start()
