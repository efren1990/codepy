"""
DESEMPAQUETAMIENTO II
----------------------------------------------------
Como funciona el desempaquetamiento.
"""
# EJEMPLO 1
print("----------EJEMPLO 1----------")
lista = [11, 10, 12]
# Funcion que desempaquera la lista
def func(a, b, c):
	print(a)
	print(b)
	print(c)
# Ordenar la lista - de menor a mayor
lista.sort()
# Llamar la funcion
func(*lista)
# EJEMPLO 2
print("----------EJEMPLO 2----------")
# Funcion que desempaquetara la lista que sera primero una tupla
tupla = (11, 13, 10, 12)
def funcB(a, b, c, d):
	print(a)
	print(b)
	print(c)
	print(d)
# Ya que la tupla es inmutable no se puede Ordenar
# para esto se desempaqueta la tupla convirtiendola en una lista
l = [*tupla]
# Ordenar la lista
l.sort()
# pasar la lista a la funcion y desempaquetarla
funcB(*l)
# EJEMPLO 3 - USANDO ZIP
print("----------EJEMPLO 3----------")
# Funcion zip - toma 2 listas como parametro y retorna un diccionario
func(**dict(zip(("b", "a", "c"), lista)))
