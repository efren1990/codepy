#-----------MANIPULACION DE DATOS--------------------#
num_entero = 5
num_decimal = 5.8
tipo_string = "Este es un Texto "

#Casteo en python
"""
str()->casteo a string
int()->Casteo a int
float()->Casteo a float
"""
print(tipo_string + str(num_decimal))
print("Nuero float a string: " + str(num_decimal))

#concatenacion en pytohn----------------
print("Numero Decimal:", num_decimal)

#Marcadores
"""Se deben usar con el signo % seguido de la inicial
del tipo de dato
%i entero
%f flotante
%.#f = cantidad de decimales a mostrar
%s strings
"""
print("Numero Entero: %i" %num_entero)
print("Numero Decimal: %f" %num_decimal)
print("Nuero Decimal Controlado decimales: %.2f" %num_decimal)

