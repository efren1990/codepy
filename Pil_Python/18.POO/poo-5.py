#---------------------------------------------------#
#POO->Programacion Orientada a Objetos
#---------------------------------------------------#
#Cosntruccion de una clase
	# class NombreClase():
#METODO CONSTRUCTOR-> Se usa para darle un estado inicial
#a un objeto o clase instanciada, es decir la configuracion por defecto del objeto

#ENCAPSLAMIENTO->Se usa para proteger desde afuera una propiedad o metodo de una clase

class Motos():
	#Metodo Cosntructor(al ser instanciada la clase las propiedades tomaran el valor)
	#definido en el metodo constructor
	def __init__(self):
		#Encapsulamiento en pytho se hace con dos guiones bajos antes del nombre(__nombrePropiedad)
		self.__largChass = 120;
		self.__ancChass = 65;
		self.__ruedas = 2;
		self.__motor = 650;
		self.__enMarcha = False;
	#Propiedades------>
	
	
	#Metodos------->
	# Metodo para arrancar la moto
	def arrancar(self, orden):
		self.__enMarcha = orden;
		# Validamos el checkeo interno antes del arranque
		if (self.__enMarcha):
			# Llamamos el metodo del chequeo interno para alamacenar su respuesta
			cheking = self.__checkInterno();
		# Validamos la orden y el cheking para el arranque	
		if self.__enMarcha and cheking:

			return "La Moto esta en Marcha";

		elif self.__enMarcha and cheking == False:

			return "Fallos en el sistema interno, no podemos arrancar";	

		else:
			return "La Moto esta Parada";
			
	# Metodo para saber el estado de las propiedades de la moto
	def estado(self):
		print("Largo del Chasis:", self.__largChass,"cm");
		print("Ancho del Chasis:", self.__ancChass,"cm");
		print("Ruedas: ",self.__ruedas);
		# Para acceder a una propiedad encapsulada se debe poner los dos guines bajos antes del nombre
		print("Motor:",self.__motor,"cc");
	# Metodo para checkeo interno de la moto(Encapsulado para que no sea usado desde afuera de la clase)
	def __checkInterno(self):
		print("Realizando chequeo Interno");
		self.gasolina = "ok";
		self.aceite = "ok";
		self.frenos = "activos";
		if self.gasolina == "ok" and self.aceite == "ok" and self.frenos == "activos":
			return True;
		else:
			return False;


# fin clase
print("-----------------------Creamos el Primer Objeto----------------------");
miMoto = Motos();
# No permitira cambiar el valor de la propiedad ruedas ya que esta protegida y encapsulada
#una propiedad encapsulada no es accesible desde afuera de la clase solo desde adentro asi se aplique
#los guines bajos
miMoto.__ruedas = 10;
miMoto.estado();
print(miMoto.arrancar(True));
