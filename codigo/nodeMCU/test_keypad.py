import machine
import time

v = 0.2

KEY_LEFT = 10    # SW1
KEY_UP = 180     # SW2
KEY_DOWN = 375   # SW3
KEY_RIGHT = 560  # SW4
KEY_ENTER = 805  # SW5

adc = machine.ADC(0)

print('Waiting por keypress...')

while True:
    value = adc.read()
    print('\r',value,end=' ')
    if value < KEY_LEFT:
        print('Left')
    elif value < KEY_UP:
        print('Forward')
    elif value < KEY_DOWN:
        print('Backward')
    elif value < KEY_RIGHT:
        print('Right')
    elif value < KEY_ENTER:
        print('Enter')
    else:
        # No key
        time.sleep_ms(100)

        