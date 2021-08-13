"""
#COMPARANDP STRINGS 
---------------------------------------------------------------------
Relacion entre dos strings distintas
"""
# Python compara los strings segun el valor del codigo ascci
print("a" > "1")

# Obtener carracter segun valor ascii
print(chr(100))
print(chr(97))
# Obtener codigo ascci segun caracter strings
print(ord('d'))
print(ord('a'))
print(ord('1'))
# Caracteres de la tabla ascii
print("================Caracteres y Valores Tabla ASCII======================")
for car in range(122):
	print("| Codigo: ",car," | Caracter: ", chr(car))
	print("-----------------------------------------")