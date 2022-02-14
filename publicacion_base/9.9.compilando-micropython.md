# Proceso de compilación de micropython

En este caso vamos a hacerlo para la placa meowbit de kittenbot

Descargamos el código 

git clone https://github.com/KittenBot/micropython_meowbit.git

Preparamos la compilación

cd micropython_meowbit/mpy-cross/
make

Descargamos los módulos de los que dependen

git submodule update --init


Necesitamos instalar con compilador cruzado (cross-compiler) para la CPU que vamos a usar. En mi caso para smt32, necesitamos descargar los compiladores de arm https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads

Descomprimimos en /usr/share

sudo tar xvf ~/Descargas/gcc-arm-none-eabi-10.3-2021.10-x86_64-linux.tar.bz2 -C /usr/share/

Los hacemos accesibles en el Path

sudo ln -s /usr/share/gcc-arm-none-eabi-10.3-2021.10/bin/arm-none-eabi-* /usr/bin/

Probamos

arm-none-eabi-gcc --version
arm-none-eabi-g++ --version

Vamos al directorio de nuestra plataforma

cd ports/stm32/

y lanzamos la compilación

make
