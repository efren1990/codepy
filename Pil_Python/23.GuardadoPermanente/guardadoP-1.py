#xxxxxx------------------------------------------------------------->
#GUARDADO PERMANENTE 
#xxxxxx------------------------------------------------------------->
"""
El guardado permante se usa para ir guardando paulatinamente
informacion dentro de el incluso desde diferentes programas,
informacion la cual tendremos disponible en nuestro sismtema de archivos
"""
#Cramos clase y objetos para ir guardandolo en un fichero externo para luego reutilizarlo
#Importamos libreria pickle para poder manipular archivos
import pickle
#Clase persona
class Persona():
	#Constructor
	def __init__(self, nombre, genero, edad):
		#Propiedades
		self.nomPer = nombre;
		self.genPer = genero;
		self.edaPer = edad;
		print("Se ha Creado una Persona Nueva con el nombre de: ", self.nomPer);
	#Metodo Especial->str para convertir en cadena de texto la informacion de un objeto
	"""Metodo para ver lainformacion de las ppersonas que guardemos en un fichero
	externo"""
	def __str__(self):
		#Retorno de los tres datos con un formato
		return "{}  {}  {}".format(self.nomPer, self.genPer, self.edaPer);
#Fin Clase
# Clase para Guardar la informacion en una lista
class ListaPersonas():
	#Propiedad Array Vacio
	listaPer = [];
	#Constructor->El cual abrira el archivo externo y guardara la informacion
	def __init__(self):
		#abrir con permiso para agreagar informacion binaria "ab+"
		listaPerArchi = open("ficheroExterno", "ab+");
		#Desplazar el cursor al comienzo para que se pueda leer la informacion 
		listaPerArchi.seek(0);
		try:#Usar try para la primera vez que se instacie la clase ya que no llevara ninguna informacion
			#Volcado de informacion para almacenarla y leerla
			self.listaPer = pickle.load(listaPerArchi);
			print("Se Cargaron {} Personas al Fichero externo".format(len(self.listaPer)));
		except:
			print("El Fichero Esta vacio");
		finally:
			# Cerrar Archivo
			listaPerArchi.close()
			# Borrar lista de memoria
			del(listaPerArchi)
	#Metodos---------------<
	#Metodo para agregar personas a la lista
	def agregarPersona(self, per):
		#Agregar persona a la lista con append
		self.listaPer.append(per);
	#Metodo para leer o mostrar persona de la lista
	def mostrarPersona(self):
		#Recorrer lista de personas con for
		for p in self.listaPer:
			# Imprimir la listaPer
			print(p);
	#Metodo para guardar Personas Fichero Externo
	def guardPersonasArchivo(self):
		#Abrir archivo con permiso "wb" escribir binario
		listaPerArchi = open("ficheroExterno", "wb");
		#Volcado de informacion
		pickle.dump(self.listaPer, listaPerArchi);
		# cerrar la lista no utilizada de la memoria
		listaPerArchi.close()
		del(listaPerArchi)
	#Metodo para mostrar la informacion del archivo externo
	def mostArchiLista(self):
		print("La informacion del fichero externo es la siguiente: ");
		for p in self.listaPer:
			print(p)

#GUARDAR LA INFORMACION EN UN ARCHIVO EXTERNO
#Obejto lista personas
miListaPersonas = ListaPersonas();
#Instancia de Objetos
p1 = Persona("Carol", "Femenino", "18");
#Agregamos personas al objeto lista persona
miListaPersonas.agregarPersona(p1);
#Mostrar informacion del fichero
miListaPersonas.mostArchiLista();