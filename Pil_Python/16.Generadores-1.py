#---------------------------------------------------#
#GENERADORES->
#---------------------------------------------------#
#QUE SON ?->
"""
►Son estructuras que extraen los valores de una funcion y se almacenan
en objetos iterables(que se pueden recorrer)
►Estos Valores se almacenan de uno en uno
►Cada vez que un generador almacena un valor, este permanece en un estado pausado
hasta que se solicita el siguiente. Caracteristica conocida como "Suspension de Estadp"
"""
#FUNCIONAMIENTO->
"""#los generadores se pueden comprar con funcines tradicionales solo que en vez
	de usar un return se usa la intruccion yield

	Funcion Tradicional                      Generador
	def funcionNamero():					def funcionNamero():					
		return dato								yield dat
"""

#UTILIDAD->
"""
►Son mas Eficientes que las funciones tradicionales
►Muy utilies con listas de valores infinitos
►Bajo determinados escenarios, sera muy util que un generador devuelva valores de uno en uno
"""
