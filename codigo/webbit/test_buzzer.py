# test zumbador

import machine
import time

import webbit

v = 0.5

print(f'webbit {v}')

buzzer = machine.PWM(machine.Pin(webbit.PIN_BUZZER))

for i in range(10,20000,100):
    buzzer.freq(i)
    buzzer.duty(100)
    print(f'freq: {i}  ',end='\r')
    time.sleep_ms(200)
    
