# basado en 
#   https://www.dfrobot.com/blog-608.html 
#   https://pymotw.com/2/socket/udp.html

v= '0.4.2'

import socket
import time
import config
import test_wifi
import blinky



def listen(port=10086):
    ip_config = test_wifi.initWifi(config.SSID,config.PASSWD_WIFI)

    ip = ip_config[0]

    print(f'Listening {ip}@{port}')

    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
    s.bind((ip,port))
    print('waiting....')
    while True:
        data,addr=s.recvfrom(1024)
        blinky.ledOn()
        s.sendto(data,addr)
        print(f'got:"{data.decode()}" ({len(data)}) from {addr}')
        blinky.ledOff()
