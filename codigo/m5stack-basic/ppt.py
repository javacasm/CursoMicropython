# rock, paper, scissors
from m5stack import *
import utime as time
import random
ROCK = 0
PAPER = 1
SCISSORS = 2

rps_img = (
  'img/rock_128.jpg',
  'img/paper_128.jpg',
  'img/scissors_128.jpg'
)

lcd.clear(lcd.WHITE)

lcd.image(48, 200,  rps_img[0], 2)
lcd.image(143, 200, rps_img[1], 2)
lcd.image(238, 200, rps_img[2], 2)

win_music = (1046,1318,1568,2093)
lose_music = (2093,1568,1318,1046)


def play_music(notes):
  for note in notes:
    speaker.tone(note, 120, 1)

while True:
  rand = random.randint(0, 2)
  lcd.image(lcd.CENTER, 30, rps_img[rand])

  if btnA.isPressed():   # ROCK
    if rand == SCISSORS:
      play_music(win_music)
    elif rand == PAPER:
      play_music(lose_music)
    while not btnA.isReleased(): # Wait for button A release
      pass

  elif btnB.wasPressed(): # PAPER
    if rand == ROCK:
      play_music(win_music)
    elif rand == SCISSORS:
      play_music(lose_music)
    while not btnB.isReleased(): # Wait for button B release
      pass

  elif btnC.wasPressed(): # SCISSORS
    if rand == PAPER:
      play_music(win_music)
    elif rand == ROCK:
      play_music(lose_music)
    while not btnC.isReleased(): # Wait for button C release
      pass
  
  time.sleep(0.02)