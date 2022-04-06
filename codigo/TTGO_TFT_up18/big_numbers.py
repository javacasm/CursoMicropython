from machine import Pin, SPI
import st7789
import time

v =0.6

numbers = ( ( '###',
              '# #',
              '# #',
              '# #',
              '###') ,
            ( ' # ',
              ' # ',
              ' # ',
              ' # ',
              ' # '),
            ( '###',
              '  #',
              '###',
              '#  ',
              '###'),
            ( '###',
              '  #',
              '###',
              '  #',
              '###'),
            ( '#  ',
              '# #',
              '###',
              '  #',
              '  #'),
            ( '###',
              '#  ',
              '###',
              '  #',
              '###'),
            ( '#  ',
              '#  ',
              '###',
              '# #',
              '###'),
            ( '###',
              '  #',
              '  #',
              '  #',
              '  #'),
            ( '###',
              '# #',
              '###',
              '# #',
              '###'),
            ( '###',
              '# #',
              '###',
              '  #',
              '  #'))

bigFont_WIDTH = 3
bigFont_HEIGHT = 5

tft_width = 135
tft_height = 240

spi = SPI(1, baudrate=30000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(19))
tft = st7789.ST7789(
     spi,
     tft_width,
     tft_height,
     reset=Pin(23, Pin.OUT),
     cs=Pin(5, Pin.OUT),
     dc=Pin(16, Pin.OUT),
     backlight=Pin(4, Pin.OUT),
     rotation=0)
tft.rotation(1)
tft.init()

def printBig(number):
    u = number % 10
    d = number // 10
    print(f'{number} = {d}{u}')
    for i in range(5):
        print(numbers[d][i] +' ' + numbers[u][i])
  
  
def showBigDigit(digit,x,y,color,width,height,border):
    # printBig(digit)
    py = y
    for i in range(bigFont_HEIGHT):
        px = x
        for c in numbers[digit][i]:
            # print(px,py,c)
            if c == '#':
                tft.fill_rect(px,py,width-1,height-1,color)
                if border:
                    tft.rect(px,py,width-1,height-1,st7789.WHITE)
            px  += width                
        py += height
                
                   
  
def showBig(number,x,y,color,width=10,height=10,border = False):
    u = number % 10
    d = number // 10

    if d>0:
        showBigDigit(d,x,y,color,width,height,border)
    showBigDigit(u,x + bigFont_WIDTH * width+5,y,color,width,height,border)
 
 
def testBi(color = st7789.BLUE):
    for i in range(100):
        showBig(i,0,0,color,width=25,height=25)
        time.sleep(0.2)
        tft.fill(st7789.BLACK)
        
        
    