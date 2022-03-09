import machine  
import ssd1306
import utime
import dht
import config

v = 0.3



sensorDHT22=dht.DHT22(machine.Pin(config.DHT_PIN))

i2c = machine.SoftI2C(scl = machine.Pin(21), sda = machine.Pin(22))


oled_width = 128 # ancho
oled_height = 64 # alto
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c, addr=0x3c) # Podria ser tambien 0x34

def getSensorData():
    sensorDHT22.measure()
    return (sensorDHT22.temperature(), sensorDHT22.humidity())

def getLocalTimeHumanFormat():
    strLocalTime = "{3:02}:{4:02}:{5:02} {2:02}/{1:02}/{0}".format(*utime.localtime(utime.time())[0:6])
    return strLocalTime

tabulacion = 8

def meteo():
    while True:
        try:
            temp, hum = getSensorData()
            sFecha = getLocalTimeHumanFormat()
            oled.fill(0) # borramos
            msgTemp = f'Temp: {temp:2.2f} C'
            oled.text(sFecha,0,oled_height -10)
            print(sFecha, end = ' ')
            oled.text(msgTemp, tabulacion, 15)
            print(msgTemp, end=' ')
            msgHum = f'Hum:  {hum:2.2f} %'
            oled.text(msgHum, tabulacion, 30)
            print(msgHum)
            oled.line(tabulacion,45,oled_width - 2 *tabulacion+2,45,1)
            oled.line(tabulacion,46,oled_width - 2 *tabulacion+2,46,1)
            oled.rect(54,12,60,13,1)
            oled.rect(54,27,60,13,1)
            
            oled.show()
            utime.sleep(1)
        except Exception as e:
            print(f'Error: {e} ')
        
        
