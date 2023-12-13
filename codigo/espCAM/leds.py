# trabajando con varios leds
import machine
import utime

v = 0.5

# pin_leds = (26, 25, 17, 16, 27, 14, 12, 13) # ESP32 DEV Kit
pin_leds = (2,14,15,13,12,0,4) # ESPCAM CUIDADO CON EL GPIO 0

leds = []

def inicializar():
    for pin in pin_leds:
       print(pin,end=' ')
       led = machine.Pin(pin, machine.Pin.OUT)
       leds.append(led)
    print(' inicializados')

def encenderTodos():
    for led in range(len(leds)):
        leds[led].on() 

def apagarTodos():
    for led in range(len(leds)):
        leds[led].off()
        
def lanzamiento():
    for led in leds:
        led.on()
        utime.sleep(0.1)
        led.off()

def kit(tiempo_espera = 200):
    print('subiendo ...')
    for i in range(len(leds)):
        leds[i].on() # encendemos
        utime.sleep_ms(300) # esperamos ..
        leds[i].off() # lo apagamos
    print('bajando ...')        
    for i in range(len(leds)-1, 0,-1):
        leds[i].on() # encendemos
        utime.sleep_ms(300) # esperamos ..
        leds[i].off() # lo apagamos
        
    
