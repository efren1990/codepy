"""
PROGRAMACIÓN ORIENTADA A OBJETOS
----------------------------------------------------------------------------------------------------------
Es un paradigma de programacion y tambien una metodologia para el desarrollo de software, es un tecnica
de estructuracion y organizacion de codigo fuente que nos permite definir estructuras independientes
que podran tener variables y funciones definidas internamente.

#CREANDO INSTANCIAS

Las clase son objetos que contiene informacion de como los objetos deberan funcionar y que valores
cada instacia podra almacenar.

La clase es nuestro codigo propiamente dicho y para que tenga utilidad es necesario crear objetos o
instancias.

#INSTACIA: instacia es cada un de los objetos creados durante la ejecucion de un programa.
objeto o instacia son sinonimos
------------------------------------------------------------------------------------------------------------
CLASE es el proyecto de un objeto
OBJETO es la ejecucion del codigo de una clase
INSTACIA es un sinonimo de objeto

En python todo objeto posee un ID compuerto por un número entero no negativo, este ID
es como el nombre de cada objeto

"""
# Clase persona
class Persona():
	pass
# INSTACIA DE CLASES
# var = NombreClase()
p1 = Persona()
p2 = Persona()
# Asi los objetos sean creados con la misma clase, tienen diferentes ID
print(id(p1))
print(id(p2))