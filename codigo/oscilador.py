# Oscilador
# based on the original Servo Oscillator code by Juan Gonzalez-Gomez (Obijuan),
# which is part of his [ArduSnake project](http://www.iearobotics.com/wiki/index.php?title=ArduSnake:amplituderduino_Modular_Snake_Robots_Library) (on [Github](https://github.com/Obijuan/ArduSnake))
# and [ServoOsc](https://github.com/fitzterra/ServoOsc) de @fitzterra.

'''

offset: centro de la oscilacion
amplitud: amplitud del movimiento a ambos lados de la posicion
periodo: tiempo que tarda en hacer 2 amplitudes
pin: 

update() # comprueba si se tiene que actualizar y actualiza la posicion 

_posicion
_ultima_actualizacion

'''
import time

v = '0.2'

UPDATE_RATE = 30

class oscilador():
    def _init_(self,pin,offset,amplitud,periodo):
        self.pin = pin
        self.offset = offset
        self.amplitud = amplitud
        self.periodo = periodo
        self.posicion = offset
        self.minPosicion = offset - amplitud/2
        self.maxPosicion = offset + amplitud/2
        self.last_update = 0
        self.servo = machine.PWM(machine.Pin(pin),freq = baseFreq)
        self.incremento = 2*self.amplitud*UPDATE_RATE/self.periodo
        self.movimiento = 1
        
    def update(self):
        now = time.ticks_ms()
        if now-self.last_update > UPDATE_RATE:
            self.last_update = now
            # ¿se suma o no?
            newPosition = self.posicion + self.incremento 
            if newPosition > self.maxPosicion:
                newPosition = self.maxPosicion
            self.servo.duty(newPosition)
            self.posicion = newPosition
            