import config
import test_DTH22
import test_hmc5883l

v = '0.4'

MY_ID = config.BOARD

verbose = True

def debug(msg):
    if verbose : print(msg)

def sendDict(diccio,server,port):
    socket.setdefaulttimeout(1) # https://medium.com/pipedrive-engineering/socket-timeout-an-important-but-not-simple-issue-with-python-4bb3c58386b4
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (server, port)
    
    debug(f'Trying to connecto to {server} @ {port}')
    resultado = True
    message = str(diccio)
    try:
        debug(f'sending "{message}"')
        sent = sock.sendto(message.encode(), server_address)
        paquetes += 1
        debug('waiting to receive')
        data, server = sock.recvfrom(100)
        strData=data.decode('UTF-8')
        debug(f'received "{strData}"')
        if strData != 'OK' : 
            errores += 1
            print('Error de comunicaciones')
            resultado =  False
        else: 
            debug('Comunicaciones OK!!!')
    except socket.timeout: # https://stackoverflow.com/questions/11865685/handling-a-timeout-error-in-python-sockets
        errores += 1
        resultado = False         
    except Exception as ex:
        print(ex)
        errores += 1
        resultado = False
    finally:
        debug('closing udp socket')
        sock.close()
    return resultado

def sendData(server = '192.168.1.33', port = 10086):
    data = {}
    temp,hum = test_DTH22.getData()
    x,y,z,heading_gr,heading_min = hmc5883l.read_compas()
    data['temp'] = temp
    data['hum'] = hum
    timestamp = MyDateTime.getLocalTimeHumanFormat()    
    data['time'] = timestamp
    data['temp'] = MY_ID
    data['heading'] = heading_gr
    sendDict(data,server,port)

def test_forever(espera=5):
    while True:
         sendData()
         time.sleep(espera)

    