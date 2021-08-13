"""
ARCHIVO DE HELPERS
-----------------------------------------------------------------------
Archivo para crear funciones de ayuda
"""
# Funcion que recibe como parametro una fecha
def date_format(date_f):
	# Tupla para meses del año
	months = ("Enero", "Febrero", "Marzo", "Abril", 
						"Mayo", "Junio", "Julio", "Agosto", 
						"Septiembre", "Octubre", "Noviembre", "Diciembre")
	# Calcular el mes [fecha.month = Retorna numero de 1 a 12 - 1 = devuelve la posicion en el array monts]
	month = months[date_f.month - 1]
	# Retornar el mes formateado
	return "{} de {} del {}".format(date_f.day, month, date_f.year)