import network
import time

v='0.4'


def initWifi(ssid,passwd):

    w = network.WLAN(network.STA_IF)
    if not w.active():
        w.active(True)
    if not w.isconnected():
        w.connect(ssid,passwd)

        while not w.isconnected() :
            time.sleep(1)
            print('.', end = '')
            
    print(w.ifconfig())


def test_wifi():
    initWifi('OpenWrt','qazxcvbgtrewsdf')