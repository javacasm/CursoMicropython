# basado en 
#   https://www.dfrobot.com/blog-608.html 
#   https://pymotw.com/2/socket/udp.html

#import network
import socket
import time
port=10086
#wlan = network.WLAN(network.STA_IF)
#wlan.active(True)
#wlan.connect('dfyanfa', 'df123456')
#while(wlan.isconnected() == False):
#  time.sleep(1)
ip = '192.168.1.76' #ip = wlan.ifconfig()[0]
print(f'Listening {ip}@{port}')
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
s.bind((ip,port))
print('waiting....')
while True:
  data,addr=s.recvfrom(1024)
  s.sendto(data,addr)
  print('received:',data,'from',addr)
