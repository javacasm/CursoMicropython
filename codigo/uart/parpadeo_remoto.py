import machine
import time

uart2 = machine.UART(2, baudrate=9600, tx=17, rx=16)


def parpadeo_remoto(retardo_ms=500):

    while True:
        uart2.write('H')
        print('Light on!')
        time.sleep_ms(retardo_ms)
        uart2.write('L')
        print('Light off!')
        time.sleep_ms(retardo_ms)

parpadeo_remoto()