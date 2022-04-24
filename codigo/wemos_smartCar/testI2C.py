# test de I2C

import machine
i2c = machine.SoftI2C(sda = machine.Pin(21),scl=machine.Pin(22),freq=100000)
i2c.scan()
