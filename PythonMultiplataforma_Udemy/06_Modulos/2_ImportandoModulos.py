"""
IMPRTANDO MÓDULOS
-----------------------------------------------------------------
Importar un módulo es una actividad recurrente cuando estamos 
construyendo una aplicación esto debido a que es normal que
fragmentemos nuestro código como tambien es común que utilicemos
las bibliotecas activas de python y a módulos y paquetes de terceros
por lo tanto para que podamos utilizar a cualquier código que no se
encuentre en el modulo que estamos implementando sera necesario
importarlo.

Importación de módulos es el medio más simple para reutilizar
un código.

La importación de un modulo se realizar utilizando la instrucción import
la cual adiciona el nombre del módulo en la tabla de símbolos local

import nombreModulo  

el módulo importado se ecuentra guardado en el disco como "nombreModulo.py" 

"""
# Importar módulo math(funciones y constates matemáticas), modulo oficial en python
# import adiciona el nombre del módulo a la tabla de símbolos local
import math
# para llamar un simbolo del modulo importado se debe usar el putno (.)
# modulo.simbolo(propiedad,funcion,metodo)
print(math.gcd(45, 195))
# dir() debuelve la tabla de símbolos o nombres en el archivo o módulo
print(dir())
# Constante de Euler
e = math.e
# Constante pi
pi = math.pi
print(e)
print(pi)