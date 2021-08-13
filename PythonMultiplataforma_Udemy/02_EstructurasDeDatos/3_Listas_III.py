"""
METODOS PARA OPERCIONES CON LISTAS----------------------------------
Operaciones con listas Mutables
"""
# Sumar o Agragar elementos a una lista mutable
myLista_I = [1, 2, 3, 4, 5];
print("Contenido Lista 1: ", myLista_I)

# Forma 1 de sumar o adicionar datos a una lista
myLista_I = myLista_I + [6]
myLista_I = [0] + myLista_I
print("Agregar, Forma 1: ", myLista_I)
myLista_I = myLista_I + [7, 8, 9, 10]
print("Agragando Varios elementos Forma 1: ", myLista_I)

# -----------------------------------------------------------------
# Agregar elementos con append - solo 1 ulelemto a la vez
myLista_II = ["a", "b", "c", "d"]
myLista_II.append("e")
print(myLista_II)
# Agregar Listas dentro de listas
myLista_II.append([1, 2, 3, 4, 5])
print(myLista_II);
# Eliminar elementos dentro de una Lista
myLista_del = ["x", "y", "z", "q"]
print("Datos antes de borrar")
# del(lista[indiceElemento])
del(myLista_del[3])
print("Datose de lista: ", myLista_del);
# ---------------------------------------------------------------------
# Agregar varios elementos a la vex
lisNum = [1, 21, 31, 55] 
lisNum += 10*[0]
print(lisNum)
listRay = "-"
listRay += 50 * "-"
print(listRay)