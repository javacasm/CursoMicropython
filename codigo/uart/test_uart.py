from machine import UART
from time import ticks_ms, sleep_ms

# ![](./images/Wemos_d1_R32_serial_Arduino_UNO_bb.png)

v = 0.4

uart2 = UART(2, baudrate=9600, tx=17, rx=16)

def sendCommand(command):
    print(f'> command({command})')
    uart2.write(command)
    
def phisicalPixelMaster(delay_ms = 30):
    
    while True:
        sendCommand('H')
        sleep_ms(delay_ms)
        sendCommand('L')
        sleep_ms(delay_ms)
        
physicalpixel_comands = ['H', 'L']
def sendCommands(comands, retardo_ms=500):
    last_time_command = ticks_ms()
    counter = 0
    while True:
        now = ticks_ms()
        if now - last_time_command > retardo_ms:
            sendCommand(comands[counter%len(comands)])
            counter += 1
            last_time_command = now
        while uart2.any()>0: # hay datos
            line = uart2.readline().decode('UTF-8').replace('\r\n','')
            print(f'< "{line}"')

def echoSerial():
    while True:
        c =uart0.read()
        uart0.write(c)
        print('< {c}\necho > {c}')

# test_uart.sendCommands(['H','L','T'],retardo_ms=20)