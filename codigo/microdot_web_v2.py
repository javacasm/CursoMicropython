from microdot import Microdot,send_file
from machine import Pin, PWM, SoftI2C, ADC, reset
from time import sleep
from ssd1306 import SSD1306_I2C

import config

v = '0.9'

print(f'v:{v}')

OLED_RESET = 16

OLED_SCL = config.SCL
OLED_SDA = config.SDA

OLED_ADDRESS = 0x3c

OLED_WITDH = 128
OLED_HEIGHT = 64


WEB_PORT = 80

app = Microdot()   

@app.before_request
def before_request_(request):
    print(f'{request.path}')
# if not user:
#        return 'Unauthorized', 401
#    request.g.user = user    


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
    return response, {'Content-Type': 'text/html'}

@app.route('/free')
def index(request):
    import gc
    mem_before = gc.mem_free()
    gc.collect()
    response = f'<h1>free mem before: {mem_before} now:{gc.mem_free()}</h1>'
    return response, {'Content-Type': 'text/html'}

i2c = None
oled_rst = None
oled = None

def init_oled():
    global i2c, oled_rst, oled
    
    if i2c == None:
        i2c = SoftI2C(scl=Pin(OLED_SCL),sda=Pin(OLED_SDA))
        
    if oled_rst == None:
        oled_rst = Pin(OLED_RESET,Pin.OUT)

    oled_rst.on()
    
    if oled == None:
        oled = SSD1306_I2C(OLED_WITDH,OLED_HEIGHT,i2c,addr=OLED_ADDRESS)
        oled.clear()
    
@app.route('/oledclear')
def oledclear(request):
    init_oled()
    
    sMsg = 'oled.clear'
    oled.clear()
    print(sMsg)
    return sMsg
        
@app.route('/oled/<x>/<y>/<text>')
def oled_text(request,x,y,text):

    init_oled()

    oled.text(text,int(x),int(y))
    sMsg = f'oled: "{text}"@({x},{y})'
    oled.show()
    print(sMsg)
    return sMsg
    
@app.route('/servo/<servo_id>/<value>')
def servo(request,servo_id,value):
    try:
        id_Pin = int(servo_id)
        iValue = int(value)

        pinServo = Pin(id_Pin)
        servo = PWM(pinServo,freq = 50)
        servo.duty(iValue)
        sMsg = f'servo({id_Pin}) {iValue} '
        print(sMsg)
        return sMsg
        
    except Exception as e:
        print(f'error: {e}')

    
@app.route('/adc/<pin_id>')
def adc(request,pin_id):
    try:
        id_Pin = int(pin_id)

        pin = Pin(id_Pin)
        adc = ADC(pin)
        sMsg = f'adc({id_Pin}) {adc.read_u16()} '
        print(sMsg)
        return sMsg
        
    except Exception as e:
        print(f'error: {e}')    

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

@app.route('/pwm/<pin_id>/<value>')
def pwm(request,pin_id,value):
    try:
        id_Pin = int(pin_id)
        iValue = int(value)

        pin = Pin(id_Pin)
        pinPWM = PWM(pin,freq=5000)
        pinPWM.duty(iValue)
        sMsg = f'PWM({id_Pin}) {iValue} '
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

@app.get('/reset')
def reset(request):
    reset()
    return 'reset...'


@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'


def init_web():
    global oled
    from network import WLAN,STA_IF
    w=WLAN(STA_IF)
    if w.active() == False:
        w.active(True)
    init_oled()    
    if w.isconnected():
        sWeb = f'{w.ifconfig()[0]}:{WEB_PORT}'
        print('http://' + sWeb + f'\n/ - mem - free - test  - shutdown - reset\nled/<pin>/<state>\npwm/<pin>/<value>\nservo/<servo_id>/<value>\nadc/<pin> \nstatic/<file> - \noled/<x>/<y>/<text> - oledclear')
        oled.text('..'+sWeb[7:],0,0)
        oled.show()
        app.run(port=WEB_PORT)
    else:
        print('no network available')
