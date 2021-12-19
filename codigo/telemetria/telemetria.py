import socket
import time
import json
import config
import test_DHT22
import test_hmc5883l
import MyDateTime
import blinky
import test_rele

test_rele.Verbose = False


v = '0.6.6'

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
    message = json.dumps(diccio)
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
        elif strData.startswith('CMD'):
            cmd = strData[4:]
            if cmd.startswith('Rele=On') :
                test_rele.releOn()
            elif cmd.startswith('Rele=Off') :
                test_rele.releOff()
            else:
                print(f'Got command: {cmd}')
            
            resultado =  True
        else:
            errores += 1
            print('Error de comunicaciones')
            resultado =  False

            
        print(f'Paquetes: {paquetes} Errores: {errores}',end ='\r')
    except OSError as oex: # por ejemplo: timeout https://docs.micropython.org/en/latest/library/socket.html
        print(f'{oex} errores: {errores}')
        errores += 1
        resultado = False       
    except Exception as ex:
        print(f'{ex} errores: {errores}')
        errores += 1
        resultado = False
    finally:
        debug('closing udp socket')
        sock.close()
    return resultado

def sendData(server = config.telemetry_server, port = config.telemetry_port):
    global paquetes, errores
    data = {}
    temp,hum = test_DHT22.getData()
    x,y,z,heading_gr,heading_min = test_hmc5883l.read_compas()
    data['v'] = v
    data['temp'] = temp
    data['hum'] = hum
    timestamp = MyDateTime.getLocalTimeHumanFormat()    
    data['time'] = timestamp
    data['board'] = MY_ID
    data['heading'] = heading_gr
    data[f'rele{config.pinRele}'] = f"{'On' if test_rele.rele.value()>0 else 'Off'}"
    data['count'] = paquetes
    data['errors'] = errores
    sendDict(data,server,port)

def test_forever(espera=5):
    while True:
         sendData()
         blinky.tick(0.1)
         time.sleep(espera)

        