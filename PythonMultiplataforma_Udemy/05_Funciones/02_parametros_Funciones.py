"""
PARÁMETROS DE FUNCIÓN-------------------------------------
Parámetro es una variable declarada entre los paréntesis
de una función.
	
	def miFuncion(paramtro1, parametro2, paramtro3, etc...):
		bloque de código
"""
# Funcion con parametros 
def miFuncion(nombre, apellido):
	print("Hola, "+nombre+" "+apellido)
# Llamado de la funcion pasando los argumentos
miFuncion("Cosme", "Fulanito")

# Funcion para sumar dos numeros
def suma(x, y):
	#	Declaracion de una variable local dentro de la funcion
	total = x + y
	print("Total: "+str(total))
suma(10, 45)
# Una funcion puede ser llamada las veces que se requiera
suma(150, 125)
