# test de lecturas de teclasos AD_Keys con ADC

v = '0.5'

import machine
import time

keyb=machine.ADC(machine.Pin(34)) # A3 de arduino

keyb.atten(machine.ADC.ATTN_11DB) # entre 0 y 3.6V
keyb.width(machine.ADC.WIDTH_9BIT) # entre 0 y 511


LEFT_KEY = 0
TOP_KEY = 46
DOWN_KEY = 146
RIGHT_KEY = 238
ENTER_KEY = 355
NO_KEY = 511

while True:
    value = keyb.read()
    key = ''
    if value == NO_KEY:
        key = 'NoKey'
    elif value >= ENTER_KEY:
        key = 'Enter '
    elif value >= RIGHT_KEY:        
        key = 'Right '
    elif value >= DOWN_KEY:        
        key = 'Down  '
    elif value >= TOP_KEY:        
        key = 'Top   '
    elif value >= LEFT_KEY:        
        key = 'Left  '
    else:        
        key = 'Unkown'

    print(f'{value} {key} ', end='\r') # Salen los datos en la misma linea
    
    time.sleep_ms(200)
