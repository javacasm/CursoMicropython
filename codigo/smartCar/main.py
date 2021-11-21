import network
w = network.WLAN(network.STA_IF)
if w.isconnected():
    w.ifconfig()
else:
    w.active(True)
    w.connect('MiWifi','MiClave')


