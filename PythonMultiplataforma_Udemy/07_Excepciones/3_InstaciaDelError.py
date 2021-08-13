"""
CAPTURANDO LA INSTACIA DEL ERROR
--------------------------------------------------------------------------------
Cada vez que se genera un error este es tomado como una
clase de error la cual  da como resultado una instacia delo objeto de error
que fue levantado.
Una clase es definida para representar a cada error especifico

Toda clase de error se extiende a partir de la clase Exception la cual
representa el tope de la jerarquia de errores

Cuando se levanta una Excepcion generalmente se define en su instancia
algunos mensajes adicionales en relacion al problema que ocasiono al error
python permite acceso a estas opciones

Capturar la instancia 
try:
	#codigo
except: ErrorClass1 as variable:
	#Tratamiento

"""
def error(x):
	try:
		eval(x)
	except (ValueError, ZeroDivisionError) as e:
		# Typo de Error
		print(type(e))#Instancia de la Excepcion
		# Mensaje de error
		print(e.args)#Argumentos o mensajes
		# Valor de la variable interna de la clase
		print(e)#__str__menssage

error("5/0")
error("int('a')")
