# Ejemplo de uso de camara ESP-CAM
# https://github.com/lemariva/micropython-camera-driver
# from @lemariva

v = '0.7.3'



import camera
import time
import uos
import machine
from config import *

bCameraInitted = False
bSDInitted = False

def initCamera():
    global bCameraInitted
    if not bCameraInitted:
        print('Inicializando camara')
        camera.init(0, format=camera.JPEG)
        print('Tamaño a  Frame_VGA')
        camera.framesize(camera.FRAME_VGA)
        '''
        # special effects
        camera.speffect(camera.EFFECT_NONE)
        # The options are the following:
        # EFFECT_NONE (default) EFFECT_NEG EFFECT_BW EFFECT_RED EFFECT_GREEN EFFECT_BLUE EFFECT_RETRO

        # white balance
        camera.whitebalance(camera.WB_NONE)
        # The options are the following:
        # WB_NONE (default) WB_SUNNY WB_CLOUDY WB_OFFICE WB_HOME

        # saturation
        camera.saturation(0)
        # -2,2 (default 0). -2 grayscale 

        # brightness
        camera.brightness(0)
        # -2,2 (default 0). 2 brightness

        # contrast
        camera.contrast(0)
        #-2,2 (default 0). 2 highcontrast

        # quality
        camera.quality(10)
        # 10-63 lower number means higher quality
        '''
    bCameraInitted = True
    
def initSD():
    global bSDInitted
    if not bSDInitted:
        sd = machine.SDCard(slot=3, width=1, 
            sck=machine.Pin(microsd_config['sck']),
            mosi=machine.Pin(microsd_config['mosi']),
            miso=machine.Pin(microsd_config['miso']),
            cs=machine.Pin(microsd_config['ss']))
        uos.mount(sd, '/sd')
        uos.listdir('/')
        bSDInitted = True
    
def flash(value):
    led = machine.Pin(app_config['led'], machine.Pin.OUT)
    if value:
        led.on()
    else:
        led.off()
        
def getPicture(f=False):
    initCamera()
    initSD()
    
    try:
        print('Capturando')
        flash(f)
        buf = camera.capture()
        flash(False)
        print(f'Capturado {len(buf)}')
        
        fileName='/sd/pics/image_'
        for v in time.localtime():
            fileName+=str(v)
        fileName+='.jpg'
        f = open(fileName,'w')
        print(f'Escribiendo {fileName}')
        written = f.write(buf)
        print(f'{written} bytes  written in {fileName}')
        f.close()
        print('Terminado!!')
    except Exception as e:
        print(e)
        print(buf)
    flash(False)

def borraFichero():
    import os
    os.remove('image.jpg')