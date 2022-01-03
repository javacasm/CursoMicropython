# test de I2C

v = '0.3.1'

import machine
i2c = machine.SoftI2C(sda = machine.Pin(21),scl=machine.Pin(22),freq=100000)

def scan_I2C():
    addresses = i2c.scan()
    for address in addresses:
        print(f'{hex(address)} ({address})')

