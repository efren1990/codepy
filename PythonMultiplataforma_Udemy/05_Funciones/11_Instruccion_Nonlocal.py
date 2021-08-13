"""
INSTRUCCION NONLOCAL
-----------------------------------------------------------
Es la instruccion que permite acceder a miembros no globales y no locales
miembros contenidos en el ambito externo

Sera siempre utilizada cuando se este trabajando con
funciones anidadas

"""
# Funcion General - aplicar nonlocal
def func():
	var_local = 10
	# Funcion anidada
	def func_interna():
		# tomar la variable no local
		nonlocal var_local
		# Sumar a la variable no local
		var_local += 1
		# Imprimir variable
		print(var_local)
	# Llamado de la funcion interna
	func_interna()
# Llamado de la funcion
func()
# Funcion que accede a una variable global
x = 25
def funcGlob():
	# Llamado de la variable global
	global x
	x += 1
	return x
# Llamado de la funcion
print(funcGlob())