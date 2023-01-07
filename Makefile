DIR_PUBLICACION="./publicacion"


S1  = "Tema 1 Introducción a micropython y placas compatibles.docx"
S2  = "Tema 2 Entornos de programación, instalación del firmware de micropython y primeras pruebas.docx"
S3  = "Tema 3 Uso de entradas  y salidas digitales.docx"
S4  = "Tema 4 Trabajando con señales analógicas: ADC y DAC.docx"
S5  = "Tema 5 Módulos y librerías.docx"
S6  = "Tema 6 Conexion a redes.docx"
S7  = "Tema 7 IoT y MQTT.docx"
S8  = "Tema 8 Pantallas gráficas.docx"
S9  = "Tema 9 Creación de modulos micropython.docx"

m = "Programando micro:bit con micropython.docx"


all:  1 2 3 4 5 6 7 8 9 m

m: 
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(m)  \
		Cabecera.md        \
		Cabecera_latex.md \
		1.0.Micropython.md \
		1.6.0.microbit.md \
		1.6.1.microbit_v2.md \
		2.7.0.Instalacion_microbit.md \
		2.7.1.mejora_microbit_v2.md \
		3.1.3.Hello_microbit.md \
		3.2.3.2.led_externo_microbit.md \
		3.2.3.3.microbit_pines.md \
		3.6.2.Botones_microbit.md \
		3.8.2.microbit_touch_v2.md \
		3.9.2.PWM_microbit.md \
		4.2.4.ADC_microbit.md \
		4.5.2.sonido_microbit.md \
		5.12.I2C_microbit_v2.md \
		p.estroboscopio_microbit.md \
		microbit_display_av.md \
		microbit.md \
		microbit_display_basico.md

1:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(S1)  \
		Cabecera.md        \
		Cabecera_latex.md \
		0.0.Presentacion.md \
		0.2.intro.md \
		0.3.Indice.md \
		1.0.Micropython.md \
		1.2.0.Hardware.md \
		1.2.1.PyBoard.md \
		1.2.2.0.ESP32.md \
		1.2.2.1.ESP32-DevKit.md \
		1.2.2.2.WemosD1R32.md \
		1.2.2.3.TTGO_TFT.md \
		1.2.2.4.ESPCAM.md \
		1.2.2.9.ESP32-keyestudio.md \
		1.2.2.10.Adafruit_Feather_Huzzah.md \
		1.2.2.13.STEAMAKERS.md \
		1.2.3.0.ESP8266.md \
		1.2.3.1.WemosD1.md \
		1.2.3.2.NodeMCU.md \
		1.2.3.5.ESP01.md \
		1.3.0.M5Stack.md \
		1.3.1.M5StackCore.md \
		1.3.3.m5StickC.md \
		1.4.Lego_EV3.md \
		1.5.RaspiPico.md \
		1.6.0.microbit.md \
		1.7.0.Sonoff.md \
		1.9.Simulador.md
	

2:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(S2)  \
		Cabecera.md        \
		Cabecera_latex.md \
		2.0.Entornos_e_Instalacion.md \
		2.1.Entornos.md \
		2.2.0.Thonny.md \
		2.2.1.Thonny_install_firmware.md \
		2.2.2.Thonny_uso.md \
		2.3.variables.md \
		2.4.OtrosEntornos.md \
		2.5.0.Install_consola.md \
		2.5.1.Instalacion_ESP32CAM.md \
		2.6.0.Instalacion_raspiPico.md \
		2.7.0.Instalacion_microbit.md \
		2.10.Instalacion_m5stack.md \
		2.11.Actualización.md

3:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(S3)  \
		Cabecera.md        \
		Cabecera_latex.md \
		3.0.0.proyectos_microcontroladores.md \
		3.0.2.Entrada_salida.md \
		3.0.5.Modulos_python.md \
		3.1.0.Hello_Led.md \
		3.1.1.Pines_ESP32.md \
		3.1.2.Hello_led_pico.md \
		3.1.3.Hello_microbit.md \
		3.2.0.ficheros_codigo.md \
		3.2.1.retardos.md \
		3.2.2.bucles.md \
		3.2.3.0.Breadboard.md \
		3.2.3.1.led_externo.md \
		3.2.3.2.led_externo_microbit.md \
		3.2.3.3.microbit_pines.md \
		3.2.4.ficheros_main_boot.md \
		3.3.0.Funciones.md \
		3.3.1.Funciones_argumento.md \
		3.3.2.Funciones_argumento_defecto.md \
		3.4.Colecciones_leds.md \
		3.5.Reles.md \
		3.6.0.buttons.md \
		3.6.1.Button_pullup.md \
		3.6.2.Botones_microbit.md \
		3.6.5.Interrupciones.md \
		3.7.0.condicionales.md \
		3.9.0.PWM.md \
		3.9.1.Efectos_PWM.md \
		3.9.2.PWM_microbit.md \
		3.10.servos.md \
		3.11.controlMotores.md \
		3.13.Leds_RGB.md 		

4:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(S4)  \
		Cabecera.md        \
		Cabecera_latex.md \
		4.0.Señales_analogicas.md \
		4.1.Tipos_formatos.md \
		4.2.0.ADC.md \
		4.2.1.ADC_esp32.md \
		4.2.3.ADC_pico.md \
		4.2.4.ADC_microbit.md \
		4.3.0.SensoresAnalogicos.md \
		4.3.2.Controlando_brillo_led.md \
		4.4.0.Concionales_2.md \
		4.5.0.DAC.md \
		4.5.1.Sonido_avanzado.md \
		4.5.2.sonido_microbit.md \
		4.6.MedidaBateria.md \
		4.7.proyectos.md

5:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(S5)  \
		Cabecera.md        \
		Cabecera_latex.md \
		5.0.0.Modulos.md \
		5.0.1.modulos_os.md \
		5.1.5.f-string.md \
		5.1.Sensores_DHT.md \
		5.2.Excepciones.md \
		5.3.0.I2C.md \
		5.3.1.lcd.md \
		5.6.P.CO2_local.md \
		5.7.ficheros.md \
		5.8.TarjetaSD.md \
		5.9.P.Datalogger.md \
		5.10.1.Neopixels.md \
		5.14.modulos_ESP32.md

6:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(S6)  \
		Cabecera.md        \
		Cabecera_latex.md \
		6.0.Wifi.md \
		6.1.webrepl.md \
		6.2.0.tiempo_hora.md \
		6.2.1.ntp.md \
		6.5.1.Datalogger_V2.md \
		6.6.0.Bluetooth.md \
		6.6.1.Bluetooth_ESP32.md \
		6.7.0.sockets.md \
		6.7.1.socket_mp.md \
		6.7.2.web_request.md \
		6.9.0.webserver.md \
		6.9.1.weberver_ejemplo.md \
		6.9.2.HTML.md \
		6.9.3.web_meteo.md \
		6.9.5.WebServer_control.md

7:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(S7)  \
		Cabecera.md \
		Cabecera_latex.md \
		7.0.IOT.md \
		7.1.0.PlataformasIOT.md \
		7.1.1.ThingSpeak.md \
		7.3.0.MQTT.md \
		7.3.1.MQTT_ejemplo.md \
		7.3.3.AdafruitIO.md \
		7.4.0.ControlRemoto_mqtt.md \
		7.4.1.Control_Adafruit_IO.md \
		7.5.P.CO2_IOT.md 

8:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(S8)  \
		Cabecera.md \
		Cabecera_latex.md \
		8.0.Pantallas.md \
		8.2.0.oled.md \
		8.2.3.OLED_SPI.md \
		8.4.1.TTGO.md \
		8.5.m5stack_ui.md


9:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_micropython.docx \
		-o  $(S9)  \
		Cabecera.md        \
		Cabecera_latex.md \
		9.0.0.micropython.md \
		9.0.1.estructura_codigo.md\
		9.1.compilacion_micropython.md\
		9.3.1.mejorandoVelcidad.md\
		9.3.2.Optimizaciones.md\
		9.9.compilando_porting_micropython.md
		
