import dht
import machine
import time
import esp8266_i2c_lcd

v = 0.3

dht22 = dht.DHT22(machine.Pin(27)) # inicializamos el sensor dHT22

i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21)) # creamos el acceso al i2c
lcd = esp8266_i2c_lcd.I2cLcd(i2c, 0x27,2,16)  # creamos el lcd

lcd.putstr('Medida con DHT22')

while True:
    try:    
        dht22.measure()  # Leemos el sensor
        tempDHT22 = dht22.temperature()
        humDHT22 = dht22.humidity()
        sMsg = f'T:{tempDHT22} H:{humDHT22}'  # creamos una cadena con el contenido a mostrar
        print(sMsg)  # enviamos el mensaje a la consola
        lcd.move_to(0,1) # columna 0, fila 1
        lcd.putstr(sMsg) # enviamos el mensaje al LCD
    except:
        print('Error leyendo el sensor')
    time.sleep(1)
    