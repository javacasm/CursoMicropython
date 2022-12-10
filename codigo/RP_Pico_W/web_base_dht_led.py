from microdot import Microdot, send_file
from machine import Pin

from dht import DHT22

v = '0.3'

app = Microdot()

WEB_PORT = 80

sensorDHT22 = DHT22(Pin(2))

@app.route('/')
def index(request):
    return 'Hello, HTML world!'

@app.route('/LED/<state>')
def led_state(request,state):
    try:
        bState = int(state)

        pin = Pin('LED',Pin.OUT)
        pin.value(bState)
        sMsg = f'LED {bState} '
        print(sMsg)
        return sMsg, {'Content-Type': 'text/html'},200

        
    except Exception as e:
        print(f'error: {e}')

@app.route('/sensor')
def sensor(request):
    sensorDHT22.measure()
    sMsg = f'T: {sensorDHT22.temperature()} H: {sensorDHT22.humidity()}'
    print(sMsg)
    return sMsg, {'Content-Type': 'text/html'},200
   
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


from network import WLAN,STA_IF
w=WLAN(STA_IF)
if w.isconnected():
    print(f'http://{w.ifconfig()[0]} (/ - LED/<state> - /sensor)')
    app.run(port=WEB_PORT)
else:
    print('no network available')        
