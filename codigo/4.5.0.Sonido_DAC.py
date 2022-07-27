import machine
import math
import time

v = 0.5

dac25 = machine.DAC(machine.Pin(25))

def tono(tiempo = 0): # Onda de sierra
    for i in range(10000):
        valor = i%256 # módulo 256 para que esté entre 0 y 255
        dac25.write(valor) 
        time.sleep_us(tiempo)
       
wave = []
def replay(t): 
    if len(wave) == 0:
        for grado in range(360): # 360 grados son un ciclo entero
            valor = int(128 + 127 * (math.sin(20 * grado * math.pi / 180)))
            wave.append(valor)
    
    for i in range(10):
        for w in wave:
            dac25.write(w)
            time.sleep_us(t)

def seno( m = 1): # Onda sinusoidal
    for grado in range(360): # 360 grados son un ciclo entero
        valor = int(128 + 127 * (math.sin(m * grado * math.pi / 180)))
        dac25.write(valor)
        
def efecto_subida():
    for t in range(0,100,5):
        seno(t)