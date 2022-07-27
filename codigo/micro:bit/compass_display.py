# Add your Python code here. E.g.
from microbit import *


images_grades = (Image('00900:00900:00900:00000:00000:'), 
                 Image('00090:00900:00900:00000:00000:'), 
                 Image('00009:00090:00900:00000:00000:'),
                 Image('00000:00099:00900:00000:00000:'), 
                 
                 Image('00000:00000:00999:00000:00000:'),                  
                 Image('00000:00000:00900:00099:00000:'), 
                 Image('00000:00000:00900:00090:00009:'), 
                 Image('00000:00000:00900:00090:00090:'), 
                 
                 Image('00000:00000:00900:00900:00900:'), 
                 Image('00000:00000:00900:09000:09000:'), 
                 Image('00000:00000:00900:09000:90000:'), 
                 Image('00000:00000:00900:99000:00000:'), 
                 
                 Image('00000:00000:99900:00000:00000:'), 
                 Image('00000:99000:00900:00000:00000:'), 
                 Image('90000:09000:00900:00000:00000:'), 
                 Image('09000:00900:00900:00000:00000:') )

def showImages():
    for i in images_grades:
        display.show(i)
        sleep(300)

# showImages()

# compass.calibrate()
while True:
    #dir = compass.heading()//45 # convertimos los 360 grados a un número de 0 a 7
    #dir = compass.heading()//30 # convertimos los 360 grados a un número de 0 a 11
    dir = compass.heading()*16//360 # convertimos los 360 grados a un número de 0 a 15
    #display.show(Image.ALL_ARROWS[7-dir]) # están ordenados al revés
    #display.show(Image.ALL_CLOCKS[11-dir]) # están ordenados al revés
    display.show(images_grades[15-dir]) # están ordenados al revés
    print(dir,end = '\r')
    sleep(200)


