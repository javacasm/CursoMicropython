import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = '192.168.1.33'
port = 10086
server_address = (server, port)
message = 'This is the message.  It will be repeated.'

try:
    print(f'sending "{message}"')
    sent = sock.sendto(message.encode(), server_address)
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    strData=data.decode('UTF-8')
    print(f'received "{strData}"')
    if strData != message : print('Error de comunicaciones')
    else: print('Comunicaciones OK!!!')
except Exception as ex:
    print(ex)
finally:
    print('closing udp socket')
    sock.close()


