#---------------------------------------------------#
#METODOS STRING->
#---------------------------------------------------#
"""
Metodos para manipular cadenas de caracteres
Python, considera a las cadenas de caracteres objetos
METODOS MAS UTILIZADOS->

►upper()->Convierte en mayusculas el string.

►lower()->Pasa a minusculas un string

►capitalize()->Pone la primera letra en mayusculas en un string

►count()->cuenta cuantas veces aparece una letra o una cadena de
de caracteres, grupo de letras, dentro de una frase o otro string

►find()->Representa la posicion[indice] de un caracter o grupo de caracteres
dentro de un texto o string

►isdigit()->devuelve un boolean, dice si el valor introducido es un digito
es un valor numerico o no

►isalum()->comprueba si es alfanumerico

►isalpha()->comprueba si hay solo letras, sin espacios

►split()->separa por palabras utilizando espacios

►strip()->borra los espacios sobrantes al comienzo y al final del string

►replace()->cambia una palabra o letra por otra en un string

►rfind()->representa el indice de un caracter desde el final del string reverse
 
y muchos mas...

"""
# Upper---------------------------------------------------------->
nomUs = input("Introduce un Nombre de Usuario: ");
print("El Nombre con upper es: ", nomUs.upper());
# lower---------------------------------------------------------->
print("El Nombre con lower es: ",nomUs.lower());
# capitalize----------------------------------------------------->
print("El Nombre con capitalize es: ",nomUs.capitalize());
# isdigit----------------------------------------------------->
#devuelve un booleano: True o False si es digito o no
print("Es digito(Numero)?: " + str(nomUs.isdigit()));

#Ejercicio de Strings
# Todo lo introducido en un input es considerado un string
edad = input("Introduce tu edad: ");
# Comprobar si lo ingresado es un numero o no
while (edad.isdigit() == False):
	print("Por Favor introduce tu edad en numeros...");
	# Pedir la edad de nuevo
	edad = input("Introduce tu edad: ");
	#Se saldrda del bucle si lo ingresado es un numero
#validar Mayoria de edad
if ( int(edad) < 18):
	print("No puedes Pasar, Mocoso...");
else:
	print("Puedes pasar");