"""
EXCEPCIONES
--------------------------------------------------------------------------------
Todo programa por bien construido que se encuentre ira en algun momento
y por las razones mas insolitas a fallar.

Excepción es todo desvío de la regla general, es un objeto cuya clase
a partir de la cual se origino se extiende a partir de la clase
exception.

VALORES INVALIDOS
--------------------------------------------------------------------------------
Cuando se introducen Datos de un tipo, diferente al esperado
Las excepciones deben ser usadas en situciones que se escapen
de lo normal o que no se puedan solucionar con lo contenido basicamente
por el lenguaje.

"""
"""
SITUACION EJERCICIO
---------------------------------------------------------------------------------
Se le pide al usuario que digite 2 numeros para ser divididos
mas sin embargo el usuario quizas inserte datos de diferente tipo al esperado
como strings 
"""
# Funcion para Retornar numeros float, evaluando
# el tipo de dato y retornando mensaje de no ser un numero int o float
def input_float(msg):
	# Bucle while que evalua una excepcion
	while True:
		try:
			# Intenta convertir el dato recivido a .flotante
			# de no ser asi saldra una excepcion, la cuala se evualara
			# en el except, retornando un mensaje y pidiendo nuevamente el numero
			return float(input(msg))
		except ValueError:
			# Mensaje de retorno para tratar la excepcion
			print("Introdusca solo Números.")
		
num1 = input_float("Digite el Número 1: ")
num2 = input_float("Digite el Número 2: ")
# Tratar la excepcion de la division por 0
try:
	print("Resultado: {}".format(num1 / num2))
except ZeroDivisionError:
	print("No es posible dividir por 0")
