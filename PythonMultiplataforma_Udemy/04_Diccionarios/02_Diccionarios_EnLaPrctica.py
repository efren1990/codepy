"""
#DICCIONARIOS EN LA PRACTICA 
---------------------------------------------------------------------
Diccionarion - Estructura clave - valor
	donde la clave no puede repetirce es unica y puede ser cualquier objeto
	inmutable
represnetado por { }
diccionario = {}
"""

d = dict()
print(type(d))
# Agregar un elemento al diccionario 
# dic[clave] = valor
d['a'] = 10
d['b'] = 20
d['c'] = 30
print(d)
# Otra forma de declarar un diccionario
dic = {'a':10, 'b':15}
print(dic)
# Otra forma de declarar diccionarios
versiones = {1.0:'radeon', 2.0:'colkip', 2.5:'colkipper', 3.0:'randerz-x'}
print(versiones)
print("Version del Kernel:",versiones[1.0])

