"""
FUNCIONES ANIDADAS
---------------------------------------------------------
Las cuales son declaradas en el ambito de otras funciones
es decir dentro de una funcion

"""
# Funcion Externa
def func():
	print("func")
	# Funcion interna(anidada)
	def func_Interna():
		print("func_Interna")
	
	# Llamado de la funcion interna
	func_Interna()

func()