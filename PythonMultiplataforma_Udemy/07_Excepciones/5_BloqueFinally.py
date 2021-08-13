"""
BLOQUE FINALLY
--------------------------------------------------------------------------------
Sub estructra de try que siempre independientemente de lo que suceda tendra su 
bloque de codigo ejecutado.

El bloque finally nos permite ejecutar a nuestro codigo en las peores situaciones

Suponiendo que en la aplicacion un error realmente grave ocurrio sera en esta
parte del codigo en la que implementaremos como es que nuestra aplicacion debera
comportarse ante el mismo

Ya que esta es la unica parte de nuestro codigo de la cual podemos tener la certeza
de que simpre independientemente de lo que suceda sera ejecutado.

Tambien en este bloque sera en el que cerraremos algun archivo abierto o alguna conexion
de red que se encuentre activa.

try:
	#codigo
except ErrorClass1:
	#Codigo Tratamiento
finally:
	#Codigo que siempre se ejecutara se levenaten excepciones o no
	aun si estas excepciones no tienente tratamiento, lo cual se ejecutara
	antes de la finalizacion de la aplicacion

"""
def error(x):
	try:
		eval(x)
	except (ValueError, ZeroDivisionError) as e:
		# Typo de Error
		print(type(e))#Instancia de la Excepcion
	finally:
		print("El bloque finally: Siempre seta ejecutado")

error("5/2")
error("5/0")
error("int('a')")