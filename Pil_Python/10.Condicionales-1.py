#---------------------------------------------------#
#Estructuras de Control de flujo(Condicional If)
#---------------------------------------------------#
#El flujo de ejecucion de un programa es el 
#orden con el que se ejecutan sus intrucciones
# flujo-> de Arrbia a Abajo 
# El if evalua si una condicion es verdadera o falsa
#Si es es verdadera ejecuta una accion
#Si es falsa no ejecuta el condicional if y sigue el flujo de ejecucion
# Creo una funcion para evaluar con un if una nota ingresada
def evaluacion(nota):
	#variable valoracion
	valoracion = "aprobado";
	# Inicio del if
	if nota < 5:
		# Codigo a Ejecutar
		valoracion = "se Rajo";
	# Retorno de datos Funcion	
	return valoracion;	
print(evaluacion(5));	
print(evaluacion(2));
