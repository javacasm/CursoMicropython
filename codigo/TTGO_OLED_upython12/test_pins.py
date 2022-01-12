import machine
import time

v = '0.5.3'

BUTTON_LEFT = 0
BUTTON_RIGHT = 35

PIN_POWER = 14
ADC_BAT = 34

PIN_BACKLIGHT = 4

button_left = machine.Pin(BUTTON_LEFT,machine.Pin.IN)
button_right = machine.Pin(BUTTON_RIGHT,machine.Pin.IN)

power  = machine.Pin(PIN_POWER, machine.Pin.IN)

backLight = machine.Pin(PIN_BACKLIGHT, machine.Pin.OUT)

adc_bat = machine.ADC(machine.Pin(ADC_BAT))
adc_bat.atten(machine.ADC.ATTN_11DB)



while True:
    print('left: ',button_left.value(), ' right: ',button_right.value(),' Bat: ',adc_bat.read_u16(),' Power: ', power.value(), end='\r')
    backLight.value( not button_left.value())
    time.sleep_ms(200)