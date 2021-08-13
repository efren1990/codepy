#--------------------------------------------------------------------------------#
# Las Tuplas->
# Son Listas inmutables(no se pueden alterar), es decir,
# No se pueden modificar despues de su creacion
# No permiten añadir, eliminar, mover elementos etc(no append, extend, remove)
# Si permiten Extrer porciones, pero el resultado de la extraccion es una tupla nueva
# Si permite Comprobar si un elemento se encuentra en la tupla

# Qué utilidad o Ventaja tienen las Tuplas?
#son mas Rapidas
#Menos Espacion(Mayor optimizacion)
# Formatean Strings
# ->Pueden Utilizarse como Claves en un Diccionario.(Las Listas no)<-
#-------------------------------Sintaxis de las Tuplas--------------------------------#
# Las tuplas se leen como los arrays por indices, pero no son arrays
#nombreTupla = (elem1(inidie 0), elem2(indice 1), elem3, .....)
tuplita = (2, "hola", "mundo", "python");
# Acceder a un elemento de la Tuplas
print(tuplita[2]);
print(tuplita[0]);

#--------------------------------------------------------------------------------#
#METODOS DE CONVERSION
# 1-->DE TUPLA A LISTA(ARRAYS)
miLista = list(tuplita);
print(miLista);#Las Listas se imprimen con corchetes(mirar consola)
print(tuplita);#Las Tuplas se imprimen con parentesis(mirar consola)
# 2-->DE LISTA A TUPLA
lista = ["casa", "carro", "piscina", "jardin", "baño", "jardin"];
miTupla = tuple(lista);
print(miTupla);
#--------------------------------------------------------------------------------#
# Saber si el elemento esta en la Tuplas ("ElementoBuscado" in(palabre clave) nombreTupla)
print("casa" in miTupla);
#--------------------------------------------------------------------------------#
# Contar un elemento dentro de una Tupla nombreTupla.count(elementoAContar)
print(miTupla.count("casa"));
print(miTupla.count("jardin"));
#--------------------------------------------------------------------------------#
# Haberiguar la Longitud en elementos de una Tupla, elementos, indices no
print(len(miTupla));
#--------------------------------------------------------------------------------#
# Tuplas Unitarias->Tuplas con un unico elemento
miTuplaUnitaria = ("Efren",);
print(len(miTuplaUnitaria));
#--------------------------------------------------------------------------------#
# Empaquetado de Tupla->Se declara la tupla sin parentesis(no se recomienda)
tuplaEmpaquetada = "pepe", 2, 5, 1990, "sagitario";
print(tuplaEmpaquetada);
# Desempaquetado de Tuplas->alamacenar los contenidos de la tupla en variables
nombre, dia, mes, agno, signo = tuplaEmpaquetada #->Pytoh empaqueta en orden los valores de la tupla en las variables
print(nombre);
print(mes);
print(dia);
print(agno);
print(signo);