"""
ORDENAMIENTO DE LISTAS
"""
lista = ['Juan', 'Pedro', 'Carlos', 'Adriana', 'Carolina', 'Maria']
print(lista)

# Invertir posiciones en una lista - lista.reverse()
lista.reverse()
print(lista)

# Ordernar lista de forma ascendente - lista.sort()
li = ['e', 'b', 'f', 'g', 'h', 'a', 'c', 'd']
li.sort()
print(li)

# Truco para ordenar una lista de forma descendente
n = [4, 8, 7, 3, 2, 1, 5, 6]
n.sort()
print(n)
n.reverse()
print(n)

# Truco 2 para ordenar una lista de forma descendente
g = [80, 100, 90, 60, 70, 30, 40, 50]
g.sort(reverse = True)
print(g)