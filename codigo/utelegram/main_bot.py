
from config import utelegram_config
from config import wifi_config
from config import hardware_config

import utelegram
import network
import utime
import machine

v = 0.8

print(f'Telegram control bot: {v}')

def get_message(message):
    msg_processed = message['message']['text'].lower()
    try:
        
        if msg_processed in hooks.keys():
            hooks[msg_processed](message)
        else:
            print(f'No hook for {msg_processed}')
            bot.send(message['message']['chat']['id'], msg_processed)
    except Exception as e:
        print(f'Error: {e}')
        
def reply_ping(message):
    print(message)
    bot.send(message['message']['chat']['id'], 'pong')

def reply_on(message):
    print('On')
    led.on()
    if hardware_config['rele_inverted']:
        rele.off()
    else:
        rele.on()    
    bot.send(message['message']['chat']['id'], 'On')
 
def reply_off(message):
    print('Off')
    led.off()
    if hardware_config['rele_inverted']:
        rele.on()
    else:
        rele.off()
    bot.send(message['message']['chat']['id'], 'Off')

chat_id = -1

def register_master(message):
    print('Message: ',message)
    username = message['message']['chat']['username']
    if username == utelegram_config['admin']:
        chat_id = message['message']['chat']['id']
        print(f'Chat_id: {chat_id}')
    else:
        print(f'User {username} not allow')
    

hooks ={'on':reply_on, 'off':reply_off, 'record_master':register_master, 'ping':reply_ping}

led = machine.Pin(hardware_config['led'],machine.Pin.OUT)
rele = machine.Pin(hardware_config['rele'],machine.Pin.OUT)


sta_if = network.WLAN(network.STA_IF)
if sta_if.active() == False:
    sta_if.active(True)

print('Connecting to ' + wifi_config['ssid'])
if sta_if.isconnected() == False:
    sta_if.connect(wifi_config['ssid'], wifi_config['password'])

while sta_if.isconnected() == False:
    print('.')
    utime.sleep(1)
print(f'Connected to {wifi_config["ssid"]}')

if sta_if.isconnected():
    print('Registering bot ' + utelegram_config['channel'] + ' ',end='')
    bot = utelegram.ubot(utelegram_config['token'])
    for hook,handler in hooks.items():
        hook = hook.lower()
        if hook[0] != '/':
            hook = '/' + hook
        print(hook,end=' ')
        bot.register(hook, handler)

    print('default ^upper ', end='')    
    bot.set_default_handler(get_message)
    
    print(' refresh time: ', utelegram_config['refresh_time'], ' s')
    bot.set_sleep_btw_updates(utelegram_config['refresh_time'])


    if 'admin_chat_id' in utelegram_config.keys():
        bot.send(utelegram_config['admin_chat_id'],f"Welcome to {utelegram_config['channel']} V{v}")

    print('BOT LISTENING')
    bot.listen()
else:
    print('NOT CONNECTED - aborting')