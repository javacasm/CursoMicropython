# basado en 
#   https://www.dfrobot.com/blog-608.html 
#   https://pymotw.com/2/socket/udp.html

import socket
import time


v = '0.3.1'

verbose = True

def debug(msg):
    if verbose : print(msg)

def listen(port=10086, ip = '192.168.1.76'):
    print(f'Listening {ip}@{port}')
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
    s.bind((ip,port))
    print('waiting....')
    while True:
        data,addr=s.recvfrom(1024)
        strAnswer = 'OK'
        answer = strAnswer.encode()
        s.sendto(answer,addr)
        debug(f'got:"{data.decode()}" ({len(data)}) from {addr}. Sent {strAnswer}')

if __name__ == '__main__':
    listen()