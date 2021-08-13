#---------------------------------------------------#
#Bucles(Estructura de control de flujo)
#---------------------------------------------------#
"""CONTINUE, PASS, ELSE:

►continue->Salta a la siguiente iteracion de bucle cuando se lee en
		   el interior de un bucle

►pass-> devuelve null en cuanto se lee en el interior del bucle,
		es decir devuelve null, como si no se leyera el bucle.

►else-> en un bucle funciona igual que en un condicional
"""
#►CONTINUE:----------->
for letra in "python":
	if letra == "h":
		# cuando se encuentre con la h el continue salta a la siguiente vuelta de bucle
		continue;
	print("Viendo la letra: " + letra);
#Ejercicio
nombre = "Pildoras DimetilTriptamina";
# len()->Devuele la longitud del string
print(len(nombre));
contador = 0;
for i in nombre:
	if i == " ":
		continue;
	contador+=1;
print("Letras Reales: " + str(contador));

#►PASS:----------->Devuelve un null lo que pone a la espera el bucle, funcion o clase;
# while True:
# 	pass;
	#Evitara que el bucle se ejecute

#►ELSE:----------->
email = input("Introduce tu email: ");

for i in email:
	if i == "@":

		arroba = True;
		#el break rompe el flujo de ejecucion del bucle for y saldra del mismo sin ejecutar el else
		break;
else:#El else en el for, while, o do while, se ejecutara siempre y cuando el bucle este vacio
#Es decir cuando ya halla completado todas sus vueltas de bucle;
	arroba = False;
	
print(arroba);