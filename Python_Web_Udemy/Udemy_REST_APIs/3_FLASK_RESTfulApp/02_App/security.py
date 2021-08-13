"""
# APLICACION FLASK REST FUL 2
Pequeña aplicacion de articulos(recursos) en una lista de articulos
que funciona como memoria interna del sistema com practica

SEGURIDAD DE DATOS USUARIO
"""
# Libreria util para comprar cadenas de forma segura
from werkzeug.security import safe_str_cmp
# Importar la clase User del archivo user.py
from user import Users
# Tabla en la memoria para los usuarios registrados / como bd practica
# users_db = [
# 	{
# 		'id': 1,
# 		'username': 'bob',
# 		'password': '123_4' 
# 	}
# ]
users_db = [
	Users(1, "bob", '123_4')
]
"""Diccionario de mapeo de usuario por nombre de usuario,
	para evitar iterarlo cada vez que se necesite un dato de usuario
"""
# user_mapping = {
# 	'bob':{
# 		'id': 1,
# 		'username': 'bob',
# 		'password': '123_4' 
# 	}
# }
"""Diccionario de mapeo de usuario por id"""
# user_id_mapping:{
# 	1:{
# 		'id': 1,
# 		'username': 'bob',
# 		'password': '123_4'
# 	}
# }
# Mapeo creado una comprension establecida
user_mapping = {us.username: us for us in users_db}
user_id_mapping = {us.id: us for us in users_db}
#------------------------------------------------------------------------------
# FUNCION PARA AUTENTICAR UN USUARIO
#------------------------------------------------------------------------------
def authenticate(username, password):
	# Encontrar un usuario por nombre de usuario usando metod get(Clave, defaul-value) diccionarios
	user = user_mapping.get(username, None)
	# Validar los datos devueltos en el diccionario mapeado
	if user and safe_str_cmp(user.password, password):
		# Retornar el usuario
		return user
#------------------------------------------------------------------------------
# FUNCION IDENTITY DE FLASK JWT - JASON WEB TOKEN
#------------------------------------------------------------------------------
def identity(payload):
	# Extrar el id de usuario de la carga util o payload
	user_id = payload['identity'] #Accede a la identidad devuelta por el objeto JWT 
	return user_id_mapping.get(user_id, None)
