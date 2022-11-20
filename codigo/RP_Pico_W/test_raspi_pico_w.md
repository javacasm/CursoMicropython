## Test de Raspi Pico W

### Instalación 

Instalamos el firmware de micropython uf2

### Acceso con Thonny

¿RP2040?

### Primeras pruebas

Led interno

```python
from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT) # WL_GPIO0 del chip Infineon 43439

tiempo = 0.5

while True:
    led.on()
    print('On')
    sleep(tiempo)
    led.off()
    print('Off')
    sleep(tiempo)
```

### ADCs


Test del sensor de temperatura interno

```python
from machine import ADC
from time import sleep

tempADC = ADC(4) # ADC interno

factorV = 3.3/65535 # conversion de valor adc a V


while True:
    temp = 27 - (tempADC.read_u16()*factorV - 0.706)/0.001721    
    print (f'Temp: {temp}',end='\r')
    sleep(0.5)

```

### Wifi


### Servidor web

Servidor web con microdot


Usamos led y leemos temperatura



## Placa Kitronik

Permite controlar 8 servos y 4 motores DC o 2 motores stepper

Internamente:

Usa un pca9685 y 2 controladores de motores 8833 

#### Servo

Control de servo

Robot mk3  

test_servos_mk3

#### Robot 4 servos

Robot con 4 servos continuo y


#### Control de motores

Robot con 4 motores

Robot con 4 motores y 4 servos