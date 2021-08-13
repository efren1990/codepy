###############################################################################################################
#########################################          Sr.Joker          ##########################################
###############################################################################################################
### @NAME: W3 MACHINE LEARNING PRACTICE###
### @CONTENT: STANDARD DEVIATION - DESVIACION ESTANDAR###
#--------------------------------------------------------------------------------------------------------------
"""
#¿Qué es la desviación estándar?
	La desviación estándar es un número que describe la distribución de los valores.
	Una desviación estándar baja significa que la mayoría de los números están cerca del valor medio (promedio).
	Una desviación estándar alta significa que los valores se extienden en un rango más amplio.
Ejemplo: esta vez hemos registrado la velocidad de 7 autos:
	speed = [86,87,88,86,87,85,86]
La desviacion estandar es
	0.9
Lo que significa que la mayoría de los valores están dentro del rango de 0.9 del valor medio, que es 86.4.
"""
# El módulo NumPy tiene un método para calcular la desviación estándar:
import numpy
# Velocidades
speed = [86,87,88,86,87,85,86]
# Media
media = numpy.mean(speed)
# Desviación estandar
des = numpy.std(speed)
# Desviacion estandar baja - indica que los numeros estan mas cerca de la media
print("La media es: {} y su Desviacion estandar es: {}".format(media, des))
"""
La desviación estándar es la medida de dispersión más común, que indica qué tan dispersos están los datos con respecto a la media. 
Mientras mayor sea la desviación estándar, mayor será la dispersión de los datos.

El símbolo σ (sigma) se utiliza frecuentemente para representar la desviación estándar de una población, 
mientras que s se utiliza para representar la desviación estándar de una muestra. 
La variación que es aleatoria o natural de un proceso
se conoce comúnmente como ruido.

La desviación estándar se puede utilizar para establecer un valor de referencia 
para estimar la variación general de un proceso.
"""
# EJEMPLO DE DESVIACION ALTA
speed = [32,111,138,28,59,77,97]
# Media
media = numpy.mean(speed)
# Desviacion estandar
des = numpy.std(speed)
# Desviacion estandar alta
print("La media es: {} y su Desviacion Estandar es: {}".format(media, des))
