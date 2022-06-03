import dht
import machine
import u_ina219
import onewire, ds18x20
import time
import config
import urequests

v = 0.6

def test_DHT22(pin = config.pinDHT):
    dhtsensor = dht.DHT22(machine.Pin(pin))
    try:
        dhtsensor.measure()
        temp = dhtsensor.temperature()
        hum = dhtsensor.humidity()
        print(f'dht22 @ {pin} temp: {temp} C hum: {hum} %')
        return temp, hum
    except Exception as e:
        print(f'DHT Error: {e}')
    

def bRom2str(rom):
    str=''
    for b in rom[1:]:
        sb = ''
        if b<16:
            sb = '0'
        str += sb + hex(b)[2:] + ':'
    return str

def test_all_ds18x20(pin = config.pinDS):
    # from https://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html
    dat = machine.Pin(pin)
    ds = ds18x20.DS18X20(onewire.OneWire(dat))
    roms = ds.scan()
    ts=[]
    print(f'Found {len(roms)} DS Sensors')
    ds.convert_temp() # iniciamos la conversion
    time.sleep_ms(750)  # esperamos al menos 750ms    
    for rom in roms: # leeos los valores disponibles
        try:
            temp = ds.read_temp(rom) # leemos el sensor concreto
            print(f' rom: {bRom2str(rom)} temp:{temp}')
            ts.append(temp)
        except  Exception as e:
            print(f' rom: {bRom2str(rom)} error:{e}')
    return ts

def pubData(field1,field2,field3,field4,field5,field6,field7,field8):
        dict_datos = {'field1':field1, 'field2':field2, 'field3':field3, 'field4':field4, 'field5':field5,'field6':field6,'field7':field7,'field8':field8}
        
        request_headers = {'Content-Type': 'application/json'}

        request = urequests.post(
            'http://api.thingspeak.com/update?api_key=' + config.thingSpeak_api_key,
            json = dict_datos,
            headers = request_headers)
        if request.text == '0':
            print('Error sendinng: ',request.text)
        else:
            print('Published: '+request.text)
        request.close()

def test_all(forever = False):
    devs = u_ina219.init_all(config.pinSDA,config.pinSCL)
    while forever:
        ts = []
        if config.pinDHT>0:
            t,h=test_DHT22()
        if config.pinDS>0:
            ts=test_all_ds18x20()
        data=u_ina219.read_all(devs = devs)
        if len(ts) == 2 and len(data) == 4:
            pubData(t,h,data[0],data[1],ts[0],data[2],data[3],ts[1])
            print('pub data')
        else:
            print(f'Not enough data: ts:{ts} data:{data}')
        if config.DEEP_SLEEP:
            print(f'deepsleep({config.everySeconds*1000})')
            machine.deepsleep(config.everySeconds*1000)