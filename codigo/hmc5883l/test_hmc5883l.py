# test HMC5883l (compas/brujula)
# https://github.com/gvalkov/micropython-esp8266-hmc5883l

v= '0.3'

import hmc5883l
import config

sensor = hmc5883l.HMC5883L(scl=config.pinSCL,sda=config.pinSDA)

def read_compas():
    x,y,z = sensor.read()
    heading_gr,heading_min = sensor.heading(x,y)
    return x,y,z,heading_gr,heading_min

def test_forever():
    heading_gr0 = 0
    while True:
        x,y,z,heading_gr,heading_min = read_compas()
        if abs(heading_gr-heading_gr0)>2:
                print(sensor.format_result(x, y, z))
                heading_gr0 = heading_gr