import machine

v = 0.2

pin_leds = (26, 25, 17, 16, 27, 14, 12, 13) # Wemos D1 R32

leds = []

adc36 = machine.ADC(machine.Pin(36), atten = machine.ADC.ATTN_11DB) # Hasta 3.3v
adc36.width(machine.ADC.WIDTH_9BIT) # no necesitamos más precisión

def inicializar():
    for pin in pin_leds:
       print(pin,end=' ') # tras imprimir cada pin añade 1 espacio sin saltar de línea
       led = machine.Pin(pin, machine.Pin.OUT)
       leds.append(led)
    print(' inicializados')


def apagarTodos():
    for led in range(len(leds)): # iteramos usando el índice del rango
        leds[led].off()  

inicializar()
while True:
    volumen = adc36.read()
    apagarTodos()
    # encadenamos condiciones if
    if volumen < 100:
        leds[0].on()
    if volumen < 160:
        leds[1].on()
    if volumen < 360:
        leds[2].on()        
    if volumen < 560:
        leds[3].on()
    if volumen < 660:
        leds[4].on()
    if volumen < 760:
        leds[5].on()
    if volumen < 860:
        leds[6].on()
    if volumen < 950:
        leds[7].on()