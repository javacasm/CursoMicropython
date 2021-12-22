# Test Sensor capacitivo TouchPad

v = '0.5.1'

import machine
import time
import config

tPad = machine.TouchPad(machine.Pin(config.pinTouch))
print(f'Using Touch @ {config.pinTouch}')


def test_forever():
    while True:
      print(tPad.read())
      time.sleep(0.2)
