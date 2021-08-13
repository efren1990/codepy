"""
IMPOSTANDO SÍMBOLOS
---------------------------------------------------------------------------
La importación de símbolos copia atributos de un módulo directamenta a la
tabla de símbolos local.
Lo mas frecuente es importar a los símbols ya que es la manera mas optima de
trabajar

Importar uno o más símbolos o nombres
# form modulo import símbolo1, símbolo2

Renombrar el módulo (as)-alias
# import modulo as M

Renombrar Símbolo
# from modulo import simbolo as s

Renombrar Varios Símbolos
# from modulo import simbolo1 as s1, simbol2 as s2

Formas Alternas de importar símbolos
# import modulo
# simbo = modulo.simbolo

Importar todos los símbolos de un modulo
# from modulo import *
►	Una practica no aconsejable que si se importan todos los símbolos de uno o mas modulos
	las aplicaciones se tornaran lentas, debido a que el interprete le tomara mas tiempo
	buscar un nombre en la tabla de simbolos.
	
"""
# Importar el modulo math, simbolos pi y euler
from math import pi, e
# Importar la funcion que calcula la raiz cuadrada
from math import sqrt
# Impirmir pi y euler
print(pi)
print(e)
# raiz cuadrada de 3
print(sqrt(9))

# IMPORTAR DENTRO DE UNA FUNCIÓN
def func():
	# Importar función factoria
	from math import factorial
	print(factorial(10))
# LLamado de la funcion
func()