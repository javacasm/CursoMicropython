# Ejemplo de uso de camara ESP-CAM
# https://github.com/lemariva/micropython-camera-driver
# from @lemariva

v = '0.8.4'

print(f'test_camera v{v}')
import camera
import time
import uos
import machine
from config import *

bCameraInitted = False
bSDInitted = False

def initCamera(resolution=camera.FRAME_VGA):
    global bCameraInitted
    if not bCameraInitted:
        print('Inicializando camara')
        camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
# ALL the options are the following:
# FRAME_96X96 FRAME_QQVGA FRAME_QCIF FRAME_HQVGA FRAME_240X240
# FRAME_QVGA FRAME_CIF FRAME_HVGA FRAME_VGA FRAME_SVGA
# FRAME_XGA FRAME_HD FRAME_SXGA FRAME_UXGA FRAME_FHD
# FRAME_P_HD FRAME_P_3MP FRAME_QXGA FRAME_QHD FRAME_WQXGA
# FRAME_P_FHD FRAME_QSXGA
# Check this link for more information: https://bit.ly/2YOzizz      
# For ESP32-CAM: FRAME_VGA FRAME_XGA
        print('Resolución:',str(resolution))
        camera.framesize(resolution)
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
    
def flash(value = True):
    led = machine.Pin(app_config['led'], machine.Pin.OUT)
    if value:
        led.on()
    else:
        led.off()
        
def getPicture(f=False,res=camera.FRAME_VGA):
    initCamera(resolution=res)
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


def borrarImagenes(filename,basedir = '/sd/pics'):
    initSD()
    uos.chdir(basedir)
    files = uos.listdir()
    for file in files:
        if filename in file:
            uos.remove(file)
            print('borrado',basedir+'/'+file)
        else:
            print(filename,'not in',file)
            
def borraFichero(filename = 'image.jpg'):
    uos.remove(filename)