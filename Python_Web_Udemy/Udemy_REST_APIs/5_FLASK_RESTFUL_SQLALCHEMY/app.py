"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------
Archivo principal
"""
# Libreria Flask ------->
from flask import Flask
# Libreria Flask Restful ------->
from flask_restful import Api
# Libreria flask-jwt Tokens
from flask_jwt import JWT
# Funciones Seguridad (security.py) ------->
from security import authenticate, identity
# Clase Recurso registro de usuario (user.py) ------->
from resources.user import UserRegister
# Clases Recursos Articulos o Items (item.py) resources->carpeta-paquete.nombreArchivo ------->
from resources.item import Item, ItemsList
# Clase Recursos para Tiendas ------->
from resources.store import Store, StoreList
# Objeto db del archivo db(flask-sql-alchemy) ------->
from db import db
#------------------------------------------------------------------------------
# INSTANCIA FLASK
#------------------------------------------------------------------------------
app = Flask(__name__)

# CONFIGURACIONES SQLALCHEMY ------->
# Sqlite3 Data base file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# Track Modification
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Secret Key ------->
app.secret_key = 'MyAppSqlite3'
# Objeto JWT Tokens ------->
jwt = JWT(app, authenticate, identity)
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
#------------------------------------------------------------------------------
# EJECUCIÓN
#------------------------------------------------------------------------------
if __name__ == '__main__':
	# Iniciar nuestra base de datos
	db.init_app(app)
	app.run(port=5000, debug=True)