import network
import time

import config

v='0.5'


def initWifi(ssid,passwd):

    w = network.WLAN(network.STA_IF)
    if not w.active():
        w.active(True)
    if not w.isconnected():
        w.connect(ssid,passwd)

        while not w.isconnected() :
            time.sleep(1)
            print('.', end = '')
            
    msg = f'{w.ifconfig()}'
    return msg
    

def test_wifi():
    msg = initWifi(config.SSID,config.PASSWD_WIFI)
    print(msg)