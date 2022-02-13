import machine
import time

v = 0.2

adc36 = machine.ADC(machine.Pin(36))
adc36.atten(machine.ADC.ATTN_11DB) # 0 - 3.6v
    
pwm_rojo=machine.PWM(machine.Pin(26))

while True:
    valor_pot = adc36.read()
    brillo = valor_pot//4 # o int(valor_pot/4)
    print(valor_pot,' > ',brillo, end='  \r')
    pwm_rojo.duty(brillo)
    time.sleep_ms(100)