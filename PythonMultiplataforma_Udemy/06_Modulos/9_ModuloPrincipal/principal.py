"""
EL MÓDULO PRINCIPAL
----------------------------------------------------------------------
Sera el primer archivo de script con código python que sea ejecutado
y recibirá el nombre de __main__(Por deificion de python)

NOTA IMPORTANTE: el nombre de un modulo no debe ser el mismo al de una
								 palabra reservada en python ej: while, if, list, for...
"""
# Importar el modulo
import moduloFunc
# Imprimir el nombre del modulo
print(__name__)
"""
Todos los modulos importados seran llamados como el nombre del archivo
el nombre del archivo inicial sera asignado al archivo que los importa
"""
# Importar Dentro de un directorio sin necesidad de insertar un path
import modulario.subMod

# Varificar el archivo o módulo principal de la aplicacion
if (__name__ == "__main__"):
	print("La aplicación puede ser iniciada")