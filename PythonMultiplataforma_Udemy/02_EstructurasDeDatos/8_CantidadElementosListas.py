"""
CANTIDAD DE ELEMENTOS DE UNA LISTA
"""
l = ["pepe", "roncancio", "cosme", "fulanito", "sutanejo", "pacholino"]
print(l)
# Obtener la cantidad de elementos de una LISTA
# len(lista)
print(len(l))

# Acceder al ultimo elemento de una lista con len
# lista[len(lista)-1]
print(l[len(l)-1])

# Acceder al ultimo elemento de una lista con -1
print("Ultimo elemento con indice negativo: ", l[-1])
# Acceder al primer elemento de una lista con indice negativo
# el primer elemento seria contando la lista de atras hacia adelante en degativo
# Los indices negativos iniciarian empezando a contar desde el ultimo elemento hasta el primero
print("Primer elemento con indice negativo : ",l[-6])

# Saber cuantos elementos repetidos existen en una lista
k = ["a", "s", "d", "f", "t", "p", "w"]
k.insert(len(k) + 1, 'a')#agragar al ultimo con len :)
print(k)
k.append('a')
print(k)
# count -> permite saber cuantas veces se repite un elemento en una misma lista
# lista.count(elemento)
cant = k.count('a')
print("Cantidad de veces elemento a en lista k: ", cant)

n = [1, 4, 5, 6, 1, 6, 8, 1, 1]
cantN = n.count(1)
print("Canttidad de veces 1 en lista n: ", cantN)

# Saber cual es el indice de un elemento dentro de una lista
# lista.index()
c = ['xp', 'ye', 'bp', 'ms', 'to']
c = c.index('xp')
print("indice elemento xp: ", c)
# Si un elemento se repite index solo devolvera el indice del primer elemento