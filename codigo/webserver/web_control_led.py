import socket
import machine
import network

v = 0.4

led = machine.Pin(19,machine.Pin.OUT)


def start_webServer(puerto = 80):
    w = network.WLAN(network.STA_IF)
    if w.isconnected():
        print(f'Connect to http://{w.ifconfig()[0]}:{puerto}')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos un socket para escuchar
    s.bind(('', puerto)) # conectado al puerto
    s.listen(5) # nos podemos a escuchar

    while True:
        conn, addr = s.accept() # Se bloque hasta que llega una conexión
        print(f'Cliente con IP {addr}')
        request = conn.recv(1024)
        strRequest = str(request)  # convertimos a cadena
        # print(f'Petición: {strRequest}')
        if strRequest.find("/led_on") > 0: # Piden encender el led?
            led.on()
            print('LED ON!')
        if strRequest.find("/led_off") > 0: # Piden apagar el led?
            led.off()
            print('LED OFF!')
        if led.value() == 1:
            led_status = 'On'
        else:
            led_status = 'Off'
        html = f'''<html>
              <head>Control del led</head>
              <body>
              <h3>Control del led</h3>
              <p>Led {led_status}</p>
              <h3>Pulsa el enlace para enceder o apagar el led</h3>
              <p><a href="/led_on" >Encender LED</a></p>
              <p><a href="/led_off" >Apagar LED</a></p>
              </body>
              </html>'''
        # print(html)     
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(html)
        conn.close()
