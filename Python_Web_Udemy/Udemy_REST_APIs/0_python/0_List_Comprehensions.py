"""
COMPRENSION DE LISTAS
-----------------------------------------------------------------------------
Es una caracteristica de python y nos permite crear nuevas listas
sobre la marcha a partir de listas existentes.
"""
# lista de numeros
numbers = [1, 2, 3, 4, 7, 8]
"""lista nueva insertando un bucle for con la operacion a realizar
dentro del bucle inicialmente y no despues del mismo como se sue realizar
		for num in numbers:
			doubled.append(num * 2)
"""
# LISTA DE COMPRENSION->permite simplificar lineas de codigo
doubled = [num * 2 for num in numbers]
print(doubled)
# Lista de nombres de amigos
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
"""
Se pueden crar bucles y condicionales dentro de una lista de comprension

"""
friend_start_s = [friend for friend in friends if friend.startswith("S")]
print(friend_start_s)