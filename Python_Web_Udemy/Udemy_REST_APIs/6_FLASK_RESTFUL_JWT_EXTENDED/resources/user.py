"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------
RESOURCE O RECUROS->
Son los que responden a peticiones de las apis clientes e interactuan
con la base de dato.
Un Recurso es la Representacion externa de una entidad
Recurso-> Registro de usuario
"""
# Libreria sqlite3 ------->
import sqlite3
# Libreria Flask Restful - Resource ------->
from flask_restful import Resource, reqparse
# Required de tokens jwt - extended ------->
from flask_jwt_extended import jwt_required
# Seguridad werkzeug
from werkzeug.security import safe_str_cmp
# Flask JWT Extended crear tokens
from flask_jwt_extended import (
		 create_access_token, 
		 create_refresh_token, 
		 jwt_refresh_token_required,
		 get_jwt_identity, 
		 jwt_required, 
		 get_raw_jwt
)
# SET PARA LA LISTA NEGRA
from blacklist import BLACKLIST
# Importar paquete de modelos
from models.user import UserModel
#------------------------------------------------------------------------------
# @CLASS: REGISTRO DE USUARIOS - HERDA:Resource
#------------------------------------------------------------------------------
class UserRegister(Resource):
	# ANALIZADOR DE PETICIONES - PARSER ------->
	parser = reqparse.RequestParser()
	parser.add_argument('username',
			type=str,
			required=True,
			help="Campor requerido"
		)
	parser.add_argument('password',
			type=str,
			required=True,
			help="Campor requerido"
		)
	#----------------------------------------------------------
	# @METHOD: POST-Registra un usuario                        
	# @PARAMS: Self                     
	#----------------------------------------------------------
	def post(self):
		# Captar datos recibidos - parseados
		data = UserRegister.parser.parse_args()
		# Validar si el usuario exite
		if UserModel.find_by_username(data['username']) is not None:
			return {"message":"El nombre de usuario ya existe"}, 400
		# Crear un nuevo objeto y guardarlo con el metodo que usa flask alchemy
		# Pasando como parametro el diccionarion desempaquetado
		user = UserModel(**data)
		# Guardar el objeto
		user.save_to_db()
		# Retorno de mensaje
		return {'message':'El usuario se creo correctamente'}		
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# @CLASS: USER - @HEREDA: Resource
#------------------------------------------------------------------------------
class User(Resource):

	#----------------------------------------------------------
	# @CLASSMETHOD: GET - Envia un usuario por id                        
	# @PARAMS: self, id usuario                        
	#----------------------------------------------------------
	@classmethod
	def get(self, user_id):
		# Buscar el usuario por el id
		user = UserModel.find_by_id(user_id)
		# Validar si no encontro el usuario
		if not user:
			# Retorno mensaje
			return {'message':'El usuario no existe'}, 404
		# Retornar el usuario formateado
		return user.json()

	#----------------------------------------------------------
	# @CLASSMETHOD: DELETE - Elimina un usuario por id                        
	# @PARAMS: self, id usuario                        
	#----------------------------------------------------------
	@classmethod
	def delete(self, user_id):
		# Buscar el usuario por id
		user = UserModel.find_by_id(user_id)
		# Validar si no encontro
		if not user:
			return {'message':'El usuario no existe'}, 404
		# Llamar el metodo que elimina del model
		user.delete_from_db()
		# Enviar mensaje
		return {'message':'El usuario ha sido eliminado'}, 200
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# @CLASS: LOGIN DE USUARIOS - HEREDA:Resource
#------------------------------------------------------------------------------
class UserLogin(Resource):
	#------------------------------------------------------------------------------
	# PARAMETROS - PARSER
	#------------------------------------------------------------------------------
	# ANALIZADOR DE PETICIONES - PARSER ------->
	parser = reqparse.RequestParser()
	parser.add_argument('username',
			type=str,
			required=True,
			help="Campo requerido"
		)
	parser.add_argument('password',
			type=str,
			required=True,
			help="Campo requerido"
		)
	#----------------------------------------------------------
	# @CLASSMETHOD: POST                        
	# @PARAMS: cls                        
	#----------------------------------------------------------
	@classmethod
	def post(cls):
		# Tomar los datos del parser
		data = cls.parser.parse_args()
		# Buscar el usuario en la base de datos
		user = UserModel.find_by_username(data['username'])
		# Validar password
		if user and safe_str_cmp(user.password, data['password']):
			# Crear token de acceso, fresh=True-> esta reciente o fresco
			access_token = create_access_token(identity=user.id, fresh=True)
			# Crear token refresh
			refresh_token = create_refresh_token(user.id)
			# Retornar los tokens
			return {
				'access_token':access_token,
				'refresh_token':refresh_token
			}, 200
		# Usuario invalido
		return {'message':'Datos de usuario invalidos'}, 401
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# @CLASS: LOGOUT DE USUARIOS - HEREDA:Resource
#------------------------------------------------------------------------------
class UserLogout(Resource):
	@jwt_required
	#----------------------------------------------------------
	# @METHOD: POST - Cierre de session                        
	# @PARAMS:                        
	#----------------------------------------------------------
	def post(self):
		"""Para realizar el cierre de session es necesario pasar el token
		creado incialmente para el usuario que se logea y pasarlo a la lista
		negra, el cual quedara inutilizable y tendra que logerase de nuevo"""
		# Cada token tiene un id unico
		jti = get_raw_jwt()['jti'] #jti es JWT ID identificador unico del token
		# Agregarlo a la lista negra el cual es un set en el archibo blacklist.py
		BLACKLIST.add(jti)
		return {'message':'Has cerrado seccio satisfactoriamente'}		
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# @CLASS: REFRESCA TOKENS - HEREDA:Resource
#------------------------------------------------------------------------------
class TokenRefresh(Resource):
	#----------------------------------------------------------
	# @METHOD:POST- Recibe datos para refrescar el token                     
	# @PARAMS:self                      
	#----------------------------------------------------------
	"""#COMENT->Recibe el token de actualizacion que se crea
	inicialemente y lo pasa como actulizacion del access_token"""
	@jwt_refresh_token_required
	def post(self):
		# Como se ha creado un token de actualizacion en el login
		#Significa que podemos utilizarlo para obtener una identidad jwt
		current_user = get_jwt_identity()
		# Crear el nuevo token con la identidad obtenida, fresh=False, no es reciente es token de actualizacion
		new_token = create_access_token(identity=current_user, fresh=False)
		# Retorno del nuevo token de acceso refresh
		return {'access_token':new_token}, 200
#------------------------------------------------------------------------------