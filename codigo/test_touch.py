# Test Sensor capacitivo TouchPad

v = '0.1'

import machine
import time

tPad12 = machine.TouchPad(machine.Pin(12))

while True:
  print(tPad12.read())
  time.sleep(0.2)

  