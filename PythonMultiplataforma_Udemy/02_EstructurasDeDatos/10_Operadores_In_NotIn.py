"""
IN y NOT IN
permiten verificar si un elemento se encuentra o no en una lista, tupla, diccionario

IN (Significa Contenido en)-> 
Permiten verficar si un elemento se encuetra contenido en una lista, tupla, diccionario
	x in lista[] - devuelve True

"""
l = ["a", "b", "c", "d", "e"]
# Validar si el elemento esta en la tupla
confir = "a" in l
print("Esta el elemento:",confir)
confir = "x" in l
print("Esta el elemento:",confir)
# Validar si el elemento no esta en la tupla
connot = 4 not in l
print("No esta el elemenot:",connot)
connot = "a" not in l
print("No esta el elemento:",connot)

# In y Not In Con Range --------------------------------------------
l_ran = list(range(1,6))
print(l_ran)
#1
con = 1 in range(1,6,)
print("1 se encuentra en el rango de 1 a 6: ", con)
#2
con_a = 6 in range(1,6,)
print("6 se encuentra en el rango de 1 a 6: ", con_a) 
#3
con_b = 6 not in range(1,6,)
print("No esta 6 en el rango de 1 a 6: ", con_b)
#4
ra = range(0,8,2)
print(list(ra))
#Esta 1 en el rango(0,8,1)
if 1 in range(0,8,1):
	print("Esta")
else:
	print("No Esta")