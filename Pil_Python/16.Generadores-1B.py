#---------------------------------------------------#
#GENERADORES->
#---------------------------------------------------#
#Uso de yield from->
"""Simplificar el codigo del generador en el caso
de utilizar bucles anidados
	def miGenerador():
		yield elementos	
Los elementos pueden ser: listas, diccionarios, tuplas, etc...
"""
# Funcion generador que devuelve un serie de ciudades
""" (*ciudades)->el asterisco antes del parametro de la funcion quiere decir
que va a recibir un numero indeterminado de elementos, ademas que esos
 elementos los va a recibir en forma de tupla
"""
def devCiudades(*ciudades):
	# For para recorrer el paremtro de la funcion
	for elemento in ciudades:
		# #for anidado
		# for subElement in elemento:
		# 	#generador
		# 	yield subElement;
		# generador que evita hacer un bucle anidado para acceder dentro del elemento y
		# Extraer su sub elementos en este caso las letras de cada palabra
		yield from elemento;
# fin funcion

ciudades_Devueltas = devCiudades("Madrid", "Barcelona", "Bilbao", "Valencia");
# Devolver las dos primeras ciudades
# Devuelve 1
print(next(ciudades_Devueltas));
# Devuelve 2
print(next(ciudades_Devueltas));
# Acceder a cada una de las letras que forma el elemento
