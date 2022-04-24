import machine
import time
import dht

pin_rele =16
DHT_pin = 14

rele=machine.Pin(pin_rele, machine.Pin.OUT)

sensor=dht.DHT22(machine.Pin(DHT_pin))
                 
def ventilador():   
    while True :
         sensor.measure()
         if sensor.temperature() > 24 :
            rele.on()
            print("Encendemos el rele")
         else :
            rele.off()
            print("Apagamos el rele")
                
         time.sleep(1)

