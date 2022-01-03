# módulos usados
import machine
import time

import pins

v='0.1'


# objetos para inicializar motores
def M1SetUp():
    global in1, in2, ena
    in1 = machine.Pin(pins.IN1,machine.Pin.OUT) #definimos un objeto pin con las propiedades de los de su tipo
    in2 = machine.Pin(pins.IN2,machine.Pin.OUT)
    ena = machine.PWM(machine.Pin(pins.ENA), freq = 100)

def M2SetUp():
    in3 = machine.Pin(pins.IN3,machine.Pin.OUT)
    in4 = machine.Pin(pins.IN4,machine.Pin.OUT)
    enb = machine.PWM(machine.Pin(pins.ENB), freq = 100)
"""
La freq es el nº de veces que dividimos una función (sen por ejemplo),
cuantas más divisiones más precisa y más difícil de procesar. La frecuencia
de muestreo tiene que ser al menos el doble que la de la señal (Teorema de Nyquist).
Si cada vez que comprobamos la señal, está al máximo la velocidad va a ser la máxima,
para conseguir velocidades intermedias ponemos un nº de veces la señal al máximo y
otro al mínimo (porque es digital) así consigues el efecto analógico.
"""
# Objetos para expresar la velocidad
def M1SetSpeed (percent):
    speed = float(100)*percent/1023
    ena.duty(int(speed))
    
def M2SetSpeed (percent):
    speed = float(100)*percent/1023
    enb.duty(int(speed))
    
# Objetos movimientos de los motores
def M1Forward():
    in1.off()
    in2.on()

'''def robotForward():
    
def robotForward():
    
def robotForward():
    
def robotForward():
    
def robotForward():
    
def robotForward():
#crear funciones'''

