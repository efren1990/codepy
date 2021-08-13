"""
#ITERACION DE  STRINGS 
---------------------------------------------------------------------
Funciona de la misma forma que cualquier otra iteracion de una lista de objetos
"""
# EJEMPLO 1
s = "Iterando strings"
# Recorrer el string con for
for l in s:
	print(l)

# EJEMPLO 2
s = "Iterando strings"
indice = 0;
while indice < len(s):
	print(indice, s[indice])
	# Aumentar indice
	indice+=1

# EJEMPLO 3
s = "Iterando strings"
# Usando Enumarate - Genera un indice para cada elemento de la lista - strings
# enumerate en un string - devuelve el caracter - valor y la clave -llave 
print(dict(enumerate("Iterando listas")))
# k - key - llave
# v - value - valor
for k,v in enumerate("Iterando strings"):
	print(k,"-", v)