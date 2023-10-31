# test de sensores de luz LDR

import machine
import time

import webbit

v = 0.3

print(f'test_ldr {v}')

luz_r = machine.ADC(machine.Pin(webbit.PIN_LDR_RIGHT))

luz_l = machine.ADC(machine.Pin(webbit.PIN_LDR_LEFT))

while True:
    print(f'{luz_l.read()} - {luz_r.read()}      ',end='\r')
    time.sleep_ms(100)