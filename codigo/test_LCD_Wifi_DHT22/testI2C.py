# test de I2C

v = '0.2'

import machine
i2c = machine.SoftI2C(sda = machine.Pin(21),scl=machine.Pin(22),freq=100000)
addresses = i2c.scan()
for address in addresses:
    print(f'{hex(address)} ({address})')