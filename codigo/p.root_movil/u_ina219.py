from machine import SoftI2C, Pin
""" 
INA219 Power Monitor interface.
Copyright GPL3.0 sergei.nz.
https://www.ti.com/lit/ds/symlink/ina219.pdf
original from https://sergei.nz/interfacing-ina219-board-with-micropython
updated by @javacasm
"""
v = 0.7

MAX_CURRENT = 3.2 # Amps
CURRENT_LSB = MAX_CURRENT/(2**15)
R_SHUNT = 0.1 # Ohms
CALIBRATION = int(0.04096 / (CURRENT_LSB * R_SHUNT))

CONF_R = 0x00
SHUNT_V_R = 0x01
BUS_V_R = 0x02
POWER_R = 0x03
CURRENT_R = 0x04
CALIBRATION_R = 0x05

DEFAULT_ADDRESS = 0x40 # 0x44

i2c = None 

avoid_address = []

def init_i2c(pinSDA,pinSCL):
    global i2c
    print(f'SDA={pinSDA} SCL = {pinSCL}')
    i2c = SoftI2C(scl = Pin(pinSCL), sda = Pin(pinSDA))    

def init_ina219(address = DEFAULT_ADDRESS):
    global i2c
    i2c.writeto_mem(address, CALIBRATION_R ,(CALIBRATION).to_bytes(2, 'big'))

def init_all(pinSDA,pinSCL,devs = None):
    global i2c
    if i2c == None:
        init_i2c(pinSDA,pinSCL)
    if devs == None:
        devs = i2c.scan()
        print(devs)
    for address in devs:
        if address not in avoid_address:
            init_ina219(address=address)
        else:
            devs.remove(address)
    return devs

def read_current(address = DEFAULT_ADDRESS):
    global i2c
    raw_current = int.from_bytes(i2c.readfrom_mem(address, SHUNT_V_R, 2), 'big')
    if raw_current >> 15:
        raw_current -= 2**16
    return raw_current * CURRENT_LSB

def read_current_ma(address = DEFAULT_ADDRESS):
    return int(100000*read_current(address))/100

def read_voltage(address = DEFAULT_ADDRESS):
    global i2c
    return (int.from_bytes(i2c.readfrom_mem(address, BUS_V_R, 2), 'big') >> 3) * 0.004

def read_all(devs = None):
    global i2c
    if devs == None:
        devs = i2c.scan()
    data = []
    for address in devs:
        v = read_voltage(address=address)
        i = read_current_ma(address=address)
        data.append(v)
        data.append(i)
    #    print(f'@{address} {v}v {i}ma',end=' ')
    # print()
    return data