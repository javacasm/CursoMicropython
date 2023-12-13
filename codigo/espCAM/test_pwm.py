
import time
import machine

v = 0.3

def fadeIn(pin, tiempo_espera = 10):
    pwm_led = machine.PWM(machine.Pin(pin), freq = 500)
    for brillo in range(0,1023,10): # Hacemos que el rango vaya de 10 en 10
        pwm_led.duty(brillo)
        time.sleep_ms(tiempo_espera)
        print(brillo)
        
def fadeOut(pin, tiempo_espera = 10):
    pwm_led = machine.PWM(machine.Pin(pin), freq = 500)
    for brillo in range(1023, 0, -10
                        ): # hacemos un rango decreciente
        pwm_led.duty(brillo)
        time.sleep_ms(tiempo_espera)
        print(brillo)
        