"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------
Modelo de Items o Articulos
"""
# sqlite3 ------->
import sqlite3
# Recursos y analizardor de peticiones ------->
from flask_restful import Resource, reqparse 
# Required de tokens jwt ------->
from flask_jwt import jwt_required
#------------------------------------------------------------------------------
# @CLASS: ITEM-RESOURCE
#------------------------------------------------------------------------------
class Item(Resource):
	# parser de campos validos
	parser = reqparse.RequestParser()
	# Argumento Precio
	parser.add_argument(
			'price',
			type=float,
			required=True,
			help="Campo Requerido"
		)
	#----------------------------------------------------------
	# @CLASSMETHOD: Busca un articulo por nombre                    
	# @PARAMS: self, name                        
	#----------------------------------------------------------
	@classmethod
	def find_by_name(cls, name):
		# Conexion
		# Conexion
		connection = sqlite3.connect('data.db')
		# cursor
		cursor = connection.cursor()
		# Query
		select_query = "SELECT * FROM items WHERE name=?"
		# Resultado del query
		result = cursor.execute(select_query, (name,))
		# Obtener unica fila
		row = result.fetchone()
		# Cierre de Conexion
		connection.close()
		# Validar si no es none, encontro el dato
		# if row not is None: = if row:
		if row:
			# Retorno del los datos
			return {'item':{'id':row[0], 'name':row[1], 'price':row[2]}}
		# De lo contrario, Retornar None
		return None
	#----------------------------------------------------------
	# @CLASSMETHOD: Inserta un articulo                     
	# @PARAMS: self, Item-diccionario                        
	#----------------------------------------------------------
	@classmethod
	def insert_item(cls, new_item):
		# Conexion
		connection = sqlite3.connect('data.db')
		# Cursor
		cursor = connection.cursor()
		# Query
		query_insert = "INSERT INTO items VALUES(NUll, ?, ?)"
		# Ejecutar consulta
		cursor.execute(query_insert, (new_item['name'], new_item['price']))
		# Comit - Salvar datos
		connection.commit()
		# Cerrar conexion
		connection.close()


	#----------------------------------------------------------
	# @CLASSMETHOD: Actualizar un articulo                     
	# @PARAMS: self, Item-diccionario                        
	#----------------------------------------------------------
	@classmethod
	def update_item(cls, new_item):
		# Conexion
		connection = sqlite3.connect('data.db')
		# Cursor
		cursor = connection.cursor()
		# Query
		query_insert = "UPDATE items SET price=? WHERE name=?"
		# Ejecutar consulta
		cursor.execute(query_insert, (new_item['price'], new_item['name']))
		# Comit - Salvar datos
		connection.commit()
		# Cerrar conexion
		connection.close()

	#----------------------------------------------------------
	# @METHOD: GET- Devuelve datos del item- Autenticable                    
	# @PARAMS: self, name                        
	#----------------------------------------------------------
	# Requerir token de autenticacion
	# @jwt_required()
	def get(self, name):
		# Llamar metodo de clase que devuelve un item
		item = self.find_by_name(name)
		# Validar si no es none, encontro el dato
		# if item not is None: = if item:
		if item:
			# Retorno del los datos
			return item
		# Retornar mensaje
		return {'message':'El articulo no existe.'}, 400
	#----------------------------------------------------------
	# @METHOD: POST- Recibe e inserta datos de item                    
	# @PARAMS: self, name, json->precio                        
	#----------------------------------------------------------		
	def post(self, name):
		# Validar si existe el item
		if self.find_by_name(name):
			return {'message':'El Articulo con el nombre de {} ya existe'.format(name)}, 400
		# Tomar los datos post
		data = Item.parser.parse_args()
		# Nuevo item
		new_item = {'name':name, 'price':data['price']}
		# Päsar el nuevo item al metodo de insercion
		# Validar la excepcion si ocurre un error de inserion
		try:
			# Insertar item
			self.insert_item(new_item)
			# Retornar el nuevo item + mensaje
			return {'message':'Articulo Creado', 'item':new_item}, 201
		except:
			return {'message':'Ha ocurrido un error, intenta de nuevo mas tarde'}, 500 #Internal Server Error
	#----------------------------------------------------------
	# @METHOD: DELETE- Elimina articulo segun nombre                    
	# @PARAMS: self, name                        
	#----------------------------------------------------------
	def delete(self, name):
		# Validar si el objeto a eliminar existe
		if self.find_by_name(name):
			# Conexion
			connection = sqlite3.connect('data.db')
			# Cursor 
			cursor = connection.cursor()
			# Query delete
			query_delete = "DELETE FROM items WHERE name = ?"
			# Ejecutar consulta
			cursor.execute(query_delete, (name,))
			# Guardar y cierre
			connection.commit()
			connection.close()
			return {'message':'El articulo {}, ha sido eliminado'.format(name)}
		else:
			return {'message':'El articulo no existe'}, 400
	#----------------------------------------------------------
	# @METHOD: PUT- Actualiza o crea un articulo                    
	# @PARAMS: self, name, json->precio                        
	#----------------------------------------------------------
	def put(self, name):
		# Tomar datos request
		data = Item.parser.parse_args()
		# Crear nuevo Item
		new_item = {'name':name, 'price':data['price']}
		# Buscar El item
		item = self.find_by_name(name)
		# Validar si existe un item anterior
		if item is None: #Si no Exite es none
			# Intenta
			try:
				# Crearlo nuevo
				self.insert_item(new_item)
				return {'message':'El item {} ha sido creado'.format(name)}
			
			except:
				# Retorno de mensaje
				return {'message':'Ha ocurrido un error, intenta de nuevo mas tarde'}, 500 #Internal Server Error

		else: # Si existe
			# Intenta
			try:
				# Actualizar el anteriro metodo de actulizacion
				self.update_item(new_item)
				return {'message':'Articulo actulizado', 'Datos Ateriores':item, 'Datos Nuevos':new_item}
			except:
				# Retorno de mensaje
				return {'message':'Ha ocurrido un error, intenta de nuevo mas tarde'}, 500 #Internal Server Error			
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# @CLASS: ITEMS LIST - RESOURCE
#------------------------------------------------------------------------------
class ItemsList(Resource):
	#----------------------------------------------------------
	# @METHOD: GET- Metodo para retornar la lista de articulos                        
	# @PARAMS: self                        
	#----------------------------------------------------------
	def get(self):
		# Conexion
		connection = sqlite3.connect('data.db')
		# Cursor
		cursor = connection.cursor()
		# Query
		query_insert = "SELECT * FROM items"
		# Ejecutar consulta tomar resultado
		result = cursor.execute(query_insert)
		# Pasar toda la tabla de items
		items_list = result.fetchall()
		# Cerrar conexion
		connection.close()
		# Retorno de un diccionario con la lista
		return {'message':'','items':items_list}
#------------------------------------------------------------------------------