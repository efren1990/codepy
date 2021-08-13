"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------
Modelo de Usuario
"""
# Libreria sqlite3 ------->
import sqlite3
# Libreria Flask Restful - Resource ------->
from flask_restful import Resource, reqparse
#------------------------------------------------------------------------------
# @CLASS: USUARIOS - AUTENTICACION 
#------------------------------------------------------------------------------
class Users():
	#----------------------------------------------------------
	# @METHOD: Constructor                         
	# @PARAMS: id, nombreUsuario, contraseña                       
	#----------------------------------------------------------
	def __init__(self, _id, _username, _password):
		self.id = _id
		self.username = _username
		self.password = _password
	#----------------------------------------------------------
	# @METHOD CLASS: Busca por nombre de usuario                        
	# @PARAMS: NombreUsuario           
	#----------------------------------------------------------
	@classmethod
	def find_by_username(cls, username):
		# Conectar con las base de datos
		connection = sqlite3.connect('data.db')
		# Cursor
		cursor = connection.cursor()
		# Consulta - busqueda por nombre de usuario
		select_query = "SELECT * FROM users WHERE username=?"
		# Ejecutar y tomar el resultado - recibe tupla
		result = cursor.execute(select_query, (username,))
		# Tomar la primera fila de la consulta la cual es la contenedora de los datos
		# de no haber resultados devolvera None
		row = result.fetchone()
		# Si el resultado no es None
		if row is not None:
			# Crear una variable para el objeto usuario, para devolver el usuario encontrado,
			# Se usa palabra reservada cls y no el nombre de la clase, para crear un objeto dentro de la clase
			"""cls(row[0], row[1], row[2]) = cls(*row)"""
			user = cls(*row)
		else: #El usario es None
			user = None
		# Cierre de Conexion
		"""
		#COMENT-> No es necesario hacer un comit porque no se estan insertando ni guardando datos
		"""
		connection.close()
		# Retornar el usuario
		return user
	#----------------------------------------------------------
	# @METHOD CLASS: Busca por nombre de id usuario                        
	# @PARAMS: NombreUsuario           
	#----------------------------------------------------------
	@classmethod
	def find_by_id(cls, _id):
		# Conectar con las base de datos
		connection = sqlite3.connect('data.db')
		# Cursor
		cursor = connection.cursor()
		# Consulta - busqueda por id de usuario
		select_query = "SELECT * FROM users WHERE id=?"
		# Ejecutar y tomar el resultado - recibe tupla
		result = cursor.execute(select_query, (_id,))
		# Tomar la primera fila de la consulta la cual es la contenedora de los datos
		# de no haber resultados devolvera None
		row = result.fetchone()
		# Si el resultado no es None
		if row is not None:
			# Crear una variable para el objeto usuario, para devolver el usuario encontrado,
			# Se usa palabra reservada cls y no el nombre de la clase, por ser un metodo de clase
			"""cls(row[0], row[1], row[2]) = cls(*row)"""
			user = cls(*row)
		else: #El usario es None
			user = None
		# Cierre de Conexion
		"""
		#COMENT-> No es necesario hacer un comit porque no se estan insertando ni guardando datos
		"""
		connection.close()
		# Retornar el usuario
		return user 
#------------------------------------------------------------------------------

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
		if Users.find_by_username(data['username']) is not None:
			return {"message":"El nombre de usuario ya existe"}, 400
		# Conexion ------->
		connection = sqlite3.connect('data.db')
		# Cursor
		cursor = connection.cursor()
		# Query Insertar
		query_insert = "INSERT INTO users VALUES(NULL, ?, ?)"
		# Ejecutar query
		cursor.execute(query_insert, (data['username'], data['password'],))
		# Commit y Cierre
		connection.commit()
		connection.close()
		# Retorno de mesaje satisfactorio
		return {"message":"El usuario ha sido creado"}, 201
#------------------------------------------------------------------------------