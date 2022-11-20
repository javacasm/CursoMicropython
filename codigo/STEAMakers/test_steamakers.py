# test of steamakers board

pin_led = 17
pin_rele = 12
pin_dht = 14
pin_humedad = 4
pin_vOUT = 39
pin_iOUT = 36

v = '0.7.7'

print(f'test_steamakers {v}')

def test_led(pin_led = 17):
    from machine import Pin
    led=Pin(pin_led,Pin.OUT)
    led.on()
    led.off()

def test_rele(pin_rele = 12):
    rele = Pin(pin_rele,Pin.OUT)
    rele.off()
    rele.on()


def test_dht22(pin_dht = 14):
    ## embrion de estacion meteorlogica
    from dht import DHT22  # importamos el DHT22 del modulo DHT
    sensorDHT = DHT22(Pin(pin_dht))  
    from time import sleep
    while True:
        sensorDHT.measure()  # medimos
        print(sensorDHT.temperature(), sensorDHT.humidity())
        sleep(2)

def test_control_humedad_rele():
    ## control de humedad con el rele
    while True:
        sensorHT.measure()
        print(sensorHT.temperature(),sensorHT.humidity())
        if sensorHT.humidity()>50:
            rele.on()
        else:
            rele.off()
        sleep(2)

from machine import ADC
from time import sleep
    
## Sensores analogicos
def test_ADC(pin_humedad = 4):


    sensorHumedadSuelo = ADC(Pin(pin_humedad))
    while True:
        print(sensorHumedadSuelo.read())
        sleep(1)

## Stroboscopio
def test_stroboscopio(tiempo_espera = 50):
    while True:
        led.on()
        sleep_ms(tiempo_espera)
        led.off()
        sleep_ms(tiempo_espera)
        count+=1
        if count%1000 == 0:
            print(count,end='\r')

def test_riego(umbral=500):
    ## Proto sistema de riego
        
    while True:
        if sensorHumedadSuelo.read()<umbral:
            rele.on()
            led.on()
        else:
            rele.off()
            led.off()

def promedioADC(adc, N=100):
    media = 0
    for i in range(N):
        media += adc.read()
    media = media / N
    return int(media)
    

# medida de consumo
def test_consumo(tiempo_espera = 200):
    vOut = ADC(Pin(36),atten=ADC.ATTN_11DB)
    iOut = ADC(Pin(39),atten=ADC.ATTN_11DB)    
    contador=0
    led = Pin(17,Pin.OUT)
    sensV = 0.185
    while True:
        v = promedioADC(vOut) 
        i = v - promedioADC(iOut)
        print(f' {v//10} v {i} {int(i*sensV)} ma  ',end='\r')
        sleep_ms(tiempo_espera)
        if contador % 50 == 0:
            led.on()
        if contador % 50 == 25:
            led.off()
        contador += 1
        

from machine import Pin,PWM
from time import sleep_ms

led = None
ledPWM = None

def test_contro_brillo():
## PWM control de brillo
    global led, ledPWM    
    if ledPWM == None:
        ledPWM = PWM(led,freq=1000) # enlazamos un controlador de brillo sobre nuestro led

    ledPWM.duty(500) # medio gas

    ledPWM.duty(100)

    ledPWM.duty(10)
    ledPWM.duty(1) # iluminacion minima
    ledPWM.duty(0) # apagado
    ledPWM.duty(1023) # iluminacion maxima



def fadeOut(tiempo_espera = 10):
    global led, ledPWM
    if led == None:
        led=Pin(pin_led,Pin.OUT)
        ledPWM = PWM(led,freq=1000) # enlazamos un controlador de brillo sobre nuestro led    
    for brillo in range(1023,0,-16):
        ledPWM.duty(brillo)
        sleep_ms(tiempo_espera)
    ledPWM.duty(0)


def fadeIn(pin_led=17, tiempo_espera = 10):
    global led, ledPWM
    if led == None:
        led=Pin(pin_led,Pin.OUT)
        ledPWM = PWM(led,freq=1000) # enlazamos un controlador de brillo sobre nuestro led    
    for brillo in range(0,1024,16):
        ledPWM.duty(brillo)
        sleep_ms(tiempo_espera)
    ledPWM.duty(1023) # para asegurar que esta al maximo

def test_network():
    from network import WLAN,STA_IF
    wl = WLAN(STA_IF) # conexion a una red wifi existent

    if not wl.active():
       wl.active(True)

    if not wl.isconnected():
        wl.connect('OpenWrt','qazxcvbgtrewsdf')
    while not wl.isconnected():
        sleep_ms(500)
        print('.',end='')
        
    print(f'IP: {wl.ifconfig()[0]}')
    # tras conectar activamos webrepl en boot.py