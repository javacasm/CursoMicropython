import machine 
import time

v = 0.3

pulsado = False

def interupcion_pulsador(pin):
    global pulsado
    print('detectado')
    pulsado = True


led = machine.Pin(12, machine.Pin.OUT)
led.off()
pulsador = machine.Pin(35, machine.Pin.IN,machine.Pin.PULL_DOWN)

pulsador.irq(trigger=machine.Pin.IRQ_RISING, handler = interupcion_pulsador)

while True:
  if pulsado:
    print('Pulsado. ¡encendiendo la luz!')
    led.on()
    time.sleep(20) # 20 segundos encendido
    print('Apagado!')
    led.off()
    pulsado = False