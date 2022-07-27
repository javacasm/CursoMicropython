import machine
import time

rele = machine.Pin(17, machine.Pin.OUT)

adc36 = machine.ADC(machine.Pin(36), atten = machine.ADC.ATTN_11DB) # Hasta 3.3v
adc36.width(machine.ADC.WIDTH_9BIT) # no necesitamos más precisión

medidaLuz = 600 # Los determinamos empíricamente
medidaOScuridad = 400

while True:
    valor_luz = adc36.read()
    if valor_luz < medidaOScuridad:
        rele.on()
        print('Encendemos la luz')

    if valor_luz > medidaLuz:
        rele.off()  
        print('Apagamos la luz')  