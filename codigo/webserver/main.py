# fichero main.py

import machine
import web_meteo

v = 0.3

try:
    web_meteo.start_webServer()
except Exception as e:
    print(e)
    machine.reset()
    

