import network
w = network.WLAN(network.STA_IF)
if not w.isconnected():
    w.active(True)
    w.connect('OpenWrt','qazxcvbgtrewsdf')
w.ifconfig()