#xxxxxx------------------------------------------------------------->
#Paquetes Redistribuibles
#xxxxxx------------------------------------------------------------->
##LLamado del PAquete->
"""
Son paquetes que creamos, distribuimos, instalamos, para asi luego
llamarlos desde cualquier lugar del ordenador donde se alamacene el archivo
que llama el modulo o pquete

lo que sehace es instalar el paquete dentro del propio python del sistema
operativo

1-Se debe crear un archivo en la raiz de la carpeta llamado
	setup.py
	el cual contendra una descripcion del paquete que vamos
	a distribuir, debe contener->
	Nombre del paquete, descripcion, version, autor, fechas, etc

Para instalar el paquete se debe ingresar por consola o por consola
power shell a la ruta donde esta el archivo setup y escribir
					(instruccion)        (nombreArchivo)  (instruccion)
RutaArchivoConsola>     python             setup.py           sdist

al haber hecho esto
se crearn dos carpetas 
1.dist->de distribucion donde estara un archivo con extension nombreArchivo.tar.gz
		el cual contendra el paquete redistribuible para instalar en la maquina
		o pasar a mas personas
2.nombrePaquete.egg-info->dentro estara la informacion del paquete

para instalar el paquete hay que entrar a la ruta por consola
donde esta la carpeta dist creada del paquete
y usar la instruccion

►rutaCarpetaDistConsola> pip3 install nombrePaquete.tar.gz

"""
#uso del modulo redistribuible creado el cual esta dentro de la carpeta Paquetes/
#submodulo redonde_potencia/modPotRedon.py
#llamado del paquete, la diferencia es que se podra llamar desde cualquier carpeta del ordenador
from Paquetes.redondeo_Potencia.modPotRedon import *
potencia(45,2);