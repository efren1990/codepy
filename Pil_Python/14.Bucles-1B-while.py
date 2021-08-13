#---------------------------------------------------#
#Bucles(Estructura de control de flujo)
#---------------------------------------------------#
# BUCLE-> WHILE - INDETERMINADO:
#Ejercicio para evaluar edades usando un bucle while
edad = int(input("Introduce tu edad: "));
while (edad < 5) or (edad > 100):
	print("La edad es incorrecta, vuelve a Intentarlo...");
	edad = int(input("Introduce tu edad: "));
