import machine, os
try:
    sd = machine.SDCard(slot=3, miso=19, mosi=23, sck=18, cs=4)
    sd.info()
    os.mount(sd, '/sd')
    print("SD card mounted at \"/sd\"")
except:
    pass