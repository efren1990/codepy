"""
#APLICACION FLASK RESTFUL SQLITE3 - JWT EXTENDED
----------------------------------------------------------------
Archivo principal
"""
# Libreria Flask ------->
from flask import Flask
# Libreria Flask Restful ------->
from flask_restful import Api
# Libreria flask-jwt-extended Manager
from flask_jwt_extended import JWTManager
# Clase Recurso registro de usuario (user.py) ------->
from resources.user import UserRegister, User, UserLogin, TokenRefresh, UserLogout
# Clases Recursos Articulos o Items (item.py) resources->carpeta-paquete.nombreArchivo ------->
from resources.item import Item, ItemsList
# Clase Recursos para Tiendas ------->
from resources.store import Store, StoreList
# Objeto db del archivo db(flask-sql-alchemy) ------->
from db import db
from blacklist import BLACKLIST
from flask import jsonify
#------------------------------------------------------------------------------
# INSTANCIA FLASK
#------------------------------------------------------------------------------
app = Flask(__name__)

# CONFIGURACIONES SQLALCHEMY ------->
# Sqlite3 Data base file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# Track Modification
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Propagacion de errores
app.config['PROPAGATE_EXCEPTIONS'] = True
# Habilitar la lista negra
app.config['JWT_BLACKLIST_ENABLED'] = True
# Definir para que token se habilita la lista negra|
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

# Secret Key ------->
app.secret_key = 'MyAppSqlite3'
#------------------------------------------------------------------------------
# OBJETO JWT EXTENDED
#------------------------------------------------------------------------------
# Objeto JWT-EXTENDED ------->
jwt = JWTManager(app)
"""
#COMENT->@jwt.user_claims_loader
Se encarga de hacer reclamos de nuestras identidades o usuarios registrados
alo loguearse, tambien linqueara la funcion al objeto JWTManager
"""
"""Cada vez que se crea un token de acceso se ejecutara la funcion asociada
al decorador, esto para ver si se deberian agregar datos extra a ese JWT
La identidad o identity sera lo que pasemos al access_token (identity=user.id)
el cual llevara el valor del id del usuario"""
@jwt.user_claims_loader
def add_claims_to_jwt(identity):
	if identity == 1: # el 1 representara el usuario - puede ser buscado en la base de datos
		# Si existe entonces dar el permiso
		return {'is_admin':True}
	# Negar permiso
	return {'is_admin':False}
#------------------------------------------------------------------------------
# CONFIGURACION DECORADORES JWT EXTENDED
#------------------------------------------------------------------------------
# Decorador para validar tokens en la black list ------->
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
	# La funcion retornara True si el token esta en la lista negra
	# retorno 
	return decrypted_token['jti'] in BLACKLIST
# Cuando el tiempo del toke finalizo y expiro el token ------->
@jwt.expired_token_loader
def expired_token_callback():
	return jsonify({
			'description':'El Token ha espirado',
			'error':'token_expired'
		}), 401
# Cuando se envia un Token invalido, manipulacion de cabeceras ------->
@jwt.invalid_token_loader
def invalid_token_callback(error):
	return jsonify({
			'description':'Verificacion de Token fallada',
			'error':'invalid_token'
		}),401
# Cundo nos envian un token no autrizado ------->
@jwt.unauthorized_loader
def missing_token_callback(error):
	return jsonify({
			'description':'La peticion no contiene el token de acceso',
			'error':'authorization_required'
		}),401
# Cuando nos envian un token que no es fresh y es necesario por un: fresh_jwt_required ------->
@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
	return jsonify({
			'description':'Token no actualizado',
			'error':'fresh_token_required'
		}), 401
# Se usa para agregar un token de un usuario que ya ha cerrado session y esta en la lista de revocados ------->
@jwt.revoked_token_loader
def revoked_token_callback():
	return jsonify({
			'description':'El token ha sido removido',
			'error':'token_revoked'
		}), 401
#------------------------------------------------------------------------------
# API REST FUL
#------------------------------------------------------------------------------
api = Api(app)
#------------------------------------------------------------------------------
# DECORADOR BEFORE_FIRST_REQUEST - Antes de la primera peticion o ejecucion
#------------------------------------------------------------------------------
@app.before_first_request
# Crar la base de datos y sus tablas
def create_tables():
	# Creara la base de datos definida en la configuracion uri
	# Tambien crara las tablas definidas en las clases de los modelos
	db.create_all()
#------------------------------------------------------------------------------
# AÑADIR RECURSOR API
#------------------------------------------------------------------------------
api.add_resource(Item, '/item/<string:name>') # Get Item
api.add_resource(ItemsList, '/items') #Get Items
api.add_resource(UserRegister, '/register') #Register User
api.add_resource(Store, '/store/<string:name>') # Store- get, post, delete
api.add_resource(StoreList, '/stores') #StoreListe- get
api.add_resource(User, '/user/<int:user_id>') # users - get, delete
api.add_resource(UserLogin, '/login') #Login de usuario
api.add_resource(UserLogout, '/logout') #Cierre de session
api.add_resource(TokenRefresh, '/refresh') #Refresh de token
#------------------------------------------------------------------------------
# EJECUCIÓN
#------------------------------------------------------------------------------
if __name__ == '__main__':
	# Iniciar nuestra base de datos
	db.init_app(app)
	app.run(port=5000, debug=True)