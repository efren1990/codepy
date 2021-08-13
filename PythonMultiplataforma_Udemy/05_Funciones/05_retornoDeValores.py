"""
RETORNO DE VALORES
El objetivo de toda funcion es el procesamiento de informacion 
y el retorno de los datos procesados
por ende toda funcion puede retornar valores
usando la palabra reservada, return
"""
# Usando return para retornar un valor por una funcion
def numero():
	return 10
# Invocar la funcion
print(numero())

# Funcion con parametros
def suma(num1, num2):
	total = num1 + num2
	# return tambien es responsable de finalizar las funciones
	return total

# Llamado de la funcion
print(suma(10, 50))

