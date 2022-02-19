import time
import machine
import esp32


v = '0.3'

def convertFahrenheit2Celsius(f):
    return (f-32)*5/9

def performanceTest(duracion_segundos = 10):
    print(f'frecuencia: {machine.freq()}')
    print(f'CPU Temp: {convertFahrenheit2Celsius(esp32.raw_temperature())} start}')
    endTime = time.ticks_ms() + duracion_segundos * 1000
    count = 0
    while time.ticks_ms() < endTime:
        count += 1
    print('Count: {count} CPS:{count/duracion_segundos}')
    print(f'CPU Temp: {convertFahrenheit2Celsius(esp32.raw_temperature())} end}')

performanceTest()

machine.freq(240000000) # 240MHz

performanceTest()