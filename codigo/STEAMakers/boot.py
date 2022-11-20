# This file is executed on every boot (including wake-boot from deepsleep)

v = 0.1

print(f'boot {v}')

#import esp
#esp.osdebug(None)

import test_steamakers
test_steamakers.test_network()

import webrepl
webrepl.start()
