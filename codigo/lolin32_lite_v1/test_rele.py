import machine
import config

v = '0.4.2'

rele = machine.Pin(config.pinRele,machine.Pin.OUT)
print(f'rele @ {config.pinRele}')

Verbose = True

def releOn():
    rele.on()
    if Verbose :     print('Rele On')
    
def releOff():
    rele.off()
    if Verbose :  print('Rele Off')    
