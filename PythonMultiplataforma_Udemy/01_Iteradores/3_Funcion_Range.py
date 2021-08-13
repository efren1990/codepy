"""
FUNCION RANGE EN ITERADORES O BUCLES

Funcion Range->
Regresa una serie numerica en el intervalo enviado.
cuyos elementos contenidos seran generados sobre demanda

Se utiliza todas las veces que se necesite generar una lista
que contiene una serie de numeros dentro de un intervalo determinado

La mayoria de las veces se usa con la instruccion for in
pero no se limita a usarse con el 

range([inicio], [fin, secuencia])
el ultimo elemento definido en el intervalo no sera parte del contenido
es decir el fin
"""
print(type(range(0, 10, 1)))
# Para poder tener el objeto devuelto en range es necesario convertirlo a lista
# lista con intervalos
lista = list(range(0, 10, 2))
print("Range con intervalos:")
print("elemntos range: ", lista)
# El numero 10 no es inculido ya que es un intervalo cerrado

# Otra forma de generar una lista a partir de range
lista2 = list(range(10))
print('Range sin intervalos:')
print("Elementos range: ", lista2)