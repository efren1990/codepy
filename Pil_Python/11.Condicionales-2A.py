#---------------------------------------------------#
#Estructuras de Control de flujo(Condicional If-else)
#---------------------------------------------------#
# Ejercicio de Notas--->
#Se usa float(para transformar en decimales)--int(para transformar en enteros)
nota_Alumno = float(input("Introduce tu Nota: "));

if nota_Alumno < 5:

	print("Insuficiente");

elif nota_Alumno < 6:

	print("Suficiente");

elif nota_Alumno < 7:

	print("Bien");

elif nota_Alumno < 9:

	print("Notable");

else:

	print("Sobresaliente");

print("El Programa ha Finalizado");