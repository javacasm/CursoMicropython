# DAC 

[Referencia](https://www.reddit.com/r/esp32/comments/nkha5c/is_there_any_function_in_micropython_to_use_dac/gzd4v19/)


>>>
MPY: soft reboot
MicroPython v1.15 on 2021-04-18; ESP32 module with ESP32
Type "help()" for more information.
>>> from machine import DAC,Pin
>>> dac = DAC(Pin(25))
>>> dac.write(128)
>>>

[C source](https://github.com/micropython/micropython/blob/a9bbf7083ef6b79cf80bdbf34984d847a6c4aae9/ports/esp32/machine_dac.c)