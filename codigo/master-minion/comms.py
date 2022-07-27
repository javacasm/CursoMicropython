# Com master

import machine
from machine import UART
from time import ticks_ms, sleep_ms
from comandos import *

v = 0.5

pinLed_builtin = 2
pinPot_retardo = 35

pot = machine.ADC(machine.Pin(pinPot_retardo))
pot.atten(machine.ADC.ATTN_11DB)
pot.width(machine.ADC.WIDTH_10BIT)

led = machine.Pin(pinLed_builtin,machine.Pin.OUT)
led.off()

ledbright = machine.PWM(led)
ledbright.duty(0)

time2waitResponse = 2

uart2 = UART(2, baudrate=115200, tx=17, rx=16, timeout=time2waitResponse, timeout_char=time2waitResponse)

debugEnable = True

def debug(text):
    if debugEnable: print(text)

def sendCommand(command):
    global uart2
    debug(f'>e>: {command}')
    uart2.write(command)
    sleep_ms(time2waitResponse)
    response=''
    while uart2.any()>0:
        responseChar=uart2.read().decode('UTF-8')
        response+=responseChar
    debug(f'<e<: [{response}]')
    value = RESULT_ERROR
    if response.startswith(command): value = RESULT_OK
    return value        
  
def sendCommandReturnFloat(command):
    global uart2
    debug(f'>e>: {command}')
    uart2.write(command)
    sleep_ms(time2waitResponse)
    response=''
    while uart2.any()>0:
        responseChar=uart2.read().decode('UTF-8')
        response+=responseChar
    # debug(f'<e<: [{response}]')
    fresponse = RESULT_ERROR
    if response.startswith(command):
        try:
            fresponse = float(response[1:-1])
            debug(f'<e<: [{fresponse}]')
        except Exception as e:
            debug(f'Error in float response [{response}]: {e}')
    return fresponse  

def sendCommandArgument(command,valor):
    global uart2
    commandFull = command+str(valor)+END_NUMBER
    debug(f'>e>: {commandFull}')
    uart2.write(commandFull)
    sleep_ms(time2waitResponse)
    response=''
    while uart2.any()>0:
        responseChar=uart2.read().decode('UTF-8')
        response+=responseChar
    debug(f'<e<: [{response}]')
    value = RESULT_ERROR
    if response.startswith(command): value = RESULT_OK
    return value 

def brightPotControlled():
    ledbright.init()
    while True:
        potValue = pot.read()
        espera = brillo = potValue//4
        ledbright.duty(brillo*2)
        sendCommandArgument(PWM_PIN_COMMAND,brillo)
        sleep_ms(espera)

def physicalPixelMasterPot():
    led = machine.Pin(pinLed_builtin,machine.Pin.OUT)
    while True:
        potValue = pot.read()
        espera = potValue//4
        led.on()
        sendCommand(HIGH_PIN_COMMAND)
        sleep_ms(espera)
        led.off()
        sendCommand(LOW_PIN_COMMAND)
        sleep_ms(espera)

def getFloatData(delay_ms = 30):
    while True:
        sendCommandReturnFloat(GET_TEMP_COMMAND)
        sleep_ms(delay_ms)

def physicalPixelMaster(delay_ms = 30):
    while True:
        sendCommand(HIGH_PIN_COMMAND)
        sleep_ms(delay_ms)
        sendCommand(LOW_PIN_COMMAND)
        sleep_ms(delay_ms)
        
physicalpixel_comands = [HIGH_PIN_COMMAND, LOW_PIN_COMMAND]
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

