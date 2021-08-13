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
#El Bucle se Recorre segun la cantidad de elementos dentro de la lista
for i in [1, 2, 3]:
	print("hola");
#por defecto i alamacena los valores de la lista
for i in ["primavera", "Verano", "Otoño", "Invierno"]:
	#4 elemento 4 impresiones
	print("Estamos en " + i);
for i in ["one", "piece", 4]:
	# imprimir en una sola line varios elementos dentro de un bucle
	print("elementos", end=" ");
#En un String el bucle recorre segun la cantidad de caracteres del string
print(" ");
c = 0; 
for i in "palabra":
	c = c + 1;
	print("caracteres: " + str(c));
#Recorriendo strings, evaluando si una  dirrecion de correo electronico
email = False;
myEmail = input("Ingresa tu Email: ");
for i in myEmail:

	if (i == "@"):
		email = True;

if (email == True):
	print("Email Correcto");
else:
	print("Email Incorrecto");	
#Ejercico Email con contador y busqueda de 2 parametros con el for
counter = 0;
myEmail2 = input("Introduce tu email 2: ");

for i in myEmail2:
	
	if (myEmail2 == "@" or myEmail2 == "."):
		# aumento el contador, si llega a estar el arroba o el punto
		counter = counter + 1;
		# si llegan a estar ambas el conador pasara a 2 porque sumara el uno de cada una
		# de las condiciones cumplidas
if (counter == 2):
	print("Email Correcto");
else:
	print("Email Incorrecto");

