



```python
import machine
import time

v = '0.5.3'

BUTTON_LEFT = 0
BUTTON_RIGHT = 35

PIN_BACKLIGHT = 4

button_left = machine.Pin(BUTTON_LEFT,machine.Pin.IN)
button_right = machine.Pin(BUTTON_RIGHT,machine.Pin.IN)


backLight = machine.Pin(PIN_BACKLIGHT, machine.Pin.OUT)


while True:
    print('left: ',button_left.value(), ' right: ',button_right.value(), end='\r')
    backLight.value( not button_left.value())
    time.sleep_ms(200)
```


Pin.IN, Pin.OUT ¿pullup? ¿Pulldown? ¿activar/descativar pullup?

### Interrupciones

IRQ_FALLING o IRQ_RISING

button_left.irq(trigger = machine.Pin.IRQ_FALLING, handler = button_irq, , machine.Pin.PULL_UP)
Puede ser PULL_UP o None


https://docs.micropython.org/en/latest/esp8266/tutorial/pins.html?highlight=interrupt

