"""
PROYECTO BITACORA O DIARIO
------------------------------------------------------------------------------------------------
Un diario de registros
"""
# Importar de la libreria collections el diccionario oredenado
from collections import OrderedDict
# Importar libreria de tiempo
import datetime
# Importar libreria peewee
from peewee import *
# Importar sys
import sys

# ------------------------------------------------------------------------
# Crear instancia base de datos
db = SqliteDatabase('bitacora')
# ------------------------------------------------------------------------
# Crear los Modelos de las Tablas
# Los cuales seran entradas o registros en la bitacora
class Entry(Model):
	# Campos de entradas
	# Fecha - timestamp
	timestamp = DateTimeField(default=datetime.datetime.now)
	# Contenido
	content = TextField()
	# Clase meta para referencias a que base de datos pertenece
	class Meta():
		database = db
# ------------------------------------------------------------------------
# Funciones para realizar operaciones con la base de datos

# Agregar un registro o entrada a la bitacora
def add_entry():
	"""Agregar registro en la bitacora"""
	print("Introduce tu registro, Presiona - ctr + D - cuando termines tu registro.")
	"""sys.stdin.read().strip() -> permite tomar el texto y captar la combinacion ctr + D
		para salir del texto y cerrar, de esta forma no se terminara al presionar enter como
		sucede con el input()
	"""
	data = sys.stdin.read().strip()
	# Validar si hay datos en la variable del contenido de registro
	if data:
		# Validar si el usuario quiere guardar el texto ingresado
		if input('Guardar Registro? [Y(Si) / N(No)]: ').lower() != 'n':
			# Usar el metodo create en el modelo de tabla para guardar los datos
			# En el campo correspondiente
			Entry.create(content=data)
			print('Registro guardado exitosamente.')
			print('-------------------------------')


# Ver Nuestros registros o entradas de bitacora
def view_entries(search_query=None):
	"""Ver registros en la bitacora"""
	# Hacer consulta peewee ordenando los registros o entradas
	# ordenado por fechas descendientes de mayor a menor
	entries = Entry.select().order_by(Entry.timestamp.desc())

	# Validar si se ingreso una busqueda por texto
	# solo se ejecutara si la variable es diferente de None
	if search_query:
		# HAcer busqueda por where y alamacenar
		entries = entries.where(Entry.content.contains(search_query));

	# Recorrer las entradas
	for entry in entries:
		# strftime(Fomarto) -> devuelve fecha en formato string y formato decha indicado
		fecha = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
		# Imprimir en pantalla datos extraidos de la tabla
		print('--------------------------------------------------------------')
		print('Fecha: ', fecha)
		print('--------------------------------------------------------------')
		print(entry.content)
		print('--------------------------------------------------------------')
		print('s| Siguiente Registro.')
		print('d| Borrar Registro.')
		print('q| Salir al Menu principal.')
		next_action = input('Seleccione Opcion: ').lower().strip()
		# Validar accion
		if next_action == 'q':
			# Terminar ciclo
			break;
		elif next_action == 'd':
			# Eliminar el registro pasando el objeto registro obtenido a la funcion 
			# que se encarga de eliminar el registro de la base de datos
			delete_entry(entry)

# Filtrar por palabras nuestras entradas o registros
def filter_entries():
	"""Filtrar por Palabras"""
	# Ingresar un parametro en el metro view_entries
	# el cual ejecutara la busqueda en la tabla
	view_entries(input('Introduce el texto a buscar: '))

# Borrar entradas o registros de la bitacora - entrada como parametro
def delete_entry(entry):
	"""Borar registro de la bitacora"""
	response = input("Estas Seguro? [Y(Si) / N(No)]: ").lower()
	# Validar seleccion de usuario
	if response == 'y':
		# Borrar instancia de la base de datos
		entry.delete_instance();
		print('--------------------------------------------------------------')		
		print('El registro ha sido borrado.')
		print('--------------------------------------------------------------')

# ------------------------------------------------------------------------
# Funciones para el menu de la aplicacion
"""Usar diccionario ordenado para las
opciones del menu"""
menu = OrderedDict([
	('a', add_entry),
	('v', view_entries),
	('s', filter_entries)
])
# Despliega menu con las opciones de diario
def menu_loop():
	# Variable para la desicion - default en None(ya que el usuario de entrada No habra escogido nada)
	choice = None
	# Bucle whime para acondicionar la seleccion del usuario
	while choice != 'q':
		print("-------------BITACORA ESPECIAL------------------------")
		print("Presiona: q || Para salir.")
		# recorrer opciones del diccionario para el menu
		for key, value in menu.items():
			# Imprimir La llave, y el comentario interno dentro del metodo que esta
			# como valor del diccionario
			# .__doc__->Muestra la documentacion interna de la funcion o metodo
			print('-----------------------------------------------------')
			print('Presiona: {} || {}'.format(key, value.__doc__))
			print('-----------------------------------------------------')
		# Tomar seleccion del usuario
		# .lower() -> pasa strin a minusculas
		# .strip() -> elimina espacios
		choice = input('Presiona la letra de tu seleccion: ').lower().strip()
		# Validar la Eleccion del usuario
		if choice in menu:
			# Llamar el metodo o funcion seleccionado
			menu[choice]() 


# Inicia la aplicacion
def initialize():
	# Conectar con la base de datos
	db.connect()
	# Crear Tablas de Modelos
	db.create_tables([Entry], safe=True)
# ------------------------------------------------------------------------
# Iniciar la app
if __name__ == '__main__':
	# Iniciar la aplicacion
	initialize()	
	# Iniciar el menu
	menu_loop()