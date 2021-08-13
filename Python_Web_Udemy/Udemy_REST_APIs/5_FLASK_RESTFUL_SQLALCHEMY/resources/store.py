"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------
Recurso de Stores o tiendas
"""
# Recursos y analizaro de peticiones ------->
from flask_restful import Resource, reqparse
# Importar modelos store.py ------->
from models.store import StoreModel

#------------------------------------------------------------------------------
# @CLASS: RESOURCE STORE @HEREDA: RESOURCE
#------------------------------------------------------------------------------
class Store(Resource):
	#----------------------------------------------------------
	# @METHOD: GET                        
	# @PARAMS: self, name                        
	#----------------------------------------------------------
	def get(self, name):
		# Obtener la tiene del modelo
		store = StoreModel.find_by_name(name)
		# Validar si la tienda es encotrada
		if store is not None:
			# Retornar la tienda llamando el metodo json() del modelo 
			return store.json()		
		# Retornar que no se encontro la tienda
		return {'message':'La tienda no se encuentra'}, 404
	#----------------------------------------------------------
	# @METHOD: GET                        
	# @PARAMS: self, name                        
	#----------------------------------------------------------
	def post(self, name):
		# Validar si la tienda existe, la consulta enviara None de no ser asi
		if StoreModel.find_by_name(name):
			# Retornar que la tienda ya existe
			return {'message':'La tienda {} ya existe'.format(name)}, 400
		# De no existir - crear una nueva
		store = StoreModel(name)
		try:
			store.save_to_db()
		except:
			return {'message':'Un error ha ocurrido.'}, 500
		# Retornar la tienda creda
		return store.json(), 201
	#----------------------------------------------------------
	# @METHOD: GET                        
	# @PARAMS: self, name                        
	#----------------------------------------------------------
	def delete(self, name):
		# Validar si la tienda a eliminar exite
		store = StoreModel.find_by_name(name)
		if store is not None:
			# Eliminar la tienda
			store.delete_from_db()
		# Se elimine o no	
		return {'message':'La tienda ha sido eliminada'}

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# @CLASS: RESOURCE STORE LIST @HEREDA: RESOURCE
#------------------------------------------------------------------------------
class StoreList(Resource):
	#----------------------------------------------------------
	# @METHOD: GET                        
	# @PARAMS: self                      
	#----------------------------------------------------------
	def get(self):
		return {'Stores':[store.json() for store in StoreModel.query.all()]}