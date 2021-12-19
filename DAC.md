# DAC 

[Referencia](https://www.reddit.com/r/esp32/comments/nkha5c/is_there_any_function_in_micropython_to_use_dac/gzd4v19/)


Están en los pines 25 y 26 GPIO

Tenemos 256 niveles (8 bits)

>>>
MPY: soft reboot
MicroPython v1.15 on 2021-04-18; ESP32 module with ESP32
Type "help()" for more information.
>>> from machine import DAC,Pin
>>> dac = DAC(Pin(25))
>>> dac.write(128)
>>>

[C source](https://github.com/micropython/micropython/blob/a9bbf7083ef6b79cf80bdbf34984d847a6c4aae9/ports/esp32/machine_dac.c)


Ejemplo 1: Led


Medimos con un voltímetro

Ejemplo 2: sonido




Diferencia con PWM

¿Osciloscopio para ver la diferencia?

ejemplo con bucle

DAC: Onda de sierra

## Referencias

https://hackaday.io/project/176774-simple-esp32-sd-audio-player-internal-dac-pdm

[Ejemplo para m5Stack](https://m5stack.hackster.io/lukasmaximus89/play-wav-files-on-your-m5stack-3bee7e)

[Ejemplo para pyBoard](https://docs.micropython.org/en/latest/pyboard/tutorial/amp_skin.html)
