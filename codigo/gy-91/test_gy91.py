import micropython
from machine import SoftI2C, Pin, Timer
from mpu9250 import MPU9250
import config

v = '0.2'

micropython.alloc_emergency_exception_buf(100)

i2c = SoftI2C(scl=Pin(config.pinSCL), sda=Pin(config.pinSDA))

sensor = MPU9250(i2c)

def read_sensor(timer):
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

print("MPU9250 id: " + hex(sensor.whoami))

timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=read_sensor)