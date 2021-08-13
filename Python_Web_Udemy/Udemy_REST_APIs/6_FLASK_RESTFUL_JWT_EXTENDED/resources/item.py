"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------
Recurso de Items o Articulos
"""
# Recursos y analizardor de peticiones ------->
from flask_restful import Resource, reqparse 
# Required de tokens jwt - extended ------->
from flask_jwt_extended import (
			jwt_required, 
			get_jwt_claims, 
			jwt_optional, 
			get_jwt_identity,
			fresh_jwt_required
)
# Importar paquete de modelos carpeta models------->
from models.item import ItemModel
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
	# Argumento id tienda
	parser.add_argument(
			'store_id',
			type=int,
			required=True,
			help="Campo Requerido"
		)
	#----------------------------------------------------------
	# @METHOD: GET- Devuelve datos del item- Autenticable                    
	# @PARAMS: self, name                        
	#----------------------------------------------------------
	# Requerir token de autenticacion - actualizado o no
	@jwt_required
	def get(self, name):
		# Llamar metodo de clase que devuelve un item
		item = ItemModel.find_by_name(name)
		# Validar si no es none, encontro el dato
		# if item not is None: = if item:
		if item:
			# Retorno del objeto formato json
			# return {'message':item.name, 'price':item.price}
			return item.json()
		# Retornar mensaje
		return {'message':'El articulo no existe.'}, 400
	#----------------------------------------------------------
	# @METHOD: POST- Recibe e inserta datos de item                    
	# @PARAMS: self, name, json->precio                        
	#----------------------------------------------------------	
	# Decorador para pedir un token nuevo reffresh actualizado
	@fresh_jwt_required
	def post(self, name):
		# Validar si existe el item
		if ItemModel.find_by_name(name):
			return {'message':'El Articulo con el nombre de {} ya existe'.format(name)}, 400
		# Tomar los datos post
		data = Item.parser.parse_args()
		# Nuevo Objeto ItemModel
		new_item = ItemModel(name, data['price'], data['store_id'])
		# Päsar el nuevo item al metodo de insercion
		# Validar la excepcion si ocurre un error de inserion
		try:
			# Insertar item
			new_item.save_to_db()
			# Retornar el nuevo item + mensaje
			return {'message':'Articulo Creado', 'item':new_item.json()}, 201
		except:
			return {'message':'Ha ocurrido un error, intenta de nuevo mas tarde'}, 500 #Internal Server Error
	#----------------------------------------------------------
	# @METHOD: DELETE- Elimina articulo segun nombre                    
	# @PARAMS: self, name                        
	#----------------------------------------------------------
	@jwt_required
	def delete(self, name):
		# Pedir El reclamo claims
		claims = get_jwt_claims()
		# Validar si esta logeado
		if not claims['is_admin']:
			return {'message':'Necesitas iniciar session'}
		# Validar si el objeto exite
		item = ItemModel.find_by_name(name)
		if item is not None:
			# Eliminarlo de la base de datos
			item.delete_from_db()
		return {'message':'Artiulo eliminado'}
	#----------------------------------------------------------
	# @METHOD: PUT- Actualiza o crea un articulo                    
	# @PARAMS: self, name, json->precio                        
	#----------------------------------------------------------
	def put(self, name):
		# Tomar datos request
		data = Item.parser.parse_args()
		# Buscar El item
		item = ItemModel.find_by_name(name)
		# Validar si existe un item anterior
		if item is None: #Si no Exite es none
			# Instanciar un nuevo Item
			item = ItemModel(name, data['price'], data['store_id'])
		else: # Si existe
			# Setear el precio del objeto econtrado para actualizarlo
			item.price = data['price']
		# Salvar al final de la operacion ya sea uno nuevo o una actualizacion
		item.save_to_db()
		# Retorno del objeto en formato json
		item.json()
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# @CLASS: ITEMS LIST - RESOURCE
#------------------------------------------------------------------------------
class ItemsList(Resource):
	#----------------------------------------------------------
	# @METHOD: GET- Metodo para retornar la lista de articulos                        
	# @PARAMS: self                        
	#----------------------------------------------------------
	"""
	#COMENT->@jwt_optional
	puede agregar a cualquier punto final si el objeto JWT estara o no presente
	luego dentro del punto final se podra decidir si esta presente o no
	"""
	@jwt_optional
	def get(self):
		# Traer el id de la identidad 
		user_id = get_jwt_identity() # esto se puede debido al jwt_optional
		# Crear lista de items list comprehension
		items = [item.json() for item in ItemModel.find_all()]
		# Validar si el usuario existe como identidad
		if user_id:
			# Retornar la lista
			return {'items':items}, 200
		# Retornar parte de la lista y una peticion de logueo
		return {
			'items':[item['name'] for item in items],
			'message':'Inicia Session para ver más datos.'
		}, 200

		
#------------------------------------------------------------------------------