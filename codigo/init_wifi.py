import network
import time
import machine

SSID = 'miWifi'
WIFI_PASSWD = 'miPassword'

try:
    w = network.WLAN(network.STA_IF)
    if not w.active():  # Si no está activa la activamos
        w.active(True)
    if not w.isconnected(): # si no está conectada nos conectamos
        print(f'wifi:{SSID} passwd: {WIFI_PASSWD}')
        w.connect(SSID, WIFI_PASSWD)

        while not w.isconnected() : # mientras conecta ...
            time.sleep(1)
            print('.', end = '')    # imprimimos "." en la consola
        
    print(f'IP: {w.ifconfig()[0]}')
    

except Exception as e:
    print(f'Error {e}')
