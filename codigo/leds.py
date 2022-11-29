# trabajando con varios leds
import machine
import utime

v = 0.5

# pin_leds = (26, 25, 17, 16, 27, 14, 12, 13) # Wemos D1 R32
# pin_leds = (0, 16, 12, 13, 15, 14, 2, 4) # ESPCAM CUIDADO CON EL GPIO 0
pin_leds = (12,17,13,32,25 ,26, 33,27) # TTGO - TFT
leds = []

def inicializar():
    for pin in pin_leds:
       print(pin,end=' ') # tras imprimir cada pin añade 1 espacio sin saltar de línea
       led = machine.Pin(pin, machine.Pin.OUT)
       leds.append(led)
    print(' inicializados')

def encenderTodos():
    if len(leds) != len(pin_leds):
        inicializar()
    for led in leds:  # Iteramos en todos los leds
        led.on() 

def apagarTodos():
    if len(leds) != len(pin_leds):
        inicializar()    
    for led in range(len(leds)): # iteramos usando el índice del rango
        leds[led].off()  
        
def kit(tiempo_espera = 200):
    if len(leds) != len(pin_leds):
        inicializar()    
    print('subiendo ...')
    for i in range(len(leds)):
        leds[i].on() # encendemos
        utime.sleep_ms(tiempo_espera) # esperamos ..
        leds[i].off() # lo apagamos
    print('bajando ...')        
    for i in range(len(leds)-1,-1,-1): # N -1 es el último
        print(i)
        leds[i].on() # encendemos
        
        utime.sleep_ms(tiempo_espera) # esperamos ..
        leds[i].off() # lo apagamos        
