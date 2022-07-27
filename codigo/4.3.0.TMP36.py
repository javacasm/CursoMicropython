import machine

adc36 = machine.ADC(machine.Pin(36), atten = machine.ADC.ATTN_11DB)
adc36.width(machine.ADC.WIDTH_9BIT)
valor = adc36.read() # entre 0 y 512

volts = 3.3 * valor / 512 # normalizamos a voltios
temperatura = (volts - 0.5) * 100  # calculamos la temperatura

print('Temperatura: ',temperatura)