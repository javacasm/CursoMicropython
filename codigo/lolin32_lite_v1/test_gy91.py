import micropython
from machine import SoftI2C, Pin, Timer
from mpu9250 import MPU9250
import BME280
import config

v = '0.5.3'

micropython.alloc_emergency_exception_buf(100)

i2c = SoftI2C(scl=Pin(config.pinSCL), sda=Pin(config.pinSDA))
print(f'{i2c.scan()}')
sensor = MPU9250(i2c)

bme = BME280.BME280(i2c = i2c) 

def read_sensor(timer):
    print(f'MPU9250\tAccel: {sensor.acceleration}')
    print(f'MPU9250\tGyro: {sensor.gyro}')
    print(f'MPU9250\tCompass: {sensor.magnetic}')
    print(f'MPU9250\tTemp: {sensor.temperature}')
    print(f'bme280\tTemp: {bme.temperature}\n\tPress: {bme.pressure}\n\tHum: {bme.humidity}')

print("MPU9250 id: " + hex(sensor.whoami))
print('BME280 @ 0x76')


timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=read_sensor)

