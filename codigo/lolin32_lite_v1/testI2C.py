import config
import machine
# test de I2C

v = '0.4'


i2c = machine.SoftI2C(sda = machine.Pin(config.pinSDA),scl=machine.Pin(config.pinSCL),freq=100000)

def scan_I2C():
    addresses = i2c.scan()
    if len(addresses) > 1:
        for address in addresses:
            print(f'{hex(address)} ({address})')
    else: print('No devices')


