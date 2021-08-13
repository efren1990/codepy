#---------------------------------------------------#
#EXCEPCIONES->
#---------------------------------------------------#
"""
►Las Excepciones son errores que ocurren durante
la ejecucion del programa.La sintaxis del codigo
es correcta pero durante la ejecucion ha ocurrido
"Algo inesperado" que el programador no tenia
previsto.

►Este tipo de errores de ejecucion se pueden controlar
para que la ejecucion del programa continue.
Es lo que se le conoce como "Manejo o Control de Excepciones"
"""
# Definicion de una Funcion
def division():
	# Captar errores
	try:
		# Captar num 1
		op1 = (float(input("Introduce el Numero 1: ")));
		# Captar num 2
		op2 = (float(input("Introduce el Numero 2: ")));
		# Imprimir calculo
		print("la Division es: " + str(op1/op2));
		print("Calculo Finalizado");
	# Captura de Multiples Excepciones
	except ValueError:

		print("El Valor introducido es Erroneo");

	except ZeroDivisionError:

		print("No se puede dividir por 0");	
	# finally->Se usa para ejecutarse siempre despues del excepciones(except)
	finally:
		print("El Programa ha FInalizado");
	# Fin try 
		
# Fin Funcion	

# Llamado de Funcion
division();