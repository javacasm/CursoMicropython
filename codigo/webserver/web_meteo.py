import dht
import machine
import utime
import socket
import network

v = 0.6

dht22 = dht.DHT22(machine.Pin(27)) # inicializamos el sensor dHT22


def getData():
    dht22.measure()  # Leemos el sensor
    tempDHT22 = dht22.temperature()
    humDHT22 = dht22.humidity()
    sFecha='{3:02}:{4:02}:{5:02} {2:02}/{1:02}/{0}'.format(*utime.localtime())
    return sFecha,tempDHT22,humDHT22

def start_webServer(puerto = 80):
    w = network.WLAN(network.STA_IF)
    if w.isconnected():
        print(f'Connect to http://{w.ifconfig()[0]}:{puerto}')


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos un socket para escuchar
    s.bind(('', puerto)) # enganchado al puerto 
    s.listen(5) # nos podemos a escuchar

    while True:
        conn, addr = s.accept() # Se bloque hasta que llega una conexión
        print(f'Cliente con IP {addr}')
        request = conn.recv(1024)
        # print(f'Petición: {request}')    
        sFecha,tempDHT22,humDHT22 = getData() 
        html = f'''<html>
                    <head>
                    <Title>Meteo data at {sFecha}</Title>
                    <meta http-equiv="refresh" content="5" >
                    </head>
                    <body>
                    <h4>Datos de las {sFecha}</h4>
                    <p>Temperatura: {tempDHT22} C</p>
                    <p>Humedad: {humDHT22} %</p>
                    </body>
                    </html>'''
        print(f'Temperatura:{tempDHT22} C Humedad:{humDHT22} {sFecha}')
        conn.send(html)
        conn.close()
