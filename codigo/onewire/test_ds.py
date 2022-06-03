import machine
import onewire, ds18x20
import time
import config


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
    if len(roms)>0:
        print(f'Found {len(roms)} DS Sensors')
        ds.convert_temp() # iniciamos la conversion
        time.sleep_ms(2500)  # esperamos al menos 750ms    
        for rom in roms: # leeos los valores disponibles
            try:
                temp = ds.read_temp(rom) # leemos el sensor concreto
                print(f' rom: {bRom2str(rom)} temp:{temp}')
                ts.append(temp)
            except  Exception as e:
                print(f' rom: {bRom2str(rom)} error:{e}')
    else:
        print('No ds sensors')
    return ts
