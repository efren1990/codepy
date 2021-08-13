#---------------------------------------------------#
#Estructuras de Control de flujo(Condicional If)
#---------------------------------------------------#
#Programa con entrada por teclado
print("Programa de Evaluacion de Notas de Alumnos");
# Pedir un valor por teclado-> input()
notaAlumno = input("Introduce la Nota del Alumno: ");
# Esto generara un error ya que la comparacion en el if se hara de
# un int con un string ya que pyton considera la entrade del teclado
# como string para esto se debe->usar int(texto a transformar en valor numerico entero)

def evaluacion(nota):
	#variable valoracion
	valoracion = "aprobado";
	# Inicio del if
	if nota < 5:
		# Codigo a Ejecutar
		valoracion = "se Rajo";
	# Retorno de datos Funcion	
	return valoracion;
# LLamado de la Funcion
print( evaluacion(int(notaAlumno)) );