#---------------------------------------------------#
#Estructuras de Control de flujo(Condicional If-else)
#---------------------------------------------------#
#Ya que python es un lenguaje muy versatil y sencillo
#pero muy poderoso, no existe el switch
#
#OPERADORES LÓGICOS->
#Operadores logicos "and-y" Y "or-o"
#Ejercicio que evaluara si un estudiante obtiene una beca estudiantil o no
#Se evaluara la distancia de vivienda , el salario de los padres y el numero de hermanos
print("Programa de Becas 2018");
# Datos del usuario
# Distancia
distancia = int(input("Introduce la Distancia a el Colegio en Km: "));
print("Distancia A Escuela: " + str(distancia));
# Numero de hermanos
numHermanos = int(input("Introduce el Numero de Hermanos: "));
print("Numero de Hermanos: " + str(numHermanos));
# Salario Padres
salFamiliar = int(input("Introduce Salario Anual Bruto: "));
print("Salario Familiar: " + str(salFamiliar));

# Evalaucion de los Datos con Operador and y or(o si no--en pytho)
if distancia > 40 and numHermanos > 2 or salFamiliar <= 30000000:

	print("Tienes Derecho a una Beca");

else:
	
	print("No tienes Derecho a Becas");	

