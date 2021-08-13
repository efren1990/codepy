"""
FOR Y RANGE
Se suelen usar conjutos amenudo
"""
# Definir un range transformado a lista
lista = list(range(15))
print(lista)
# Definir una lista con intervalos
listaInt = list(range(0, 100, 10))
print(listaInt)
# Definir una lista con intervalos pero de forma inversa
listaInver = list(range(100, 0, -10))
print(listaInver)
# Definir una lista con numeros negativos con intervalos de 10 en 10
listaNeg = list(range(-100, 0, 10))
print(listaNeg)
"""
Uso conbinado de for y range
"""
for i in range(10):
	print("Rango: ", i)
	
# For con range e intervalos numericos
for i in range(-10, 0, 1):
	print("Rango: ", i)
 