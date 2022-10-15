# Errores frecuentes


## detección de la placa

Entra en el administrador de dispositivos y mira a ver si te sale un dispositivo desconocido en la parte de puertos serie.

Si no es así puede ser que el cable USB sea de datos, prueba con otro

## sensores DHT
Ese es un error de lectura del sensor, que no responde a la petición de lectura en un tiempo determinado y por eso da TimeOUT. Posibles causas:

* No están bien conectada, es decir hay un error en la conexión de las patillas.
* Error en el programa, porque has usado un pin que no es el adecuado
* Los cables no hacen buen contacto con la protoboard, cambia los cables o muévelo a otra posición en la protoboard.
* Estás intentando medir demasiado rápido, deja al menos 1 segundo entre medidas.
* El sensor se ha estropeado. Son muy sensibles y si lo has conectado con la polaridad invertida te lo has cargado.

## Problemas de conexión con la placa:

* Prueba a apagarla y luego encenderla, no reset sino quitando la alimentación.
* Comprueba que tu sistema operativo detecta el puerto al conectar la placa 
* Los cables USB son muy traicioneros, cambia por otor
* Comprueba que el puerto está bien seleccionado
* Si usas Thonny, pulsa el botón rojo
* Abre y cierra tu IDE
* Reinicia tu ordenador


## Wifi y conexión a través de internet

* La placa está conectada al wifi (eso no se hace en este código)
* Tu wifi tiene conexión con Internet
* Pudiera ser que te diera un error puntual de conexión
