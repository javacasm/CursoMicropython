import machine
import time

v = 0.4

#setup en arduino

led = machine.Pin(2, machine.Pin.OUT)

def parpadeo(tiempo_encendido = 250,tiempo_apagado = 250) :
    # empieza la funcion, tiempos en milisegundos
    led.on()
    time.sleep_ms(tiempo_encendido) # en milisegundos
    led.off()
    time.sleep_ms(tiempo_apagado) # en segundos
# se acaba la funcion 

def parpadeo_forever() :
    while True : # bucle loop en arduino
        parpadeo()
        # esta está dentro del bucle
# esta está fuera del bucle