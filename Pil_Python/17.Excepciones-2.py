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
#CAPTURA DE VARIAS EXCEPCIONES------>

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2
#Una division por 0 genera un numero infinito, lo que genera un error en timpo de ejecucion
def divide(num1,num2):	
	# Maanejo o Control de Excepciones
	#Usamos un try-except para capturar el error en tiempo de ejecucion y crear un excepcion
	try:	
		return num1/num2;
	#si hay un error y no puede ejecutar el try ejecutara el except si el error conicide con el del except	
	except ZeroDivisionError:

		print("No se puede dividir por 0");
		return "Operacion Erronea";
#Captura del error  si se ingresa algo diferente a un numero
# inicio try
while True:
	try:
		op1=(int(input("Introduce el primer número: ")));
		op2=(int(input("Introduce el segundo número: ")));
		"""Si los valores ingresados son correctos, se leera el break el cual sacara el flujo del 
		bucle sin pasar por el except, esto se debe a que el break esta dentro del try"""
		break;

	except ValueError:

		print("los Valores introducidos no son correctos, Intentalo de nuevo");
	# fin try
# fin bucle
	
"""al capturarse un error el flujo de ejecucion continua, alguna operacion siguiente
#depende de un valor anterio podria generar mas errores y por ende seguir capturando y
crendo demasidas excepciones, por eso es bueno usarlo solo en casos especificos y necesarios"""	
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