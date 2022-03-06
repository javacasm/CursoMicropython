# fichero main.py

import machine
#import web_meteo
import web_control_led
import test_thingspeak

v = 0.3

try:
    # web_meteo.start_webServer()
    #web_control_led.start_webServer()
    test_thingspeak.pub_forever()
    #pass
except Exception as e:
    print(e)
    machine.reset()
    

