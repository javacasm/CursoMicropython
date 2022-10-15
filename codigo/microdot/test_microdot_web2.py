>>> from  requests import get
>>> response = get('http://192.168.1.35/led/25/1')
>>> response = get('http://192.168.1.35/led/25/0')

>>> response = get('http://192.168.1.35/oled/0/0/hola')
>>> response = get('http://192.168.1.35/oled/0/9/oled')
>>> response = get('http://192.168.1.35/oled/0/18/bye')

>>> response = get('http://192.168.1.35/oledclear')

>>> for i in range(0,600,100):
...     response = get(f'http://192.168.1.35/pwm/25/{i}')


>>> for i in range(100):
...     response = get('http://192.168.1.35/led/25/0')
...     response = get('http://192.168.1.35/led/25/1')