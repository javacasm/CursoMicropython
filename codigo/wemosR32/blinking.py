import machine
import time

v = 0.4 # Gracias Kiko

# setup en arduino
led = machine.Pin(2, machine.Pin.OUT)


def parpadeo(tiempo_endendido = 250,tiempo_apagado = 250):
    # tiempos en milisegundos
    led.on()
    time.sleep_ms(tiempo_endendido)  # en milisegunos
    led.off()
    time.sleep_ms(tiempo_apagado)   # en milisegunos
# se acaba la función

def blinking_forever():
    while True :  # bucle loop en arduino
        parpadeo()
        
        # esta en el bucle
#fuera de la función
