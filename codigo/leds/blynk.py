import machine
import time

v = 0.9

def blynky(pin_led,tiempo_espera=0.5):

    led = machine.Pin(pin_led, machine.Pin.OUT)

    print('Blynk en pin ' , pin_led)
    while True:
        led.on()
        print('On')
        time.sleep(tiempo_espera) # 200 milisegundos
        led.off()
        print('Off')
        time.sleep(tiempo_espera) 

# Fuera de la funcion

print('Importado modulo bkynk v',v)