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
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2
#Una division por 0 genera un numero infinito, lo que genera un error en timpo de ejecucion
def divide(num1,num2):	
	# Maanejo o Control de Excepciones
	try:	
		return num1/num2;
	#si hay un error y no puede ejecutar el try ejecutara el except si el error conicide con el del except	
	except ZeroDivisionError:

		print("No se puede dividir por 0");
		return "Operacion Erronea";


op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")