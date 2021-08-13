"""-------------------------------------------OPERADOR DE IGUALDAD-----------------------------------------------"""
"""Se usa para comprar si dos datos o valores son iguales"""
#-Captar Datos
numero1 = input("Ingrese el numero 1: ")
numero2 = input("Ingrese el numero 2: ")
#Casteo de  Datos : string a int
numero1 = int(numero1)
numero2 = int(numero2)

#VALIDACION con operador de IGUALDAD
if(numero1 == numero2):
    #%d -> es sustituido por el orden de variabels al final
    print("El numero %d es igual al numero %d "%(numero1, numero2))

#VALIDACION con operador de DIFERENCIA
if(numero1 != numero2):
    print("El numero %d es diferente del numero %d "%(numero1, numero2))

#VALIDACION con operadores MAYOR y MENOR
#Menor
if(numero1 < numero2):
    print("El numero %d es menor que el numero %d "%(numero1, numero2))
#Mayor
if(numero1 > numero2):
    print("El numero %d es mayor que el numero %d "%(numero1, numero2))
