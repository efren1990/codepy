"""
ETAPAS DE LA IMPORTACÓN
------------------------------------------------------------------------
Módulos implementados en python son analizados e interpretados en el 
momento de la importación.

El módulo puede ser ejecutado despues de ser importado

Despues de la primera importación el unico evento que tendra lugar
las proximas veces que este modulo sea importado sera la adicion del
nombre del modulo o de algun otro nombre a la tabla de símbolos local

ETAPAS:
1-LOCALIZACIÓN: 
	El path, las rutas

2-COMPILACIÓN: 
	En el momento de la importacion de los módulos python ira a compilar
	e ira a generar un archivo en el mismo directorio cuyo nombre sera
	.pyc esta extencion hace referencia a .pythoncompilado

3-EJECUCIÓN: 
	Se debe entender como ejecución a funciones que son invocadas, variables
	que son declaradas o instancias que son creadas en el ámbito global.

"""
# Como Ver el bitecode 
def func(l):
	print("Hellouses jajajaj")
# Importar modulo dis contiene funcion dis() la cual muestra el bite code
import dis
# pasar la funcion func para ver su bitecode
dis.dis(func)