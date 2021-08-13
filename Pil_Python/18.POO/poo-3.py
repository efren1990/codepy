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
	def arrancar(self):
		# Para llamar una propiedad dentro de un metodo de la clase usamos self
		self.enMarcha = True;
		
	def frenar(self):
		self.enMarcha = False;
	
	def estadoCoche(self):
		# evaluar estado del Coche
		if (self.enMarcha):
			return "El Coche esta en marcha";
		else:
			return "El Coche esta parado";

# Fin Clase	

#Crear un Objeto, instancia o ejemplar de la Clase->
miCoche = Coches();#Esto es->Instaciar una clase o crear un objeto

#Acceder a Propiedades y Comportamientos del OBjeto
#Se usa la Nomenclatura del punto
# nombreObejto.propiedad, nombreObjeto.metodo()
print("Largo del Chasis: ",miCoche.largoChasis," cm");
print("Ruedas del Coche: ",miCoche.ruedas," Ruedas");
miCoche.arrancar();
print(miCoche.estadoCoche())
miCoche.frenar();
print(miCoche.estadoCoche())