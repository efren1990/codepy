import math
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
#LANZDO DE EXCEPCIONES A VOLUNTAD->
#Ej->Programa para evaluar edad
def evaEdad(edad):
#Lanzar una excepcion de forma intencionada cuando el valor de al edad sea negativo
	if edad < 0:
		# raise lanza una excepcion del tipo especificado y podemos agregar un mensaje
		raise TypeError("No se Permiten Edades Negativas");
	if edad < 20:
		return "Eres muy Joven...";
	elif edad < 40:
		return "Eres Joven...";
	elif edad < 65:
		return "Estas Viejo...";
	elif edad < 100:
		return "Vas Colgandolos...";
# fin Funcion
print(evaEdad(18));

#Ej2->Programa para hallar raiz cuadrada(importo clase math)
def calRaiz(num):
	 if num < 0:
	 	raise ValueError ("El Numero no puede ser negativo");
	 else:
	 	return math.sqrt(num);

op1=int(input("Introduce el Numero: "));
# Capturar el Error
try:
	print(calRaiz(op1));
	#as agrega un alias al error
except ValueError as ErrorDeNumeroNegativo:
	#impresion del error con nombre alias
	print(ErrorDeNumeroNegativo);

print("Programa Terminado");