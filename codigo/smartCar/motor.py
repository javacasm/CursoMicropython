''' Motor class 1/2 de L298N
    Usamos 3 pines:
        En para controlar la velocidad
        In1 & In2 para controlar la direccion
'''
# from math import abs
import machine

v = '0.6'

class motor:
    def __init__(self, In1, In2, En):
        self._in1 = In1
        self._in2 = In2
        self._en  = En
        self._attached = False
        self._debug()
    
    def attach(self):
        if not self._attached :
            self.IN1 = machine.Pin(self._in1, machine.Pin.OUT)
            self.IN2 = machine.Pin(self._in2, machine.Pin.OUT)
            self.EN  = machine.PWM(machine.Pin(self._en), freq = 100)
            self._attached = True      
            self._debug()

    def _debug(self):
        print(f'{__name__} v:{v}')
        print(f'In1:{self._in1}\nIn2:{self._in2}\nEn:{self._en}\nAttached:{self._attached} ')

    def stop(self):
        self.attach()
        self.IN1.value(0)
        self.IN2.value(0)
        self.EN.duty(0)
        # print('STOP')

    def move(self, speed):
        self.attach()
        # velocidad entre -1023 y 1023
        # print('Speed: {speed}')
        if speed>0:
            self.IN1.value(1)
            self.IN2.value(0)
        elif speed < 0:
            self.IN1.value(0)
            self.IN2.value(1)
        else :
            self.stop()
        self.EN.duty(abs(speed))
