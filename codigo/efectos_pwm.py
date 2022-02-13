import time
import machine
import math

v = 0.4

def fadeIn(pin, tiempo_espera = 50):
    pwm_led = machine.PWM(machine.Pin(pin), freq = 500)
    for brillo in range(0,1023,10): # Hacemos que el rango vaya de 10 en 10
        pwm_led.duty(brillo)
        time.sleep_ms(tiempo_espera)
        print(brillo)        


def fadeOut(pin, tiempo_espera = 50):
    pwm_led = machine.PWM(machine.Pin(pin), freq = 500)
    for brillo in range(1023, 0, -10): # hacemos un rango decreciente
        pwm_led.duty(brillo)
        time.sleep_ms(tiempo_espera)
        print(brillo)
        
def pulse(pin, tiempo_espera): # acepta un pin y un tiempo para el efecto
    led_pwm = machine.PWM(machine.Pin(pin), freq = 1000)
    for i in range(20):
        led_pwm.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(tiempo_espera)
