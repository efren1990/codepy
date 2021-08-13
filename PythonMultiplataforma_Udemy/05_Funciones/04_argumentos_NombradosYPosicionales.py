"""
ARGUMENTOS NOMBRADOS Y ARGUMENTOS POSICIONALES

►Argumentos Posicionales:
	Es el nombre que se utiliza para el pasaje de valores
	donde cada valor se encotrara en el orden conforme fueron
	declarados en la funcion (en el encabezado)
		Es el envio de una tupla

►Argumentos Nombrados:
	es el nombre que se utiliz para el pasaje de valores
	haciendo asociacion con el nombre del parametro y el valor
	que esta siendo enviado, lo cual no necesitan estar en un orden
	preestablecido
		Es el envio de un diccionario

"""
# Funcion Datos personales
def datosPersonales(nombre, apellido, edad, sexo):
	# Imrpimir datos
	print("Nombre: {}\nApellido: {}\nEdad: {}\nSexo: {}"
				.format(nombre, apellido, edad, sexo))
# Pasar los parametros de forma posicional - los paramtros debe seguir el orden del encabezado
datosPersonales("Cosme","Fulanito", 30, True)
# Pasar los paramtros de forma nombrada, los paramtro no debe seguir un orde
datosPersonales(nombre="Juan", sexo=True, edad=25, apellido="Barajas")
