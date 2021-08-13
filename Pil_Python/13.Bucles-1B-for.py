#---------------------------------------------------#
#Bucles(Estructura de control de flujo)
#---------------------------------------------------#
# BUCLE-> FOR - DETERMINADO:
	#for varible in elemento a recorer:
		#cuerpo del bucle(codigo)
		#cuerpo del bucle(codigo)
		#cuerpo del bucle(codigo)
		#cuerpo del bucle(codigo)
#elemento a recorrer->El cual puede ser una lista,tupla,texto,rango
#USO DEL RANGE EN EL FOR->
# El range funciona como el contador de un bucle for de otros leguajes
# El range se toma como un tipo de dato.
#range(5)->devuelbe 5 valores del 0 al 4 0,1,2,3,4
for i in range(5):

	print(i);
for i in range(6):
	#Otra forma de concatenar diferentes tipos de datos es:
	#usando f(funcion por defecto)->la cual permite jugar con formatos de forma diferente
	#Se debe ubicar el dato diferente al string entre corchetes
	print(f"Valor de la Variable: {i}");

#El dato tipo range permite poner rangos de positivos o negativos, de un valor a otro(un rango)
#Rango de un valor a otro
for r in range(5,10):
	print(f"Rango desde 5 hasta 9: {r}");
#Rango de un valor a otro con un incremento especificado
for s in range(1,50,5):
	print(f"Rango con Incremento: {s}");
#}
# validando un Email con range y len(se usa para contar los caracteres de un string)
valido = False;
email = input("Introduce tu Email: ");
	
for i in range(len(email)):
	
	if (email[i] == "@"):

		valido = True;

if (valido == True):
	print("EL email es correcto");
else:
	print("El email es Incorrecto");
