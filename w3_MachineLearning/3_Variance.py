###############################################################################################################
#########################################          Sr.Joker          ##########################################
###############################################################################################################
### @NAME: VARIANCE - VARIANZA ###
### @CONTENT: ###
#--------------------------------------------------------------------------------------------------------------
"""
La varianza mide qué tan dispersos están los datos alrededor de la media.
La varianza es igual a la desviación estándar elevada al cuadrado.

Monitorear la varianza es esencial en las industrias de manufactura y control de calidad,
porque con la reducción de la varianza del proceso aumenta la precisión y disminuye el número de defectos. 
Por ejemplo, una fábrica produce clavos para carpintería que miden 50 mm de largo y un clavo cumple con las 
especificaciones si su longitud no difiere en más de 2 mm del valor objetivo de 50 mm. 
La fábrica utiliza dos tipos de máquina para producir los clavos. 
Ambas máquinas producen clavos con longitudes distribuidas normalmente y una longitud media de 50 mm. 
Sin embargo, los clavos de cada máquina tienen varianzas diferentes: la máquina A,
con la distribución de línea continua en la siguiente figura, produce clavos con una varianza de 9 mm2, 
mientras que la máquina B, con la distribución de la línea de puntos en la siguiente figura, 
produce clavos con una varianza de 1 mm2.
La longitud de los clavos de la máquina A tiene una variación mayor que la longitud de los clavos de la máquina B.
Por lo tanto, cualquier clavo en particular de la máquina A 
tiene una mayor probabilidad de estar fuera de los límites de especificación que un clavo de la máquina B.

"""
"""
#La varianza es otro número que indica qué tan extendidos están los valores.
De hecho, si tomas la raíz cuadrada de la varianza, ¡obtienes la variación estándar! O al revés, 
si multiplica la desviación estándar por sí misma, ¡obtendrá la varianza! 
Para calcular la varianza, debe hacer lo siguiente:
1. Encuentra la media:
	(32+111+138+28+59+77+97) / 7 = 77.4
2. Para cada valor: encuentre la diferencia de la media:
	 32 - 77.4 = -45.4
	111 - 77.4 =  33.6
	138 - 77.4 =  60.6
 	28 - 77.4 = -49.4
 	59 - 77.4 = -18.4
 	77 - 77.4 = - 0.4
 	97 - 77.4 =  19.6
3. Para cada diferencia: encuentre el valor cuadrado:
	(-45.4)2 = 2061.16
 	(33.6)2 = 1128.96
 	(60.6)2 = 3672.36
	(-49.4)2 = 2440.36
	(-18.4)2 =  338.56
	(- 0.4)2 =    0.16
 	(19.6)2 =  384.16
4. La varianza es el número promedio de estas diferencias al cuadrado:
	(2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2
"""
# Libreria numpy
import numpy
# Metodo para calcular la VARIANZA
# Velocidades
speed = [32,111,138,28,59,77,97]
# Calcular la vairanza
variance = numpy.var(speed)
# Imprimir
print("La Varianza es: {}".format(variance))
# Como hemos aprendido, la fórmula para encontrar la desviación estándar es la raíz cuadrada de la varianza:
# √1432.25 = 37.85
print("Variacion estandar: {}".format(numpy.std(speed)))
