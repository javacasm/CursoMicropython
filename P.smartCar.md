# Proyecto: transplante de cerebro micropython a un smartCar

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

3. Prueba motores
