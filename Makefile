DIR_PUBLICACION="./publicacion"


S1  = "Tema 1 Introducción a micropython y placas compatibles.docx"
S2  = "Tema 2 Entornos de programación, instalación del firmware de micropython y primeras pruebas.docx"
S3  = "Tema 3 Uso de entrada salida.docx"
S4  = "Tema 4 Medidas analógicas: ADC.docx"
S5  = "Tema 5 Módulos y librerías.docx"
S6  = "Tema 6 Conexion a redes.docx"
S7  = "Tema 7 IoT y MQTT.docx"
S8  = "Tema 8 Pantallas gráficas.docx"
S9  = "Tema 9 Creación de modulos micropython.docx"



all:  1 2 3 4 5 6 7 8 9

1:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(S1)  \
		Cabecera.md        \
		Cabecera_latex.md \
		0.0.0.Presentacion.md \
		0.0.intro.md \
		0.1.Indice.md \
		1.0.Micropython.md \
		1.2.0.Hardware.md \
		1.2.1.PyBoard.md \
		1.2.2.0.ESP32.md \
		1.2.2.1.ESP32-DevKit.md \
		1.2.2.2.WemosD1R32.md \
		1.2.2.3.TTGO_TFT.md \
		1.2.2.4.ESPCAM.md \
		1.2.3.0.ESP8266.md \
		1.2.3.1.WemosD1.md \
		1.2.3.2.NodeMCU.md \
		1.2.3.5.ESP01.md \
		1.3.0.M5Stack.md \
		1.3.1.M5StackCore.md \
		1.3.3.m5StickC.md \
		1.4.Lego_EV3.md \
		1.5.RaspiPico.md \
		1.6.microbit.md \
		1.7.Sonoff.md \
		1.9.Simulador.md
	

2:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(S2)  \
		Cabecera.md        \
		Cabecera_latex.md \
		2.0.Entornos_e_Instalacion.md \
		2.1.Entornos.md \
		2.2.0.Thonny.md \
		2.2.1.Thonny_install_firmware.md \
		2.2.2.Thonny_uso.md \
		2.3.OtrosEntornos.md \
		2.5.0.Install_consola.md \
		2.5.1.Instalacion_ESP32CAM.md \
		2.6.Instalacion_raspiPico.md \
		2.7.Instalacion_microbit.md

3:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(S3)  \
		Cabecera.md        \
		Cabecera_latex.md \
		3.1.Hello_Led.md \
		3.2.ficheros_main_boot.md \
		3.3.Colecciones_leds.md \
		3.4.Funciones.md \
		3.5.Reles.md \
		3.6.0.buttons.md \
		3.6.1.Interrupciones.md \
		3.7.0.condicionales.md \
		3.8.touch.md \
		3.9.PWM.md \
		3.10.servos.md \
		3.11.controlMotores.md \
		3.12.steppers.md \
		3.13.Leds_RGB.md 		

4:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(S4)  \
		Cabecera.md        \
		Cabecera_latex.md \
		4.0.Medidas_analogicas.md \
		4.1.Tipos_formatos.md \
		4.2.ADC.md \
		4.3.SensoresAnalogicos.md \
		4.5.DAC.md \
		4.6.MedidaBateria.md \
		4.7.P.Alumbrado.md

5:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(S5)  \
		Cabecera.md        \
		Cabecera_latex.md \
		5.0.Modulos.md \
		5.10.1.Neopixels.md \
		5.10.2.Neopixel_pico.md \
		5.1.Sensores_DHT.md \
		5.2.Excepciones.md \
		5.3.0.I2C.md \
		5.3.1.lcd.md \
		5.4.tiempo_hora.md \
		5.5.Sensores_atmosfericos.md \
		5.6.P.CO2_local.md \
		5.7.ficheros.md \
		5.8.TarjetaSD.md \
		5.9.P.Datalogger.md \
		5.10.1.Neopixels.md \
		5.10.2.Neopixel_pico.md \
		5.11.Camara_ESP32CAM.md

6:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(S6)  \
		Cabecera.md        \
		Cabecera_latex.md \
		6.0.Wifi.md \
		6.1.webrepl.md \
		6.2.ntp.md \
		6.5.Bluetooth.md \
		6.9.0.weberver.md \
		6.9.1.web_request.md \
		6.9.2.webserve_adv.md

7:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(S7)  \
		Cabecera.md        \
		Cabecera_latex.md \
		7.1.Blynk.md \
		7.3.MQTT.md \
		7.4.AdafruitIO.md \
		7.5.P.CO2_IOT.md \
		7.6.botTelegram.md

8:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(S8)  \
		Cabecera.md        \
		Cabecera_latex.md \
		8.2.oled.md \
		8.3.display.md \
		8.4.TFT.md \
		8.5.Matriz_led.md

9:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(S9)  \
		Cabecera.md        \
		Cabecera_latex.md \
		9.1.Inside_micropython.md \
		9.2.REPL.md \
		9.3.1.mejorandoVelcidad.md \
		9.3.2.Optimizaciones.md \
		9.3.3.OptimizacionMemoria.md \
		9.4.Precompilados.md \
		9.5.CodigoNativo.md \
		9.9.compilando-micropython.md

