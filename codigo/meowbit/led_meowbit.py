import meowbit
import utime

v = 0.1

#  podemos usar meowbit.led1 o led2 que ya vienen definidos

print('led on')
meowbit.led1.on()      # switch on the LED
print('led off')
meowbit.led1.off()     # switch off the LED
print('invertir led')
meowbit.led1.toggle()  # invert the LED state
print('fade in')
for i in range(256):
    meowbit.led1.intensity(i)  # value between 0 and 255
    utime.sleep_ms(5)
print('fade out')    
for i in range(255,0,-1):
    meowbit.led1.intensity(i)  # value between 0 and 255
    utime.sleep_ms(5)
print('led off')
meowbit.led1.off()
