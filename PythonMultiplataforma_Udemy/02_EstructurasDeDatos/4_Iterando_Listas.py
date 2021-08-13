"""
ITERANDO LISTAS-------------------------------------------------------------
Como recorrer una lista
"""
# CASO 1:-----------------------------------------
# Recorrer una lista con for in
lista_num = [100, 200, 300, 400]
# Usar for in para recorrer lista
for numero in lista_num:
	# la variable numero pasar a alamacenar cada elemento de la lista
	print("Elemento lista: " + str(numero))

# CASO 2:---------------------------------------
# Recorrer lista y manipular los items de la lista
lista_num_II = [100, 200, 300, 400, 500]
# No se pueden atribuir valores a la variable temporal del for in 
# para esto debemos acceder al item a travez del indice
# Para acceder al indice necesitamos un contador que sea una lista con el numero de indices correcto
lista_indice = [0, 1, 2, 3]
for indice in lista_indice:
	# modificar items de la lista en recorrido
	lista_num_II[indice] += 1000
# Impresion lista modifica
print(lista_num_II)

# CASO 3:-----------------------------------------
# Usar range para crear los indices de la lista
lista_nume = [5, 10, 20, 30, 40]
lista_indi = range(4)
for indice in lista_indi:
	lista_nume[indice] += 1000
# Impresion de la lista
print(lista_nume)

for indice in range(4):
	print("Elemento: " , lista_nume[indice]);

# CASO 4:-------------------------------------------
# Usar range en la misma lista para obtener los indices
lis_numeros = [10, 20, 30, 40, 50]
# for
for indice in range(4):
	lis_numeros[indice] += 1000
# Impresion
print(lis_numeros)

# CASO 5 OPTIMO:------------------------------------
# Usar len y range para contar la lista y obtener su indice
li_numbers = [100, 200, 300, 400, 500]
# len(lista)->devuelve la dimension de la lista
# range(numero)-> genera un rango entre 0 y el numero dado
for indi in range(len(li_numbers)):
	# Operaciones
	li_numbers[indi] += 2000
# Impresion
print(li_numbers);

# CASO 6 ENUMERATE:------------------------------------
# enumerate(lista) - GEnera un indice para cada elemento de la lista
# enumerate devuelve una tupla
lista_item = ['aaa', 'bbb', 'ccc', 'ddd']
for indice, item in enumerate(lista_item):
	lista_item[indice] += 'Dato'
# Impresion
print(lista_item) 