import machine

import config

i2c = machine.SoftI2C(sda = machine.Pin(config.pinSDA), scl=machine.Pin(config.pinSCL),freq=100000)

i2c.scan()