#---------------------------------------------------#
#POO->Programacion Orientada a Objetos
#---------------------------------------------------#
#Cosntruccion de una clase
	# class NombreClase():
#HERENCIA----------------->
"""
Cuando una clase hereda de otra ya sea metodos o propiedades

►Para que Sirve la Herencia?->
	Para reutilizar codigo en caso de crear objetos similares
"""
# Clase Padre o Super clase-> la que engloba las caracteristicas y comportamientos comunes
class Vehiculos:
	# Constructor------->
	def __init__(self, marca, modelo):
		self.marcaV = marca;
		self.modeloV = modelo;
		self.enMarcha = False;
		self.acelerar = False;
		self.frenar = False;
	# Metodos-----------> 
	
	#Metodo para arrancar
	def arrancar(self):

		self.enMarcha = True;
	# Fin Metodo

	#Metodo para Acelerar
	def acelerar(self):

		self.acelerar = True;
	# Fin Metodo

	# Metodo para Frenar
	def frenar(self):
		self.frenar = True;
	# Fin Metodo

	# Metodo PAra saber Estado del Objeto
	def estado(self):
		print("Marca: ", self.marcaV, "\nModelo: ", self.modeloV, "\nEn Marcha: ", self.enMarcha, 
			  "\nAcelerando: ", self.acelerar, "\nFrenando: ", self.frenar);
	# Fin Metodo
# Fin Clase----------------------------------------------------------------------------------------

"""Clase que heredara de la clase Vehiculos, tanto propiedades, como metodos y el 
metodo constructor"""
#La clase moto tendra propiedades y metodos unicos de ella que no esten en la super clase
class Moto(Vehiculos):
	
	#Propiedades------>
	haceCangu = "";
	
	#Metodos---------->

	#metodo para que la moto haga un canguro
	def canguro(self):
		self.haceCangu = "Haciendo Canguro";
	#fin metodo
	"""Para Hacer que la moto informe su estado completo incluyendi si esta o no
	haciendo canguro es necesario sobreescribir el metodo estado de la clase padre
	Conocido como polimorfismo"""
	# Metodo PAra saber Estado del Objeto
	def estado(self):
		print("Marca: ", self.marcaV, "\nModelo: ", self.modeloV, "\nEn Marcha: ", self.enMarcha, 
			  "\nAcelerando: ", self.acelerar, "\nFrenando: ", self.frenar, "\nEstado: ",self.haceCangu);
# Fin Clase-----------------------------------------------------------------------------------------------

"""Clase para Vehiculos Electricos"""
class VehElectricos(Vehiculos):
	#Constructor-------------->
	def __init__(self, marca, modelo):
		#autonomia de la bateria en kms
		self.autonomia = 100;
		# Llamado del constructor Padre
		super().__init__(marca, modelo)
	#Metodos----------------->
	def cargarEnergia(self):
		self.cargando = True;
# Fin Clase-----------------------------------------------------------------------------------------------

"""Clase para furgonetas que heredara de La Clase Vehiculos"""
class Furgoneta(Vehiculos):

	#Metodos--------------->
	def carga(self, cargar):
		self.cargado = cargar;
		if(self.cargado):
			return "La Furgoneta esta Cargada";
		else:
			return "La Furgoneta no Esta Cargada";
# Fin Clase-----------------------------------------------------------------------------------------------


# Instancia de la Clase Moto, la cual recibe los parametros para el constructor en su estado inicial
miMoto = Moto("Honda", "Tornado");
miMoto.canguro();
miMoto.estado();
print("===========================================================================================");
# Instancia de la Clase Furgoneta
miFurgoneta = Furgoneta("Mazda", "Luv-2000");
miFurgoneta.arrancar();
miFurgoneta.estado();
print(miFurgoneta.carga(True));
print("===========================================================================================");

"""HERENCIA MULTIPLE----->
Python permite heredar de dos clases o mas
En la erencia multiple se da preferencia de la primera clase
que se pone en el parentesis, de esta forma la primera clase puesta
dara como herencia su constructor
"""
# Clase para Bicicletas Electricas la cual hereda de las clases VehElectricos y Vehiculos
class BiciElectrica(VehElectricos, Vehiculos):
	pass
# Fin Clase-----------------------------------------------------------------------------------------------
# Instacia de la clase bicicleta la cual herada el constructir de la clas VehElectricos
miBicElectrica = BiciElectrica("Brecks", "pegasus100");
