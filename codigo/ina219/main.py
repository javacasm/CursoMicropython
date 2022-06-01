# import oled_meteo

# oled_meteo.meteo()

import machine

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

import test_u_ina219



test_u_ina219.test_all(forever=True)