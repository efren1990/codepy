"""
DESEMPAQUETAMIENTO I
------------------------------------------------------------------
Empaquetar = Es adicionar un conjunto de valores a una lista
						 decir que que existe valores empaquetados es decir
						 que tenemos a una estructura de tipo lista, tupla o 
						 diccionario que contiene valores.

Desempaquetar = Es la extraccion de los elementos contenidos de una
								estructura (tupla,list,diccionario) utilizando a una notacion de la sintaxis del
								lenguaje					

"""
# Ejemplos de Desempaquetamiento
# Funcion para desempaquetar
def persona(nombre, apellido, edad):
	# Imprimir los valores
	print(nombre)
	print(apellido)
	print(edad)
# Tupla de valores
tupla = "eXcript", "Brasil", 20
# Pasar valor a valor tupla--------------------------------------------
persona(tupla[0], tupla[1], tupla[2])
# Pasar la tupla desempaquetada----------------------------------------
persona(*tupla)
# Lista para desempaquetar
lista = ["Rayzor", "x", 34]
# Pasar lista a la funcion para desempaquetar
persona(*lista)
# Diccionario para desempaquetar---------------------------------------
di = {"nombre":"ReNdlli", "apellido":"canicas", "edad":18}
# pasar el diccionarion a la funcion
persona(**di)