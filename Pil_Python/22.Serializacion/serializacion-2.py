#xxxxxx------------------------------------------------------------->
#SERIALIZCION
#xxxxxx------------------------------------------------------------->
#SERIALIZACION DE OBJETOS->
# Como se va a serializar se debe importar la libreria pickle
import pickle
# Creamos una clase 
class Vehiculos():

	#Constructor
	def __init__(self, marca, modelo):
		#Propiedades
		self.marcaV = marca;
		self.modeloV = modelo;
		self.enMarcha = False;
		self.acelera = False;
		self.frena = False;

	#Metodos
	def arrancar(self):
		self.enMarcha = True;
	
	def acelerar(self):
		self.acelera = True;
	
	def frenar(self):
		self.frena = True;

	def estado(self):
		print("Marca: ",self.marcaV, "\nModelo: ",self.modeloV, "\nEn Marcha: ", self.enMarcha,
			  "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena);

#Fin Clase
#xxxxxx------------------------------------------------------------->
#OBJETOS A SERIALIZAR
#xxxxxx------------------------------------------------------------->
#Objeto1
coche1 = Vehiculos("Mazda", "MX5");
#Objeto2
coche2 = Vehiculos("Renault", "clio");
#Objeto3
coche3 = Vehiculos("Chevrolet", "Aveo Sedan");
#Objeto4
coche4 = Vehiculos("Kia", "Rio");
#Coleccion de Objetos
coches = [coche1, coche2, coche3, coche4];
# Creamos Variable Fichero, creamos abrimos el fichero con open con permisos "wb" write bites
fichero = open("losCoches", "wb");
#volcado de datos
pickle.dump(coches, fichero);
#Cierre del Fichero o archivo
fichero.close();
#Borrar Fichero de la memoria
del(fichero);

#LLAMADO DEL FICHERO NUEVAMENTE
#abrir el fichero con permiso de lectura de bites "rb"
ficheroApertura = open("losCoches", "rb")
#Variable para volcar o pasar la informacion de esste fichero
misCoches = pickle.load(ficheroApertura);
#Cierre de fichero
ficheroApertura.close();

for c in misCoches:
	print(c.estado());