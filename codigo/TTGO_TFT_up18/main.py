
import time
import os

v = 0.1

print(f'{os.uname()}')

start = time.ticks_ms() 
import mini_tetris
end = time.ticks_ms()

print(f'init: {(end-start)/1000} segundos')
start = time.ticks_ms() 
mini_tetris.full()
end = time.ticks_ms() 

print(f'fill tiles {(end-start)/1000} segundos')

nLines = 1000
start = time.ticks_ms() 
mini_tetris.randomLines(N=nLines)
end = time.ticks_ms() 

print(f'{nLines} lines {(end-start)/1000} segundos')