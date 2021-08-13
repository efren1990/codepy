#xxxxxx------------------------------------------------------------->
#LLamado de los Paquetes Contenedores de Modulos en Pyton
#xxxxxx------------------------------------------------------------->
##LLamado del PAquete->
"""
from nombreCarpeta.NombreArchivoModulo import Funcion,clase,etc->a llamar

from nombreCarpeta.NombreArchivoModulo import * -> llama todo lo contenido
en el archivo

►Se pueden creaar carpetas dentro de la carpeta principal del paquete
estas carpetas denben contener adentro tambien el archivo __init__.py

►Para llamar modulos dentro de paquetes que estan dentro de paquete
es decir carpetas dentro de carpetas con archivos modulares
se debe:

from nomCarpeta.nomCarpete... import * O clase,funcion etc....
"""
from Paquetes.basicos.modOpBasicas import *
from Paquetes.redondeo_Potencia.modPotRedon import *
sumar(24, 45);
restar(25487, 456897);
sumar(245.25, 458.69);
potencia(5, 25);



