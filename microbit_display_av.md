## Uso avanzado de la pantalla



### Trabajando con píxeles

También podemos pintar píxeles individualmente usando **display.set_pixel(x,y,brillo)**

```python
from microbit import *

for i in range(5):
     for j in range(5):
        b = (i + j) % 9 # Para asegurar que no superamos el máximo brillo
        display.set_pixel(i,j,b)

```

Donde nos hemos asegurado que no superamos el máximo brillo haciendo módulo 9 (% 9 ) a los valores de brillo, aunque en este caso no se supera.

Si lo preferimos podemos trabajar directamente con los píxeles sobre una imagen con los mismos métodos

Podemos desplazar el contenido de una imagen hacia la izquierda n píxeles con **shift_left(n)** y hacia la derecha con **shift_right(n)**. También hacia arriba con **shift_up(n)** y hacia abajo con **shift_down(n)**. 

Esto nos puede permitir tener una imagen grande en memoria e ir mostrando sólo una parte en la pantalla, algo muy utilizado en los videojuegos, donde el mapa no se muestra completo en pantalla.

También podemos copiar una parte de una imagenSRC, el rectángulo con origen en (xsrc, ysrc) de ancho wsrc y alto hsrc, en las coordeadas (xdest, ydest) de imageDest

imageDest.blit(imagenSRC, xsrc, ysrc, wsrc, hsrc, xdest, ydest)

