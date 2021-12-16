import machine
import config

v = '0.3'

rele = machine.Pin(config.pinRele,machine.Pin.OUT)
print(f'rele @ {config.pinRele}')

def releOn():
    rele.on()
    print('Rele On')
    
def releOff():
    rele.off()
    print('Rele Off')    
