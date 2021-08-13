#---------------------------------------------------#
#POO->Programacion Orientada a Objetos
#---------------------------------------------------#
#Cosntruccion de una clase
	# class NombreClase():
#POLIMORFISMO----------------->
"""
poli->muchas
morfismo->formas
Quiere decir que un objeto puede cambiar de forma dependiedo
del contexto en el que se utilice, y por lo tanto al cambiar
de forma ese objeto tambien cambia de comportamientos
"""
#Clase Coche-------------------------------------->
class Coche():
	#MEtodo Desplazamiento
	def desplazamiento(self):
		print("Me desplazo usando cuatro ruedas");
# Fin Clase---------------------------------------->

#Clase Moto---------------------------------------->
class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas");
# Fin Clase---------------------------------------->

#Clase Moto---------------------------------------->
class Camion():
	def desplazamiento(self):
		print("Me desplazo Utilizando seis ruedas");
# Fin Clase---------------------------------------->
#Funcion Polimorfista------------------------------->
"""La cual utilizara un objeto por parametro para llamar
el metodo desplazamiento, el cual dependera del objeto
ingresado, lo que permite a un obejto cambiar de forma 
dependiendo del contexto"""
def desplazamientoVehiculos(objVehiculo):
	# Llamado del metod del objeto ingresado
	objVehiculo.desplazamiento();
#Fin funcion Polimorfista--------------------------->

#Instacia de clases 
miVehiculo = Moto();#camion(),coche()
#la fucnion reconcera el objeto y desatara su metodo
#el objeto cambia de forma
desplazamientoVehiculos(miVehiculo);


