# basado en 
#   https://www.dfrobot.com/blog-608.html 
#   https://pymotw.com/2/socket/udp.html

import socket
import time
import json

v = '0.4.5'

verbose = True

def debug(msg):
    if verbose : print(msg)

def listen(port=10086, ip = '192.168.1.136'):
    print(f'Listening {ip}@{port}')
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((ip,port))
    print('waiting....')
    while True:
        data,addr=s.recvfrom(1024)
        dataDict = json.loads(data)
        strAnswer = 'OK'
        if 'board' in dataDict.keys():
             print(f"Data from {dataDict['board']} ")
        if 'heading' in dataDict.keys():
             if dataDict['heading']  < 100:
                 strAnswer = 'CMD:Rele=Off'
             else:
                 strAnswer = 'CMD:Rele=On'
        answer = strAnswer.encode()
        s.sendto(answer,addr)
        debug(f'got:"{data.decode()}" ({len(data)}) from {addr}. Sent {strAnswer}')

if __name__ == '__main__':
    listen()