from microdot import Microdot

v = '0.3'

# creamos el servidor web
app = Microdot()

WEB_PORT = 80

@app.route('/')
def index(request):
    sMsg = 'Hello, HTML world!'
    return sMsg

@app.route('/html')
def index_html(request)
    sMsg = '<H1>Hello, <b>HTML</b> world!</H1>'
    # contenido, tipo, resultado
    return sMsg, {'Content-Type': 'text/html'}, 200

## Comprobamos que el wifi esta activado y operativo
from network import WLAN,STA_IF
w=WLAN(STA_IF)
if w.isconnected():
    print(f'http://{w.ifconfig()[0]}')
    # arrancamos la web
    app.run(port = WEB_PORT)
else:
    print('no hay wifi disponible')        