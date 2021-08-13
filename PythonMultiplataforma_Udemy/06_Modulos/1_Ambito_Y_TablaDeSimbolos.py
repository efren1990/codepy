"""
ÁMBITO Y TABLA DE SÍMBOLOS
------------------------------------------------------------------------------------
La tabla de símbolos es un diccionario de datos es decir de símbolos perteneciente
al ámbito global del modulo, todo modulo posee su propia tabla y la misma puede contener
0 o n símbolos algunos símbolos son adicionados a la tabla por python y los otros van siendo
adicionados por cada nueva variable declarada, por cada nueva funcion o cada nueva clase imple
mentada.

Un símbolo o nombre es cualquier declaración, ya sea una variable, funcion, clase, etc.

Todo archivo de python es por definición un módulo
"""
# Una funcion no puede acceder a los ámbitos globales
# Las funciones poseen una tabla de símbolos propia
def func():
	# Imprimir el nombre de la funcion
	print(__name__)

# Todo lo creado en el nivel 0 de identacion esta en el ámbito global del modulo
a = 4
# list() -> es una funcion builtins 
l = list()
func()