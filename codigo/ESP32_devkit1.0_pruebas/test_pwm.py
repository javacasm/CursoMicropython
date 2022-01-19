# ejemplo de pwm
import time
import machine

led = machine.Pin(26, machine.Pin.OUT)
pwm = machine.PWM(led)

for brillo  in range(0,1023):
    pwm.duty(brillo)
    time.sleep(0.01)
    print(brillo)