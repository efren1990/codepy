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