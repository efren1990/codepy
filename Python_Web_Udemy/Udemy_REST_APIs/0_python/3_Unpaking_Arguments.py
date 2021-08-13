"""
DESEMPAQUETADO DE ARGUMENTOS
-----------------------------------------------------------------
"""
# Funcion que recibe interminados parametros desempaquetados
def multiply(*args):
	# Imprimir los paramestros recibidos como diccionario a desempquetar
	print(args)
# Llamado de la funciion|
multiply(1, "pp", 54)

# Desempaquetado de lista para parametros de funcion
# funcion
def add(x, y):
	return x + y
# Tambien tenemos famil+
nums = [4, 25]
# Pasar la lista desempaquetada a la funcion
add(*nums)
