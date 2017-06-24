#MAKEFILE QUE EJECTUTA ARCHIVO PARA LA CONECCION DE WIIMOTE
version=1
build: linker run

linker: 

run: 
	#ejecuta archivo principal
	python wii_remote_1.py 
clean:
	#archivos eliminados
	rm funcion.pyc wiiclose.pyc
