"""
FUNCION VARIADICA----------------------------------
Son las que son capaces de recibir una cantidad arbitraria(vairada) de 
parámetros. (Parámetros nombrados y posiciionales)
 def funcion(*args, **kwargs):
 		pass

"""
# Funcion Variadica con paramtros posicionales 
# Permita pasar una cantidad de elementos indeterminados
def lista_de_argumentos(*lista):
	print(lista)
# Llamado de la funcion - retornara la impresion de la lista
lista_de_argumentos(1, 2, 3, 4, 5, 6)
lista_de_argumentos("uno", "dos", "tres", "cuatro")

# Funcion Variadica con parametros asociativos
def lista_de_argumentos_asociativos(**diccionario):
	print(diccionario)
# Llamado de la funcion con argumentos asiciativos - retorna diccionarioc 
lista_de_argumentos_asociativos(a=1, b=2, c=3, d=4)
# Llamado de la funcion varidica asociativa
lista_de_argumentos_asociativos(a="juan", b="alicia", c="carolina", d="andres")

# Funcion varidica con paramtros posicionales y asociativos
# *args -> arguments(tuplas)
# **kwargs -> key words arguments(diccionarios)
def argumentos(*args, **kwargs):
	print(args)
	print(kwargs)
# Llamado de la funcion varidica multiple
argumentos("a", "b", "c", nom="Carolina", ape="Beltran")