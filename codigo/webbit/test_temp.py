# test de sensor de temperatura

import machine
import time

import webbit

v = 0.6

print(f'test_temp {v}')

temp = machine.ADC(machine.Pin(webbit.PIN_TEMP))
temp.atten(machine.ADC.ATTN_11DB) #  0-3.9V

Tp = 273.15
T = Tp + 10 #+ 25 # Normal Temperature Parameters
_T = 1 / T
B = 3950
 
def readTemp():
    adc_val = temp.read()
    Vout = adc_val * 3.9 / 8191.0
    if 0 < Vout and Vout < 3.3: # -26.9 and 160.5
        Rt = ((3.3 / Vout) - 1) * 0.51  # Sampling Resistance is 5.1K ohm
        import math
        T1 = 1 / (_T + math.log(Rt) / B) - Tp
        return round(T1, 1)
    print('ADC Value Error!')
        
while True:
    print(f'{readTemp()}  ',end='\r')
    time.sleep_ms(100)