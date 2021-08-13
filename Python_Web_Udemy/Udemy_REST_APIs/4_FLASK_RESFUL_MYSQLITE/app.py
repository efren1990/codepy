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
from user import UserRegister
# Clases Recursos Articulos o Items (item.py) ------->
from item import Item, ItemsList
#------------------------------------------------------------------------------
# INSTANCIA FLASK
#------------------------------------------------------------------------------
app = Flask(__name__)
# Secret Key ------->
app.secret_key = 'MyAppSqlite3'
# Objeto JWT Tokens ------->
jwt = JWT(app, authenticate, identity)
#------------------------------------------------------------------------------
# API REST FUL
#------------------------------------------------------------------------------
api = Api(app)
#------------------------------------------------------------------------------
# AÑADIR RECURSOR API
#------------------------------------------------------------------------------
api.add_resource(Item, '/item/<string:name>') # Get Item
api.add_resource(ItemsList, '/items') #Get Items
api.add_resource(UserRegister, '/register') #Register User
#------------------------------------------------------------------------------
# EJECUCIÓN
#------------------------------------------------------------------------------
if __name__ == '__main__':
	app.run(port=5000, debug=True)