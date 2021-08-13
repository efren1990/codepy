 #---------------------------------------------------#
#Estructuras de Control de flujo(Condicional If-else)
#---------------------------------------------------#
#Ya que python es un lenguaje muy versatil y sencillo
#pero muy poderoso, no existe el switch
#
#OPERADORES IN->
#Operador in

#Ejercicio donde el estudiante de una carrera escojera una asignatura que se le ofrece en el listado
print("Asignaturas Optativas Año 2018: ");
print("a.Informatica Grafica - b.Pruebas de Software - c.Usabilidad y Accesibilidad");

# Variables
opcion = input("Escribe la Asignatura escogida: ");
# Nota-> Python es case Sensitive lo que quiere decir que distingue entre mayusculas y minusculas
		#lower()->pasa a minusculas
		#upper()->pasa a mayuscula
asignatura = opcion.lower();

# in Valida si el dato en la variable asignatura esta en los parentesis del in()
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura);
	print("Felicitaciones, A Seleccionado Su asignatura");
else:
	print("La Asignatura no esta en la Lista");

