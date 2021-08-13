###############################################################################################################
#########################################          Sr.Joker          ##########################################
###############################################################################################################
### @NAME: PERCENTILES ###
### @CONTENT: ###
#--------------------------------------------------------------------------------------------------------------
"""
#¿Qué son los percentiles?
	Los percentiles se usan en las estadísticas 
	para darle un número que describe el valor por el cual 
	un porcentaje dado de los valores es menor.

#Ejemplo: Digamos que tenemos una serie de edades de todas las personas que viven en una calle.
	
	ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
	¿Cuál es el percentil 75? 
	La respuesta es 43, 
	lo que significa que el 75% de las personas tienen 43 años o menos.
"""
# El módulo NumPy tiene un método para encontrar el percentil especificado:
import numpy
# Edades
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# Calculo del percentil =  numpy.percentile(lista, percentilACalcular)
percen = numpy.percentile(ages, 75)
# impresion
print("El percentil es: {}".format(percen))
"""
En estadística, un percentil es una medida de posición no central, 
al igual que los cuartiles, los deciles o los quintiles.

Todas esas medidas nos informan de la posición de un valor respecto a los demás. 
Si un valor está en el cuartil 3 (Q3), indicaría que tres cuartas partes de los datos 
son igual o menores que ese valor.

El concepto de percentil es igual pero referido a porcentajes. 
Si un valor tiene un percentil 55 (P55), el 55% de los demás datos 
tendrán un valor igual o más pequeño.

Imaginemos que la altura de un grupo de personas es el conjunto de datos a estudiar. 
Si una altura de 1.75 m está en el P80 (percentil 80), quiere decir que 
el 80% de las personas del grupo mide 1.75 o menos.

Veamos unos ejemplos para entenderlo mejor:

#Ejemplo 1: 
	los datos son la nota de los alumnos de una clase. 
	Si un alumno tiene un 9.5 y está en el percentil 85, significa que 
	el 85% de los alumnos tiene un 9.5 o menos.

#Ejemplo 2: 
	si tomamos los sueldos de 10.000 trabajadores. 
	¿Cuál sería el percentil 60? 
	El P60 sería aquel sueldo por debajo del cual estaría el 60% de los trabajadores. 
	Si ordenamos los trabajadores desde el que cobra menos hasta el cobra más, 
	el P60 sería el sueldo del trabajador número 6000 (60% de 10000).

Ejemplo 3: 
	medimos el tiempo que marcan los atletas de una competición en recorrer una cierta distancia. 
	¿Cuánto tiempo tardan en recorrer esta distancia el 45% de los corredores? 
	La respuesta es el percentil 45. 
	La idea es simple, se ordenan las medidas de menor a mayor y se toma la que hay en la posición del 45%.

Fórmula para calcular percentiles

Para calcular los percentiles, 
1-primero hay que ordenar los datos de forma ascendente.
2-Una vez ordenados, se resta 0.5 a la posición que ocupa el dato del que queremos calcular el percentil. 
3-Después dividimos entre el número total de datos y multiplicamos por 100.

Ejemplo
Tenemos un conjunto de 47 datos con diferente valores que van desde 51 hasta 99. 
Si queremos saber el percentil al que pertenece el valor 63, primero ordenamos de menor a mayor y miramos la posición que ocupa e6 63. 
Supongamos la posición es 12.

Aplicamos la fórmula:

P = ( (12 – 0.5) / 47) x 100 = 24.46

Y obtenemos que el 63 está en el percentil 24.46 indica, 
es decir, que el 24.46% de los datos tienen un valor de 63 o menos. 
Esto se indica como P24.46 = 63.

"""
# ¿Cuál es la edad que tiene el 90% de las personas más jóvenes?
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# Percentil
percen = numpy.percentile(ages, 90)
# Output
print("El percentil es: {}".format(percen))