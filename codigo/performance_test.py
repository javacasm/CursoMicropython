import time
import machine
import esp32


v = '0.6'

def convertFahrenheit2Celsius(f):
    return (f-32)*5/9

def rawTempCelsius():
    return convertFahrenheit2Celsius(esp32.raw_temperature())

def performanceTest(duracion_segundos = 10):
    print(f'freq: {machine.freq()//1000000} MHz',end = ' ')
    temp_start = rawTempCelsius()
    endTime = time.ticks_ms() + duracion_segundos * 1000
    count = 0
    while time.ticks_ms() < endTime:
        count += 1
    print(f'Count: {count} CPS:{count/duracion_segundos}', end =' ')
    temp_end = rawTempCelsius()
    print(f'CPU Temp: {temp_start:2.2f} > {temp_end:2.2f} ')

for f in [20, 40, 80,160,240]:
    machine.freq(f*1000000)
    performanceTest()

