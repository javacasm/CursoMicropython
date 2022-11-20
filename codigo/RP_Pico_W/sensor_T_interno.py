# reading Raspi Pico internal temperatura sensor

from machine import ADC
from time import sleep

tempADC = ADC(4) # ADC interno

factorV = 3.3/65535 # conversion de valor adc a V


while True:
    temp = 27 - (tempADC.read_u16()*factorV - 0.706)/0.001721    
    print (f'Temp: {temp}',end='\r')
    sleep(0.5)