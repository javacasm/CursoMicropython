# Versiones de ESP: ESP8266/ESP32/ESP32-S2/ESP32-S3/ESP32-C3/ESP32-C6

Cada sistema ESP tiene unas características y prestaciones distintas, algunas más potentes y otras simplificadas.

Hay que tener en cuenta que una cosa son las características del procesador y otra las que el fabricante de la placa pone accesibles en las patillas/pines. Por ello es necesario comprobar la documentación del fabricante del procesador y de nuestra placa

Veamos una tabla comparativa de los distintos sistemas ESP

|  |ESP8266|ESP32 | ESP32-S2| ESP32-S3| ESP32-C3 | ESP32-C6   	|
|----|----	|----	|----	|----	|----	|----	|
| Fecha de creación  |Agosto 2014 | Septiembre 2016 |Septiembre 2019  	| Diciembre 2020|Noviembre 2020| Abril 2021|
| Procesador   	| Tensilica L106 32-bit (hasta 160MHz) 	| Tensilica Xtensa 32-bit LX6 (hasta 240MHz) (optionalmente dual core) 	| Tensilica Xtensa 32-bit LX7 (hasta 240MHz)  	| Tensilica Xtensa 32-bit LX7 dual core (hasta 240MHz) 	| RISC-V 32-bit (hasta 160MHz) 	| RISC-V 32-bit (hasta 160MHz) 	|
| SRAM  | 160KB | 520KB | 320KB  | 512KB   	| 400KB   	| 400KB   	|
| ROM  	| 0 | 448KB | 128KB  | 384KB   	| 384KB   	| 384KB   	|
| JTAG    	| X   	| ✓     	| ✓    	| ✓    	| ✓    	| ✓    	|
| Cache | 32 KB instrucciones| 64KB	| 8/16KB (configurable)	| ?| 16KB|?|
|WiFi|Wi-Fi 4 (hasta 72.2Mbps)| Wi-Fi 4|Wi-Fi 4|Wi-Fi 4|Wi-Fi 4|Wi-Fi 6|
|Bluetooth|X|BLE 4.2 (parcialmente 5.0)|X|BLE 5.0 | BLE 5.0  | BLE 5.0 |
| Ethernet   	| X   	| ✓     	| X    	| ?    	| X    	| ?    	|
| RTC memory 	| 768B | 16KB | 16KB | 16KB    	| 8KB     	| ?    	|
| PMU  	| ✓   	| ✓     	| ✓    	| ✓    	| ✓    	| ?    	|
| ULP coprocessor| X| ✓|ULP-RISC-V 	| ✓    	| X    	| ?    	|
| Cryptographic Accelerator | X	| SHA, RSA, AES, RNG   	| SHA, RSA, AES, RNG, HMAC, Digital Signature 	| SHA, RSA, AES, RNG, HMAC, Digital Signature 	| SHA, RSA, AES, RNG, HMAC, Digital Signature 	| SHA, RSA, AES, RNG, HMAC, Digital Signature 	|
| Secure boot   	| X   | ✓     	| ✓    	| ✓    	| ✓    	| ✓    	|
| Flash encryption|X|✓|XTS-AES-128/256|✓|XTS-AES-128| XTS-AES-128 |
| SPI  	| 2   	| 4     	| 4    	| 4    	| 3    	| ?    	|
| I2C  	| 1   	| 2     	| 2    	| 2    	| 1    	| ?    	|
| I2S  	| 1   	| 2     	| 1    	| 2    	| 1    	| ?    	|
| UART | 2 (solo 1 TX)| 3   | 2    	| 3    	| 2    	| ?    	|
| SDIO Host | 0   	| 1     	| 0    	| 2    	| 0    	| 0    	|
| SDIO Slave| 0   	| 1     	| 0    	| 0    	| 0    	| 0    	|
| GPIO    	| 17  	| 34    	| 43   	| 44  	| 22   	| 22   	|
| LED PWM   | 5   	| 16    	| 8    	| 8    	| 6    	| ?    	|
| MCPWM   	| 0   	| 6         | 0    	| 2    	| 0    	| 0    	|
| Contador de pulsos 	| 0 | 8  | 4    | 4  	| 0    	| X    	|
| GDMA  	| 0   	| 0     	| 0    	| 5    	| 6    	| ?    	|
| USB  	| X | X | USB OTG 1.1 | USB OTG 2.0 |Serial/JTAG   	| ?    	|
| TWAI  	| 0   	| 1     	| 1    	| 1    	| 1    	| ?    	|
|ADC|1x 10-bit SAR|2x 12-bit SAR, hasta 18 canales|2x 13-bit SAR, hasta 20 canales|2x 13-bit SAR, hasta 20 canales| 2x 12-bit SAR, hasta 6 canales|?    	|
| DAC  	| X   	| 2x 8-bit    	| 2x 8-bit | X	| X    	| X    	|
| RMT  	| 1x transmisión + 1x recepción 	| 8x transmisión/recepción| 4x transmisión/recepción    	| ?    	| 2x transmisión + 2x recepción  	| ?    	|
| Timer|2x 23-bit***|4x 64-bit|4x 64-bit|?| 2x 54-bit + 1x 52-bit|?|
| Sensor de Temperatura   	| ✓   	| ✓     	| ✓| ? | ✓ | ? |
| Hall Sensor | X | ✓  | X | ? | X | ?  |
| Touch Sensor| 0   	| 10    	| 14   	| ?    	| X    	| ?    	|

Todos los procesadores tienen DMA pero si no está marcado es que no está accesible para el usuario

*** Uno de los temporizadores está dedicado al Wi-Fi, con lo que no está accesible al usuario.

Más detalles de modelos específicos y variantes en [Espressif Product Selector](https://products.espressif.com/).

