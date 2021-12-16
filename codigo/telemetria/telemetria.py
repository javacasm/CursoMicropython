import socket
import time

import config
import test_DHT22
import test_hmc5883l
import MyDateTime
import blinky
import test_rele

v = '0.5'

MY_ID = config.BOARD

verbose = False

def debug(msg):
    if verbose : print(msg)

paquetes = 0
errores = 0

def sendDict(diccio,server,port):
    global paquetes, errores
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(config.net_timeout) # https://docs.micropython.org/en/latest/library/socket.html
    server_address = (server, port)
    
    debug(f'Trying to connecto to {server} @ {port}')
    resultado = True
    message = str(diccio)
    try:
        debug(f'sending "{message}"')
        sent = sock.sendto(message.encode(), server_address)
        paquetes += 1
        debug('waiting to receive')
        data, server = sock.recvfrom(4096)
        strData=data.decode('UTF-8')
        debug(f'received "{strData}"')
        if strData.startswith('OK') :
            debug('Comunicaciones OK!!!')
            resultado =  True
        elif strData.startWith('CMD'):
            cmd = strData[3]
            print(f'Got command: {cmd}')
            resultado =  True
        else:
            errores += 1
            print('Error de comunicaciones')
            resultado =  False

            
        print(f'Paquetes: {paquetes} Errores: {errores}',end ='\r')
    except OSError as oex: # por ejemplo: timeout https://docs.micropython.org/en/latest/library/socket.html
        print(oex)
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

def sendData(server = config.telemetry_server, port = config.telemetry_port):
    global paquetes
    data = {}
    temp,hum = test_DHT22.getData()
    x,y,z,heading_gr,heading_min = test_hmc5883l.read_compas()
    data['v'] = v
    data['temp'] = temp
    data['hum'] = hum
    timestamp = MyDateTime.getLocalTimeHumanFormat()    
    data['time'] = timestamp
    data['temp'] = MY_ID
    data['heading'] = heading_gr
    data[f'rele{config.pinRele}'] = f"{'On' if test_rele.rele.value()>0 else 'Off'}" 
    sendDict(data,server,port)

def test_forever(espera=5):
    while True:
         sendData()
         blinky.tick(0.1)
         time.sleep(espera)

        