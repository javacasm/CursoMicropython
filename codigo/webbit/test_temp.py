# test de sensor de temperatura

import machine
import time

import webbit

v = 0.2

print(f'test_temp {v}')

temp = machine.ADC(machine.Pin(webbit.PIN_TEMP))

while True:
    print(f'{temp.read()}    ',end='\r')
    time.sleep_ms(100)