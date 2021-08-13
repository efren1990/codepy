"""
LAMBDA FUNCTIONS- Funciones lambda
-----------------------------------------------------------------
una funcion lambda es un tipo diferente de funcion que no tiene
nombre y solo se usa para devolver valores
"""
# Üna funcion sencilla
def suma(c, f):
	return c + f 
print(suma(2, 5))
# La misma funcion pero lambda se debe asignar a una variable para darle un nombre
suma_l = lambda c, f: c + f
print(suma_l(4, 96))
# Para no asignar nombre a la funcion se debe ejecutar en linea
print((lambda x, y: x - y)(24, 5))