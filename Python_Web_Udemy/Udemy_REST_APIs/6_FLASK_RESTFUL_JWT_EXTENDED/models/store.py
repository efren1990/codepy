"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------------------
MODELS O MODELOS->
Nos permiten hacer interacciones con las base de datos directamente
pero no responden a las apis clientes 
Un Modelo es la represtacion Interna de nuestra Entidad
--------------------------------------------------------------------------
Modelo de Stores - Tiendas
"""
# Objeto sqlalchemy (db.py) ------->
from db import db
#------------------------------------------------------------------------------
# @CLASS MODEL: ITEM - ARTICULO - HEREDA: MODEL SQLALCHEMY OBJECT
#------------------------------------------------------------------------------
class StoreModel(db.Model):
	#------------------------------------------------------------------------------
	# MODELO DB SQLALCHEMY TABLA STORES
	#------------------------------------------------------------------------------
	# TABLA DEL MODELO
	__tablename__ = 'stores'
	# ID
	id = db.Column(db.Integer, primary_key=True)
	# NAME
	name = db.Column(db.String(90))
	# RELACIONAR LAs TABLAS MODELO STORES CON ITEMS
	items = db.relationship('ItemModel')
	#----------------------------------------------------------
	# @METHOD:CONSTRUCTOR                        
	# @PARAMS:Selr, nombre, precio                        
	#----------------------------------------------------------
	def __init__(self, _name):
		self.name = _name
	#----------------------------------------------------------
	# @METHOD:JSON-Crea un diccionario con los datos del item                        
	# @PARAMS:Selr                        
	#----------------------------------------------------------
	def json(self):
		# self.items -> ejecuta la consulta en el modelo relacionado 
		#  para cada item extraido llama su metodo json() que los retorna como
		# Diccionario
		return {'id':self.id, 
						'name':self.name, 
						'items':[item.json() for item in self.items] #List Comprehension
						}
	#----------------------------------------------------------
	# @CLASSMETHOD: Busca un articulo por nombre                    
	# @PARAMS: self, name                        
	#----------------------------------------------------------
	@classmethod
	def find_by_name(cls, name):
		# Consulta en la tabla flitrada por nombre flask-alchemy
		"""
		#COMENT-> Flask-Alchemy
		Evita que realicemos todo el proceso de generar un conexion y cerrarla
		convirtiendo las consultas en metodos.
		.filter_by() -> genera consultas, se pueden concatener multiples filters
		.filter_by().filter_by().filter_by().filter_by()
		.first() -> limita a la primera fila encontrada por la consulta
		objetoModel.query -> la consulta se aplica al objeto que hereda de Model Flask-Alchemy object
		"""
		return cls.query.filter_by(name=name).first() # SELECT * FROM __tablaname__ WHERE name = paramMethod LIMIT 1
	#----------------------------------------------------------
	# @METHOD: Guarda datos de un articulo, nuevo o actuliza                     
	# @PARAMS: self                        
	#----------------------------------------------------------
	def save_to_db(self):
		"""
		#COMENT-> Insertar con flask-alchemy
		permite insertar un objeto con los datos de la tabla
		en este caso se pasa el parametro self, el cual contiene
		el objeto en si mismo con sus propiedades name y price
		db.session.add(objeto)->inserta un objeto 
		"""
		db.session.add(self)
		db.session.commit()
		"""
		#session.add(datos, objeto)->Nos permite crear un objeto para
		la session actual y alamacenarlo, tambien permite hacer un
		update con el id del objeto, permitiendo hacer cambios.
		"""
	#----------------------------------------------------------
	# @METHOD: Elimina de la base de datos                     
	# @PARAMS: self                       
	#----------------------------------------------------------
	def delete_from_db(self):
		# Eliminar con sql alchemy
		db.session.delete(self)
		db.session.commit()
		"""
		#session.delete(objeto) PErmite eliminar una fila de datos
		como objeto de las tablas
		"""
	#----------------------------------------------------------
	# @CLASSMETHOD: Retorna toda la tabla de tiendas                        
	# @PARAMS:cls                        
	#----------------------------------------------------------
	@classmethod
	def find_all(cls):
		# all() -> retorna todos los datos de la tabla cada fila como objeto
		return cls.query.all()
#------------------------------------------------------------------------------