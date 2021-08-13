	# Lista Letras
l = ['bbb','ccc','ddd']

# Agregar un elemento al finar de la lista - lista.apped(valor)
l.append("eee") 
print(l)

# Agregar un elemento especificando la posicion - l.insert(posicion, valor)
l.insert(0, 'aaa')
print(l)

# Alterar el elemento de una lista - lista.[indice] = nuevo valor
l[1] = 'bbBBbbBB'
print(l)

# Limpiar un lista - lista.clear()
l.clear()
print(l)
# Eliminar un item determinado de una lisa - el ultimo itemr
s = ['bb','cc','dd','ee']
s.pop()
s.pop()
print(s)

# Eliminar el 1er item de una lista - lista.pop(indice)
x = ['francia', 'italia', 'roma']
p = x.pop(0);
print("Elemento:",p)

# eliminar el ultimo elemento con pop - lista.pop(-1)
z = ['colt 45', 'S&W .38', 'mp5']
u = z.pop(-1)
print("Ultimo:",u)

# Eliminar porciones de una lista - del(lista[inicio:fin])
d = ['a','b','c','d','e','f']
del(d[2:4])
print(d)

# Eliminar elementos con intervalos - del(lista[::intervalo])
k = ['x','y','z','1','3',5]
del(k[::2])
print(k)



