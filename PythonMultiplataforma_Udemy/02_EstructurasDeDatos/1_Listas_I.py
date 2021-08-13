"""
CLASE LISTA---------------------------------------------------------------
"""
# Declaracion de una lista
# Una lista siempre estara delimitada por corchetes
# NombreLista = [elem1, elem2, elem3]
lista = [1, 2, 3, 4, 5, 6]
print(lista)
lista2 = ["juan", "maria", 2, 234, 0.45]
print(lista2)
# Tipo de objeto lista
print(type(lista))
# Acceder a un elemento de la lista
# NombreLista[#elemento - 1 = indice]
elementoLista = lista2[1]
print(elementoLista)
# Operaciones Accediendo a elementos de lista|
sumaLista = lista[0] + lista[5]
print(sumaLista)

# LISTA TIPO CLASE LISTA----------------------------------------------------
# El string sera convertido en lista al seprar palabra por palbra
li = list("eXcript")
print(li) 
li2 = list(("eXcript","Código"))
print(li2)
# Python puede representar una lista agregando una , a su ultimo elemento
li3 = list(("eXcript",))
li4 = [4,]
li5 = ["roma", 1452, "italia", "carlos", 45.5,]

print(type(li3))
print(type(li4))
print(type(li5))

# LISTA DENTRO DE OTRA LISTA-----------------------------------------------
# Listas multidimensionales
# NombreLista = [[elem1, elem2, elem3,], [elem1, elem2, elem3], [ele,1, elem2]]
listaDim = [["Italia", "Roma", "Francia"], [5, 8, 2], []]
print(listaDim)
# Para acceder a los elementos en listas de mas de una dimension:
print(listaDim[0][0])
print(listaDim[0][1])
print(listaDim[0][2])
print(listaDim[1][0])
print(listaDim[1][1])
