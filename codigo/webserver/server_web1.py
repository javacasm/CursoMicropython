import socket
import network


v = 0.2


html = """<html>
          <head>Primera pagina web</head>
          <body>
          <h1>Hello, Web!</h1>
          <p>Algo de contenido.... desde el ESP32</p>
          </body>
          </html>"""

w = network.WLAN(STA_IF)
if w.isconnected():
    print(f'Connect to http://{w.ifconfig()[0]}:80')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos un socket para escuchar
s.bind(('', 80)) # conectado al puerto 80
s.listen(5) # nos podemos a escuchar

while True:
  conn, addr = s.accept() # Se bloque hasta que llega una conexión
  print(f'Cliente con IP {addr}')
  request = conn.recv(1024)
  print(f'Petición: {request}')
  conn.send(html)
  conn.close()