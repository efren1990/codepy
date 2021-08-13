# Importo la Libreria math para poder usar funciones matematicas como raiz,factoriales, etc
import math 
#---------------------------------------------------#
#Bucles(Estructura de control de flujo)
#---------------------------------------------------#
# BUCLE-> WHILE - INDETERMINADO:
"""Programa que hallara la raiz cuadrada de un numero
para hacer comentarios multiples su usa la 3ple comilla
"""
# Titulo
print("Programa de Calculo de Raiz Cuadrada");
# Efecto linea baja
marco = "Programa de Calculo de Raiz Cuadrada ";
for i in marco:
	print("=", end="");
print(" ");
# Numero
numero = int(input("Introduce tu Numero: "));
# Variable para intentos
intentos = 0;
while (numero < 0):
	print("No se puede hallar la raiz de un numero negativo....");
	
	if (intentos == 2):
		print("Has acabado tus intentos");
		#para finalizar un bucle se usa break
		break;
	
	numero = int(input("Introduce tu Numero: "));
	# Aumentar el contador para los numeros negativos los cuales se tomaran como intentos fallidos
	if 	numero < 0:
		intentos = intentos + 1;
#End while


"""Si los intentos del usuario no son menores que dos, quiere
decir que ha introducido un numero positivo por ende el programa
procedera al mostrar la raiz cuadrada de numero"""

if (intentos < 2):
	#objeto math metodo sqrt que saca la raiz cuadrada 
	solucion=math.sqrt(numero)
	# Imprimir la solucion
	print("Raiz cuadrada de: "+ str(numero) + " Es: " + str(solucion));
else:
	print("Lo Sentimos has fallado....");