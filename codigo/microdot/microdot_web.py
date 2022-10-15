from microdot import Microdot, send_file
from machine import Pin

v = '0.7'

app = Microdot()

WEB_PORT = 80

@app.route('/')
def index(request):
    return 'Hello, HTML world!'

@app.route('/test')
def index(request):
    return 'Only a test'

@app.route('/mem')
def index(request):
    import gc
    response = f'<h1>free mem {gc.mem_free()}</h1>'
    return response, {'Content-Type': 'text/html'}, 200

@app.route('/free')
def index(request):
    import gc
    mem_before = gc.mem_free()
    gc.collect()
    response = f'<h1>free mem before: {mem_before} now:{gc.mem_free()}</h1>'
    return response, {'Content-Type': 'text/html'}, 200


@app.route('/led/<pin_id>/<state>')
def led_state(request,pin_id,state):
    try:
        id_Pin = int(pin_id)
        bState = int(state)

        pin = Pin(id_Pin,Pin.OUT)
        pin.value(bState)
        sMsg = f'Pin({id_Pin}) {bState} '
        print(sMsg)
        return sMsg
        
    except Exception as e:
        print(f'error: {e}')

@app.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('icons/' + path)


@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'

from network import WLAN,STA_IF
w=WLAN(STA_IF)
if w.active() == False:
    w.active(True)
if w.isconnected():
    print(f'http://{w.ifconfig()[0]} (mem - free - test - / - shutdown - led/<pin>/<state> - statec/<file>)')
    app.run(port=WEB_PORT)
else:
    print('no network available')
