"""
TRATAMIENTO DE EXCEPCIONES MULTIPLES
--------------------------------------------------------------------------------
Python con la instruccion :
try:

except:

except:

Permite definir el tratamiento para cuantas excepciones
sean necesarias, sin embargo la levantarse una excepcion
solo un unico bloque except puede ser ejecutado como maximo

"""
# Funcion para Errores
def error(x):
	try:
		# Evalua y ejecutas expresiones corretas en python eval("Exrepsion")
		# Suele usarse para detectar errores
		eval(x)
	# Se pueden tratar varias excepciones en un mismo except
	except (TypeError, NameError):
		print("TypeError o NameError")
	except ValueError:
		print("ValuerError")
	except ZeroDivisionError:
		print("ZeroDivisionError")
# Levantamiento de Excepciones con eval()
# implementada en la funcion error()
# TyperError -> Error de tipos, somar dos tipos de datos
error("int+int")
# NameError -> variable no definida
error("a")
# ValueError -> Cuando ocurre algun problema con algun valor que se esta pasando como parametro
error("int('a')")
# ZeroDivisionError -> cuando se intenta dividir por 0 
error("5/0")
