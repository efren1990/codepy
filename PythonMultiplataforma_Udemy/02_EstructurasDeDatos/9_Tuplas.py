"""
TUPLAS -------------------------------------------------
Una tupla es una lista inmutable
1.Es una lista declarada como una constante
2.No es posible adicionar, eliminar, ni alterar elementos
3.Toda tupla sera un conjunto de objetos inmutable

Philip e bay "Las tuplas pueden ser usadas para alamacenar datos 
heterogeneos mientras que las listas pueden ser usadas para datos
Homogeneos, como un proposito de uso, pero no obligatorio"

"""
# Definir una tupla
# Las tuplas van en parentecisi nomTupla(element1, element2, ...)
t = tuple("abcde")
print(t)
# Python reconoce que todo lo contenido dentro de parentesis es una tupla
n = (1, 2, 3, 4, 5, 6)
print(n)
print(type(n))
s = ("juan", 23, True)
print(s)
# Los elementos de una tupla pueden ser vistos o leidos accediendo a sus indices como las listas
