"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------
Seguridad de las autenticaciones de usuario
"""
# Librerias, Modelo user.py ------->
from werkzeug.security import safe_str_cmp
from user import Users

#------------------------------------------------------------------------------
# @FUNCTION: Valida y Autentica un usuario
#------------------------------------------------------------------------------
def authenticate(username, password):
	# Uso del metodo de clase para buscar en la bd el usuario en la clase User
	user = Users.find_by_username(username)
	# Validar los datos de usuario devueltos por el modelo Users
	if user and safe_str_cmp(user.password, password):
		# Retorno de usuario
		return user
#------------------------------------------------------------------------------
# @FUNCTION: VALIDA IDENTIDAD SEGUN JWT TOKEN
#------------------------------------------------------------------------------
def identity(payload):
	# Extrar el id de la identidad obtenida como parametro
	user_id = payload['identity']
	# Retorno del usuario con el metodo de clase que consulta por id
	return User.find_by_id(user_id)
