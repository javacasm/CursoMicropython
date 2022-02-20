import machine
import time
import MotorShield

v = '0.6.4'


KEY_LEFT  =  10  # SW1
KEY_UP    = 180  # SW2
KEY_DOWN  = 375  # SW3
KEY_RIGHT = 560  # SW4
KEY_ENTER = 807  # SW5

adc = machine.ADC(0)

encoder = machine.Pin(14, machine.Pin.IN)

current_speed = 400

Contador = 0

def handler_irq(pin):
    global Contador
    Contador += 1
    # print(Contador,end = '\r')

encoder.irq(trigger=machine.Pin.IRQ_FALLING, handler=handler_irq)

def test_encoder():
    print('Waiting por keypress...')
    while True:
        value = adc.read()
        # print(f'\r {value} - {MotorShield.current_speed} - {Contador}' ,end=' ')
        print('\r ', value,' - ', current_speed, ' - ', Contador, end=' ')
        if value < KEY_LEFT:
            current_speed -= 10
            if current_speed < 0:
                current_speed = 0
            MotorShield.setSpeed(current_speed)
            # print('Left')
        elif value < KEY_UP:
            # print('Forward')
            MotorShield.forward(current_speed)
        elif value < KEY_DOWN:
            # print('Backward')
            MotorShield.backward(current_speed)
        elif value < KEY_RIGHT:
            # print('Right')
            current_speed +=  10
            if current_speed > 1023:
                current_speed = 1023
            MotorShield.setSpeed(current_speed)
        elif value < KEY_ENTER:
            # print('Enter')
            MotorShield.stop()
        else:
            # No key
            pass
        time.sleep_ms(100)

nEncoder = 36

def vuelta(nVueltas = 1):
    global Contador
    Contador = 0
    pasos = nEncoder * nVueltas
    MotorShield.forward(500)
    while Contador < pasos:
        print(Contador,end=' \r')
        time.sleep_ms(10)
    else:
        print(Contador,end=' \r')
    MotorShield.stop()
