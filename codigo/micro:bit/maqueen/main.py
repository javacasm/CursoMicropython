## ejemplo de uso del modulo para controlar maqueen desde micro:bit

# License CC by SA @javacasm 2022

v = 0.4

import microbit
import maqueen
import utime


maqueen.test_i2c()

for i in range(4): # repetimos 4 veces
    microbit.display.show(microbit.Image.ARROW_N)
    maqueen.straight(100) # adelante
    utime.sleep(2)      # 1 segundo avanzando
    maqueen.turn(100)
    microbit.display.show(microbit.Image.ARROW_E)
    utime.sleep_ms(500)      # 1 segundo avanzando
microbit.display.show(microbit.Image.SQUARE)
maqueen.stop()