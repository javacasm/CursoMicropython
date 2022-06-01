import dht
import machine
import ina219
import onewire, ds18x20
import time

v = 0.4

i2c = None

def test_DHT22(pin = 23):
    dhtsensor = dht.DHT22(machine.Pin(pin))
    try:
        dhtsensor.measure()
        temp = dhtsensor.temperature()
        hum = dhtsensor.humidity()
        print(f'dht22 @ {pin} temp: {temp} C hum: {hum} %')
    except Exception as e:
        print(f'DHT Error: {e}')
        
def test_I2C():
    global i2c
    
    i2c = machine.SoftI2C(scl = machine.Pin(21), sda = machine.Pin(22))
    print('i2c scan:', i2c.scan())

def test_ina219(address = 68):
    global i2c
    if i2c == None:
        test_I2C()
    ina = ina219.INA219(0.1,i2c,address=address)
    print(f'address: {address} volt:{ina.voltage()} current:{ina.current()} supply_voltage: {ina.supply_voltage()}')

def test_all_ina219():
    global i2c
    devs= i2c.scan()
    for dev in devs:
        test_ina219(address=dev)

def bRom2str(rom):
    str=''
    for b in rom[1:]:
        sb = ''
        if b<16:
            sb = '0'
        str += sb + hex(b)[2:] + ':'
    return str

def test_all_ds18x20(pin = 19):
    # from https://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html
    dat = machine.Pin(pin)
    ds = ds18x20.DS18X20(onewire.OneWire(dat))
    roms = ds.scan()
    print(f'Found {len(roms)} DS Sensors')
    ds.convert_temp() # iniciamos la conversion
    time.sleep_ms(750)  # esperamos al menos 750ms    
    for rom in roms: # leeos los valores disponibles
        temp = ds.read_temp(rom) # leemos el sensor concreto
        print(f' rom: {bRom2str(rom)} temp:{temp}')


def test_all():
    test_DHT22()
    test_all_ds18x20()
    test_I2C()
    test_all_ina219()