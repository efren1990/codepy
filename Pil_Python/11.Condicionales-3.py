#---------------------------------------------------#
#Estructuras de Control de flujo(Condicional If-else)
#---------------------------------------------------#
#Ya que python es un lenguaje muy versatil y sencillo
#pero muy poderoso, no existe el switch
#
#OPERADORES DE COMPARACION->
#En python se pueden concatenar los operadores de comparacion
# Lo que nos permite evaluar muchas condiciones encadenadas

# Evaluacion de la edad correcta
edad = 7;
# se verifica si la edad es menor que 0 para los numeros negativos o mayor que 100
if 0 < edad < 100:
	#el flujo de ejecucion en el if es de izquierda a derecha por ende se evalua si es menor que 0
	# y despues si es mayor que 100 
	print("La edad es Correcta");
else:
	print("Edad incorrecta");

#Evaluacion del salario en una empresa 
#python al ser fuertemente tipado hace distincion en tipos de datos
salPresidente = int(input("Introduce salarion presidente: "));
#No se puede concatenar un string con un int por ende se transforma el int a string
print("Salario presidente: " + str(salPresidente));

salDirector = int(input("Introduce salario Director: "));
print("salario Director: " + str(salDirector));

salJefe_Area = int(input("Introduce salario jefe de Area: "));
print("salario jefe de Area: " + str(salJefe_Area));

salAdministrativo = int(input("Introduce Salario Administrativo: "));
print("Salario Administrativo: " + str(salAdministrativo));

# Condicional con operadores de comparacion concatenados-->
#Se evalua si los salarios son correctos del menor al mayor
if salAdministrativo < salJefe_Area < salDirector < salPresidente:

	print("Los salarios son Correctos");

else:

	print("Los Salarios son incorrectos");

