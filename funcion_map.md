Hasta donde yo sé no hay una función "map" en micropython, pero  es fácil de implementar, ya que no es nada más que una regla de proporcional, un escalado de valores, con un rango de entrada (in_min, in_max) y un rango de salida (out_min, out_max), convirtiendo "valor" que está en el rango inicial en una "valor_escalado" comprendido en el rango de salida

```python
def my_map(valor, in_min, in_max, out_min, out_max):
 valor_escalado = (valor - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 return valor_escalado
 ```