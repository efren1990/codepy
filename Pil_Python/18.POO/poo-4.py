#---------------------------------------------------#
#POO->Programacion Orientada a Objetos
#---------------------------------------------------#
#Cosntruccion de una clase
	# class NombreClase():

class Coches():
	# Propiedades o Caracteristicas->
	largoChasis = 250;
	anchoChasis = 120;
	ruedas = 4;
	enMarcha = False;
	# Metodos o Comportamimentos->son funciones dentro de la clase
	#self->Objeto perteneciente a la clase, python pide ponerlo como primer parametro
	#self es similar a this en javascript
	# Agregamos un parametro mas al metodo arrancar
	def arrancar(self, arrancamos):
		# El segundo parametro se alamacenara en la propiedad enMarcha 
		self.enMarcha = arrancamos;

		if (self.enMarcha):
			return "El Coche esta en marcha";
		else:
			return "El Coche esta parado";
		
	def frenar(self):
		self.enMarcha = False;

	def estado(self):
		print("El Coche tiene:",self.ruedas,"Ruedas");
		print("Largo del Chasis:",self.largoChasis,"cm.");
		print("Ancho del Chasis:",self.anchoChasis,"cm.");


# Fin Clase
print("-----------------------Creamos el Primer Objeto----------------------");
#Crear un Objeto, instancia o ejemplar de la Clase->
miCoche = Coches();#Esto es->Instaciar una clase o crear un objeto

#Acceder a Propiedades y Comportamientos del OBjeto
#Se usa la Nomenclatura del punto
# nombreObejto.propiedad, nombreObjeto.metodo()
miCoche.estado();
print(miCoche.arrancar(True));

print("-----------------------Creamos el Segundo Objeto----------------------");
miCoche2 = Coches();
miCoche2.estado();
print(miCoche2.arrancar(False));
