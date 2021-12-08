import machine

led = machine.Pin(2,machine.Pin.OUT)

while True:
    led.on()
    time.sleep(1)
    print('On')
    led.off()
    print('Off')
    time.sleep(1)