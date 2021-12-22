# Proyecto: transplante de cerebro micropython a un smartCar

0. Test ESP32

Encendemos el led inteno (que duplicamos fuera para facilitar)

0. Control remoto

Configuración wifi

```python
>>> import network
>>> w = network.WLAN(network.STA_IF)
>>> w.active(True)
>>> w.connect('OpenWrt','qazxcvbgtrewsdf')
>>> w.isconnected()
True
>>> w.ifconfig()
('192.168.1.94', '255.255.255.0', '192.168.1.1', '192.168.1.1')
```

Configuración webREPL

```python
>>> import webrepl_setup
WebREPL daemon auto-start status: disabled

Would you like to (E)nable or (D)isable it running on boot?
(Empty line to quit)
> E
To enable WebREPL, you must set password for it
New password (4-9 chars): MyPassword
Confirm password: MyPassword
Changes will be activated after reboot
Would you like to reboot now? (y/n) 
y
```

Reseteamos la placa y  descargamos el cliente webRepl de https://github.com/micropython/webrepl y abrimos en nuestro navegador web la página **webrepl.html**

FOTO


Personalmente he cambiado en el fichero webrepl.html la ip que sale por defecto para use la de mi ESP32, cambiando la línea 49 que queda así:

```html
<input type="text" name="webrepl_url" id="url" value="ws://192.168.1.94:8266/" />
```

FOTO

También podemos configurar Thonny para conectarnos vía webRepl, instalando el pluggin "websockets" y estableciendo en el menú de intérprete el tipo de conexión webRepl

(PONER FOTOS)




1. Confguramos los pines [Definición](./codigo/smartCar/elegoCar.py)

```python
pinServo = 25 # D3

minServo = 45
centralServo = 80
maxServo = 115

enA = 16 # D5
in1 = 14 # D7
in2 = 12 # D8
in3 = 13 # D9
in4 = 23 # D11
enB = 27 # D6

maxSpeed = 1023
```

2. Prueba servo: [código y test](./codigo/smartCar/elegoCar.py)

```python
import machine

servoUS = machine.PWM(machine.Pin(pinServo), freq = 50)

def testServo():
    for pos in range (minServo,maxServo):
        servoUS.duty(pos)
        print(pos)
        time.sleep(0.02)
    for pos in range (maxServo,minServo,-1):
        servoUS.duty(pos)
        print(pos)
        time.sleep(0.02)        
    servoUS.duty(centralServo)
    time.sleep(0.5)
    print('centrado')

```

3. Prueba motores [Ejemplo y test](./codigo/smartCar/elegoCar.py)
```python
import machine
import time

maxSpeed = 1023

IN1 = machine.Pin(in1, machine.Pin.OUT)
IN2 = machine.Pin(in2, machine.Pin.OUT)
EN  = machine.PWM(machine.Pin(en), freq = 100)

IN1.on()
IN2.off()

for speed in range(0,maxspeed,100):
    EN.duty(speed)
    time.sleep(0.2)
```

3.1 Definimos clase [motor](./codigo/smartCar/motor.py)

```python
''' Motor class 1/2 de L298N
    Usamos 3 pines:
        En para controlar la velocidad
        In1 & In2 para controlar la direccion
'''
# from math import abs
import machine

v = '0.6'

class motor:
    def __init__(self, In1, In2, En):
        self._in1 = In1
        self._in2 = In2
        self._en  = En
        self._attached = False
        self._debug()
    
    def attach(self):
        if not self._attached :
            self.IN1 = machine.Pin(self._in1, machine.Pin.OUT)
            self.IN2 = machine.Pin(self._in2, machine.Pin.OUT)
            self.EN  = machine.PWM(machine.Pin(self._en), freq = 100)
            self._attached = True      
            self._debug()

    def _debug(self):
        print(f'{__name__} v:{v}')
        print(f'In1:{self._in1}\nIn2:{self._in2}\nEn:{self._en}\nAttached:{self._attached} ')

    def stop(self):
        self.attach()
        self.IN1.value(0)
        self.IN2.value(0)
        self.EN.duty(0)
        # print('STOP')

    def move(self, speed):
        self.attach()
        # velocidad entre -1023 y 1023
        # print('Speed: {speed}')
        if speed>0:
            self.IN1.value(1)
            self.IN2.value(0)
        elif speed < 0:
            self.IN1.value(0)
            self.IN2.value(1)
        else :
            self.stop()
        self.EN.duty(abs(speed))
```
4. Sensores siguelíneas [Definición](./codigo/smartCar/elegoCar.py)

```python
import machine
# sensor siguelineas

SL_L = 26 # D2
SL_C = 17 # D4
SL_R = 5  # D10

sensorSL_L = machine.Pin(SL_L, machine.Pin.IN)
sensorSL_C = machine.Pin(SL_C, machine.Pin.IN)
sensorSL_R = machine.Pin(SL_R, machine.Pin.IN)
```

Test básico:

```python
# sensor siguelineas

SL_L = 26 # D2
SL_C = 17 # D4
SL_R = 5  # D10

sensorSL_L = machine.Pin(SL_L, machine.Pin.IN)
sensorSL_C = machine.Pin(SL_C, machine.Pin.IN)
sensorSL_R = machine.Pin(SL_R, machine.Pin.IN)

def testSL():
    while True:
        print(f'{sensorSL_L.value()} - {sensorSL_C.value()} - {sensorSL_R.value()}')
        time.sleep(0.5)
```

4.2. No te caigas

4.3. SigueLíneas

![](https://pbs.twimg.com/media/FEt9PChWUAMfV_3?format=png)

Esquema cortesía de Antonio Gomez

5. Telemetría

5.2 Sensor meteo

6. Control remoto



n. Pantalla 16x8

