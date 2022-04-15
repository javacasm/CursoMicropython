from pyb import LED
import utime

v = 0.3


led = LED(1)  # available LED（1），LED（2）

print('led on')
led.on()      # switch on the LED
print('led off')
led.off()     # switch off the LED
print('invertir led')
led.toggle()  # invert the LED state
print('fade in')
for i in range(256):
    led.intensity(i)  # value between 0 and 255
    utime.sleep_ms(5)
print('fade out')    
for i in range(255,0,-1):
    led.intensity(i)  # value between 0 and 255
    utime.sleep_ms(5)
print('led off')
led.off()

