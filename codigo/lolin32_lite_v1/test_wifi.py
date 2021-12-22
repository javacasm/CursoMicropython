import network
import time
import ubinascii # para procesas las mac
import config

v='0.6.2'

w = None

def initWifi(ssid,passwd):
    global w
    w = network.WLAN(network.STA_IF)
    if not w.active():
        w.active(True)
    if not w.isconnected():
        w.connect(ssid,passwd)

        while not w.isconnected() :
            time.sleep(1)
            print('.', end = '')
            
    wifi_info = w.ifconfig()
    return wifi_info
    

def test_wifi():
    msg = initWifi(config.SSID,config.PASSWD_WIFI)
    print(f'IP: {msg[0]}')
    
def scan_wifi():
    global w
    test_wifi()
    redes = w.scan()
    for red in redes:
        ssid = red[0].decode('UTF-8')
        mac = ubinascii.hexlify(red[1]).decode('UTF-8')
        dbs = red[3]
        quality = int(150 + 5*dbs/3)    # https://stackoverflow.com/questions/15797920/how-to-convert-wifi-signal-strength-from-quality-percent-to-rssi-dbm
        print(f'ssid: ({ssid}) mac: {mac} dbs: {dbs} quality: {quality}%')
    return redes
    