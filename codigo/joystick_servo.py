# control de torreta con joystick
import utime
import machine

v = 0.4

joyX = machine.ADC(machine.Pin(35))
joyY = machine.ADC(machine.Pin(34))

joyX.atten(machine.ADC.ATTN_11DB)
joyY.atten(machine.ADC.ATTN_11DB)
joyX.width(machine.ADC.WIDTH_9BIT)
joyY.width(machine.ADC.WIDTH_9BIT)

servoY = machine.PWM(machine.Pin(15), freq = 50)
servoX = machine.PWM(machine.Pin(16), freq = 50)

def map_value(valor, minOrigen, maxOrigen, minDestino, maxDestino):
    return int((valor - minOrigen)*(maxDestino-minDestino)/(maxOrigen-minOrigen) + minDestino)

def getServoValue(valor):
    return map_value(valor,0,511,45,115)

def getLedValue(valor):
    return map_value(valor,0,511,0,1023)


while True:
    joyx = joyX.read()
    joyy = joyY.read()
    servox = getLedValue(joyx) # getServoValue(joyx)
    servoy = getServoValue(joyy)
    servoX.duty(servox)
    servoY.duty(servoy)
    print(f' x:{joyx:4d} y:{joyy:4d} -> servox:{servox:4d} servoy:{servoy:4d}',end = '\r')
    utime.sleep_ms(50)