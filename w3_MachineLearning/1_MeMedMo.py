###############################################################################################################
#########################################          Sr.Joker          ##########################################
###############################################################################################################
### @NAME: W3 MARCHINE LEARNING PRACTICE
### @CONTENT: Mean, Median and Mode - Media, mediana y moda
#--------------------------------------------------------------------------------------------------------------
"""
#MEDIA, MEDIANA Y MODA
---------------------------------------------------------------------------------------
¿Qué podemos aprender al observar un grupo de números? 
En Machine Learning (y en matemáticas) a menudo hay tres valores que nos interesan:
	#Media: el valor promedio
	#Mediana: el valor del punto medio
	#Moda: el valor más común

Ejemplo: Hemos registrado la velocidad de 13 autos: 
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
"""

"""
#MEDIA
---------------------------------------------------------------------------------------
¿Cuál es el valor de velocidad promedio, medio o más común?

La Media es el valor promedio

Para calcular la media se deve sumar el valor de todas las velocidades
y dividarlas entre la cantidad de velocidadades en el conjunto de datos

(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77
"""
# El modulo NumPy tiene un metodo para esto
import numpy
# Array de velocidades
speeds = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# Calcualar la media con numpy.mean(lista)
media = numpy.mean(speeds)
print('La media es: {}'.format(media))
"""
#MEDIANA
---------------------------------------------------------------------------------------
¿Cuál es el valor de velocidad promedio, medio o más común?

El valor medio es el valor en el medio, después de haber ordenado todos los valores:

77, 78, 85, 86, 86, 86, **87**, 87, 88, 94, 99, 103, 111

Es importante que los números se ordenen antes de que pueda encontrar la mediana.
"""
# Use el método NumPy median () para encontrar el valor medio:
# Array de velocidadades
speeds = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# Calcular la mediana
mediana = numpy.median(speeds)
print("La mediana es: {}".format(mediana))
"""
Si hay dos números en el medio, divida la suma de esos números entre dos.

77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103

(86 + 87) / 2 = 86.5
"""
# Velocidades
speeds = [99,86,87,88,86,103,87,94,78,77,85,86]
# Mediana con dos numeros en el medio
mediana_dos = numpy.median(speeds)
print("Le mediana con 2 numeros es: {}".format(mediana_dos))

"""
#MODA
---------------------------------------------------------------------------------------
¿Cuál es el valor de velocidad promedio, medio o más común?

El valor de Moda es el valor que aparece la mayor cantidad de veces:

99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

El módulo SciPy tiene un método para esto:
"""
# Use el método SciPy mode () para encontrar el número que aparece más:
# Importar Modulo 
from scipy import stats
# Velocidades
speeds = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# Calculo de moda
moda = stats.mode(speeds)
print("La moda es: {}".format(moda))
# El método mode () devuelve un objeto ModeResult que contiene 
# el número de modo (86) y cuenta (cuántas veces apareció el número de modo (3)).