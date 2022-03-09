import machine
import time

joyX = machine.ADC(machine.Pin(32))
joyX.atten(machine.ADC.ATTN_11DB)

joyX.width(machine.ADC.WIDTH_9BIT)
joyY = machine.ADC(machine.Pin(35))
joyY.width(machine.ADC.WIDTH_9BIT)
joyY.atten(machine.ADC.ATTN_11DB)

switch = machine.Pin(34,machine.Pin.IN,machine.Pin.PULL_UP)

while True:
    print(f'{switch.value()} ({joyX.read()},{joyY.read()}) ',end = '\r')
    time.sleep_ms(100)