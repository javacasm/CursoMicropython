import socket

v= '0.3.5'

paquetes = 0
errores = 0
verbose = False

def debug(msg):
    if verbose : print(msg)

def testUDP(server = '192.168.1.33', port = 10086,message = 'Hola caracola'):
    global paquetes, errores
    socket.setdefaulttimeout(1) # https://medium.com/pipedrive-engineering/socket-timeout-an-important-but-not-simple-issue-with-python-4bb3c58386b4
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (server, port)
    
    debug(f'Trying to connecto to {server} @ {port}')

    try:
        debug(f'sending "{message}"')
        sent = sock.sendto(message.encode(), server_address)
        paquetes += 1
        debug('waiting to receive')
        data, server = sock.recvfrom(4096)
        strData=data.decode('UTF-8')
        debug(f'received "{strData}"')
        if strData != message : 
            errores += 1
            print('Error de comunicaciones')
        else: debug('Comunicaciones OK!!!')
    except Exception as ex:
        print(ex)
    finally:
        debug('closing udp socket')
        sock.close()

def intesiveTest(N=1000,server = '192.168.1.33', port = 10086,message = 'Hola caracola'):
    for i in range(N):
        testUDP(server=server, port=port, message = f'hola caracola {i}')
        if not verbose and i % 500 == 0: print(f'Paquetes: {paquetes} Errores: {errores}',end ='\r')
    print(f'Paquetes: {paquetes} Errores: {errores}')