import machine
import time

v = 0.3

pulsador = machine.Pin(17, machine.Pin.IN)

led = machine.Pin(26, machine.Pin.OUT)

while True:
    if  pulsador.value() == 1: # está activo
      led.on()
      print('On')
    else:  # no está activo
      led.off()
      print('off')
    time.sleep_ms(200) # ponemos un pequeño retardo para no saturar la pantalla