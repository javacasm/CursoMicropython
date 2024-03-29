import dht
import machine
import utime
import socket

v = 0.5

dht22 = dht.DHT22(machine.Pin(27)) # inicializamos el sensor dHT22

def getData():
    dht22.measure()  # Leemos el sensor
    tempDHT22 = dht22.temperature()
    humDHT22 = dht22.humidity()
    sFecha='{3:02}:{4:02}:{5:02} {2:02}/{1:02}/{0}'.format(*utime.localtime())
    return sFecha,tempDHT22,humDHT22

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos un socket para escuchar
s.bind(('', 80)) # conectado al puerto 80
s.listen(5) # nos podemos a escuchar

while True:
    conn, addr = s.accept() # Se bloque hasta que llega una conexión
    print(f'Cliente con IP {addr}')
    request = conn.recv(1024)
    print(f'Petición: {request}')    
    sFecha,tempDHT22,humDHT22 = getData()
    html = f'''<html><head>Meteo data</head>
                <body><h3>Datos de las {sFecha}</h3>
                <p>Temperatura: {tempDHT22} C</p>
                <p>Humedad: {humDHT22} %</p>
                </body></html>'''
    conn.send(html)
    conn.close()
