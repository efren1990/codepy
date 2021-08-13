#---------------------------------------------------#
#Bucles(Estructura de control de flujo)
#---------------------------------------------------#
# BUCLE-> WHILE - INDETERMINADO:
	
	#while condicion:   ->true o false
		
		#Cuerpo del bucle
		#Cuerpo del bucle
		#Cuerpo del bucle
		#Cuerpo del bucle
#En el bucle while, para que se ejecute la condicion tiene que ser verdadera;
#segun lo que se evalue, para que asi se ejecute el bucle
i = 1;
#declaracion del bucle->
#Para que el bucle se ejecute la condicion debe ser verdadera
while (i <= 10):

	print(f"Mientras que i sea menor que 10 ejecutara el bucle: {i} vez");
	# Para salir del bucle se debe cambiar la condicion a falsa para asi salir del bucle o sera
	# un bucle infinito
	i = i + 1;
print("Termino la Ejecucion");

#Programa que pregunta la edad y si es negativa preguntara hasta ingresar un valor negativo
edad = input("Cual es tu Edad: ");
edad = int(edad);
while (edad < 0):
	print("Has introducido una edad negativa,Buelve a Intentarlo");
	edad = int(input("Cual es tu edad: "));
print("Eddad del Aspirante: " + str(edad));	
print("Gracias por colaborar, Puedes pasar");