#Una lista en Python es un Array
#Nota->En Python los Arrays se pueden Expandir Dinamicamente
#Nota->En Python las listas pueden guardar diferentes tipos de valores
#Sintaxi:
	#nombreLista = [elem1, elem2, elem3]

listaArra = ["pedro", "juan", "Jessica", "lili"];
#Imprimir un Elemento Segun su Indice
print("Elemento[0] es: " + listaArra[0]);
print("Elemento[1] es: " + listaArra[1]);
#En python se pueden usar indices negativos donde el primer indice sera -1 en adelante
print(listaArra[-4]);
#Porcion de Lista: es acceder a una porcion de esa lista o array
print(listaArra[0:3]);
#Donde el rango 0 incluye el primer indice y el 3 elxcluye el indice 3
#--------------------------------------------------------------------------------#
#Agregar Elemetos a una Lista
listaArra.append("Carolina");#Agrega un elemento nuevo al final de la lista
print(listaArra[:]);#Imprime todos los Elementos de la lista
#--------------------------------------------------------------------------------#
#Agregar un elemento a la lista escogiendo la posicion
# array.insert(posicion, elemento)
listaArra.insert(2,"jinx");
print(listaArra[:]);
#--------------------------------------------------------------------------------#
#Agregar Otro array a un array ya existente
listaArra.extend(["carro", "moto", "bus", "avion"]);
print("Suma de 2 Listas: " , listaArra[:]);
#--------------------------------------------------------------------------------#
#saber el indice de un elemento en la lista
print("Inidice elemento moto: ",listaArra.index("moto"));
#--------------------------------------------------------------------------------#
#Comprobar si un elemento se encuentra o no en una lista
#Debuelve true o false
print("pepe" in listaArra);
print("carro" in listaArra);
#--------------------------------------------------------------------------------#
#En Python el mismo elemento puede estar en diferente posicion de la lista
listaArra.append("pedro");
print("pedro" in listaArra);
#--------------------------------------------------------------------------------#
#Las Listas pueden alamacenar Diferentes Tipos de Datos
miLista = ["maria", 4, 8, True, 4.58];#true en python es True
print(miLista[1]);
#--------------------------------------------------------------------------------#
#BOrrar elementos de las listas
miLista.remove(4.58);
print(miLista[:]);
#--------------------------------------------------------------------------------#
# Eliminar el ultumo elemento de una listas
miLista.pop();
print(miLista[:]);
#----------------------------Ejercicios Con Listas----------------------------------------#
# Concatenar Listas
myList_1 = ["Leon", "Tigre", "Pantera", "Jaguar"];
myList_2 = ["Conejor", "Liebre", "Cabra"];
myListConcatenada = myList_1 + myList_2;
print(myListConcatenada[:]);
#Repetir una Lista->Se multiplica por la cantidad de repeticiones que se quiera
listaRepetida = ["Carlos", 5, False, 78, 99] * 3;
print(listaRepetida[:]);
