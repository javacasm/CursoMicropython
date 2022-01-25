DIR_PUBLICACION="./publicacion"


S1  = "Tema 1 Introducción a micropython.docx"
S2  = "Tema 2 Entornos de programación y primeras pruebas.docx"
S3  = "Tema 3 Uso de entrada salida.docx"
S4  = "Tema 4 Medidas analógicas: ADC.docx"
S5  = "Tema 5 Módulos y librerías.docx"
S6  = "Tema 6 Conexion a redes.docx"
S7  = "Tema 7 IoT y MQTT.docx"
S8  = "Tema 8 Pantallas gráficas.docx"
S9  = "Tema 9 Creación de modulos micropython.docx"



all:  1 2 3 4 5 6 7 8 9 10 11 12 CB

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
		1.1.Como_funciona.md \
		1.2.0.Hardware.md \
		1.2.1.DevKit.md \
		1.2.2.PyBoard.md \
		1.2.3.ESP01.md \
		1.2.4.ESPCAM.md \
		1.2.5.WemosD1R32.md \
		1.2.6.0.M5Stack.md \
		1.2.6.1.M5StackCore.md \
		1.2.6.2.m5stackCore2.md \
		1.2.6.3.m5StickC.md \
		1.2.7.WemosD1.md \
		1.2.8.NodeMCU.md \
		1.2.11.TTGO_OLED.md \
		1.2.12.Wemos_Battery.md \
		1.2.13.LOLIN32.md \
		1.2.14.TTGO_TFT.md \
		1.2.15.TTGO_Lora.md \
		1.3.Sonoff.md \
		1.4.Lego_EV3.md \
		1.5.RaspiPico.md \
		1.7.VersionesMicropython.md \
		1.9.Simulador.md
