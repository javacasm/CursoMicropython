# from https://github.com/jordiprats/micropython-utelegram

from config import utelegram_config
from config import wifi_config
from machine import Timer


import utelegram
import network
import utime
import dht
import machine

v = 0.3

debug = True

dht5=dht.DHT22(machine.Pin(5))

def init_wifi():
    print('Init wifi')
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.active():
        sta_if.active(True)
    # sta_if.scan()
    if not sta_if.isconnected():
        sta_if.connect(wifi_config['ssid'], wifi_config['password'])
        print(f'Connecting to {wifi_config["ssid"]}')
        while not sta_if.isconnected():
            utime.sleep(1)
            print('.',end='')


def sendPeriodicUpdate(value):
    dht5.measure()
    msg = f'Temp: {dht5.temperature()}'
    print(msg)
    if lastID != -1:
        bot.send(lastID,'hola! '+msg)
        
lastID = -1

def get_message(message):
    lastID = message['message']['chat']['id']
    bot.send(message['message']['chat']['id'], message['message']['text'].upper())

def reply_ping(message):
    print(message)
    bot.send(message['message']['chat']['id'], 'pong')

def init_timer():
    print('Init timer')
    tim0 = Timer(0)
    tim0.init(period=5000, mode=Timer.PERIODIC, callback=sendPeriodicUpdate)

bot = None
def init_bot():
    global bot
    print('Init bot')
    bot = utelegram.ubot(utelegram_config['token'])
    bot.register('/ping', reply_ping)
    bot.set_default_handler(get_message)

    print('BOT LISTENING')
    bot.listen()
    
init_wifi()
init_timer()
init_bot()