import machine
import time

rele = machine.Pin(17, machine.Pin.OUT)

adc36 = machine.ADC(machine.Pin(36), atten = machine.ADC.ATTN_11DB) # Hasta 3.3v
adc36.width(machine.ADC.WIDTH_10BIT) # no necesitamos más precisión

medidaSueloHumedo = 600 # Los determinamos empíricamente
medidaSueloSeco = 400

while True:
    valor_humedad = adc36.read()
    if valor_humedad < medidaSueloSeco:
        rele.on()
        print('Encendemos el riego')

    if valor_humedad > medidaSueloHumedo:
        rele.off()  
        print('Apagamos el riego') 