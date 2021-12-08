## Bajo consumo

¿Por qué usarlo?

Tipos

En el ESP32 se hace un reset del que se volverá pasada el tiempo indicado

deepsleep(milisegundos)

Para saber el motivo del último reset

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')



Problema: si lo alimentamos con powerbanks, como muchos de ellos se apagan si no detectan consumo, al entrar en ESP32 en bajo consumo se apagan....

[Documentación](https://docs.micropython.org/en/latest/esp32/quickref.html#deep-sleep-mode)

