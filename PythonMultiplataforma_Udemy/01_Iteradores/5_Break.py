"""
INSTRUCCIÓN BREAK
Esta intruccion interrumpe el bloque de ejcucion
del bucle de repeticion en el cual se encuantra 
contenido

►Cada vez que se pueda interrumpir un bloque de ejecucion, se debe hacer,
ya que se economizan recursos de nuestra maquina y tormanamos la aplicacion mas rapida

► Se puede usar con while y for, condicionales
"""
print("Antes de entrar en el bucle")
for item in range(10):
	print(item)
	# Validar la variable 
	# Al ser verdadera la condicion saldra del bucle debido al break
	if(item == 6):
		print("Interrumpiendo el bucle")
		break
print("Despues del bucle")
