## Usando la pantalla/display

micro:bit dispone de 25 leds que se pueden utilizar como una pequeña pantalla donde mostrar imágenes, números o textos.

Para mostrar algo en la pantalla usaremos el método **show** por ejemplo números o caracteres: 

```python
from microbit import *
from utime  import sleep

for i in range(5):
    display.show(i)
    sleep(1)
```

Si los números o texto tienen más de un dígito ó carácter, se mostrarán un caracter a la vez:

```python
from microbit import *

display.show(1234567890)

display.show('Hola mundo')
```


También podemos hacer que la información se muestre dislizando los caracteres de izquierda a la derecha por la pantalla, es lo que se conoce como **scroll**

```python
from microbit import *

display.scroll(1234567890)

display.scroll('Hola mundo')
```


Podemos borrar la pantalla con **display.clear()**



### Imágenes


Trabajando con imágenes, con las predefinidas:
ANGRY, ARROW_E, ARROW_N, ARROW_NE, ARROW_NW, ARROW_S, ARROW_SE, ARROW_SW, ARROW_W, ASLEEP, BUTTERFLY, CHESSBOARD, CLOCK1, CLOCK10, CLOCK11, CLOCK12, CLOCK2, CLOCK3, CLOCK4, CLOCK5, CLOCK6, CLOCK7, CLOCK8, CLOCK9, CONFUSED, COW, DIAMOND, DIAMOND_SMALL, DUCK, FABULOUS, GHOST, GIRAFFE, HAPPY, HEART, HEART_SMALL, HOUSE, MEH, MUSIC_CROTCHET, MUSIC_QUAVER, MUSIC_QUAVERS, NO, PACMAN, PITCHFORK, RABBIT, ROLLERSKATE, SAD, SCISSORS, SILLY, SKULL, SMILE, SNAKE, SQUARE, SQUARE_SMALL, STICKFIGURE, SURPRISED, SWORD, TARGET, TORTOISE, TRIANGLE, TRIANGLE_LEFT, TSHIRT, UMBRELLA, XMAS, YES

```python
from microbit import *
display.show(Image.HAPPY)

```

También podemos crear nuestras própias imágenes creando un objeto Image indicándole los valores de brillo de cada pixel, usando el siguiente formato:

```python
miImagen = Image('00000:09090:00000:90009:09990:')
display.show(miImagen)
```
Donde indicamos el nivel de brillo de cada pixel, que estará entre 0 (apagado) y 9 (máximo brillo), con 5 valores para el pixel de cada fila, ordenados por filas, cada una separada por ":" y todo encerrado entre comillas.

Por ejemplo

```python
miImagenEscala = Image('01234:12345:23456:34567:45678')
display.show(miImagenEscala)
```

También podemos crear imágenes con diferente tamaño, pero sólo se mostrará la parte que quepa.

### Colecciones de imágenes

Por defecto tenemos definidas un par de colecciones de imágenes por las que podemos iterar: Image.ALL_CLOCKS o Image.ALL_ARROWS

Podemos mostrar las colecciones también con el método **show** indicando el tiempo entre imágenes con el parámetro **delay**

```python
from microbit import *
display.show(Image.ALL_ARROWS, delay=100)
```

Que sería equivalente a este programa:

```python
from microbit import *
import utime
for i in Image.ALL_CLOCKS:
    display.show(i)
    utime.sleep_ms(100)
```
