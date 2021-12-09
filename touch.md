## Usar los pines como sensores capacitivos (Touch)

El ESP32 nos permite usar algunos de sus pines como sensores capacitivos. En concreto son los pines 0, 2, 4, 12, 13 14, 15, 27, 32, 33.


Para usarlos, definimos un objeto **TouchPad** asociado al correspondiente Pin

```python
import machine

tPad = machine.

```


Y así podemos leer el valor del sensor capacitivo

tpad.read

Obteniendo valores entre 0 y ¿1023?

Para hacerlo más sencillo conectamos un cable suelto al pin

Cuando acercamos la mano a la parte metálica del cable notamos valores menores


También podemos usarlo para despertar la placa del estado **sleep** de bajo consumo


¿SERVIRÍA PARA LEER HUMEDADES?

[Referencia](https://docs.micropython.org/en/latest/esp32/quickref.html#capacitive-touch)

