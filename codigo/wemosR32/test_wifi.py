import network
import time

import config

v='0.5.1'


def initWifi(ssid, passwd):

    w = network.WLAN(network.STA_IF)
    if not w.active():
        w.active(True)
    if not w.isconnected():
        w.connect(ssid, passwd)

        while not w.isconnected() :
            time.sleep(1)
            print('.', end = '')
            
    wifi_info = w.ifconfig()
    return wifi_info
    

def test_wifi():
    msg = initWifi(config.SSID,config.PASSWD_WIFI)
    print(msg)