"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------------------
MODELS O MODELOS->
Nos permiten hacer interacciones con las base de datos directamente
pero no responden a las apis clientes 
Un Modelo es la represtacion Interna de nuestra Entidad
--------------------------------------------------------------------------
Modelo de Usuario
"""
import sqlite3
# Importar db alchemy(db.py) ------->
from db import db
#------------------------------------------------------------------------------
# @CLASS: USUARIOS - AUTENTICACION - HEREDA el MODEL de SQLALCHEMY OBJECT 
#------------------------------------------------------------------------------
"""
#COMENT->UserModel funciona como una API(Application programming interface) para el archivo de seguridad
el cual interactua con la base de datos y el usuario
"""
class UserModel(db.Model):
	#------------------------------------------------------------------------------
	# MODELO DB SQLALCHEMY TABLA USERS
	#------------------------------------------------------------------------------
	# DEFINIR TABLA DEL MODELO ------->
	__tablename__ = 'users'
	# ID
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	password = db.Column(db.String(80))
	#----------------------------------------------------------
	# @METHOD: Constructor                         
	# @PARAMS: id, nombreUsuario, contraseña                       
	#----------------------------------------------------------
	def __init__(self, username, password):
		self.username = username
		self.password = password
	#----------------------------------------------------------
	# @METHOD CLASS: Busca por nombre de usuario                        
	# @PARAMS: NombreUsuario           
	#----------------------------------------------------------
	@classmethod
	def find_by_username(cls, username):
		# Retorno del usuario con query flask alchemy por username
		return cls.query.filter_by(username=username).first()
	#----------------------------------------------------------
	# @METHOD CLASS: Busca por nombre de id usuario                        
	# @PARAMS: NombreUsuario           
	#----------------------------------------------------------
	@classmethod
	def find_by_id(cls, _id):
		# Retorno del usuario con query flask alchemy por id
		return cls.query.filter_by(id=_id).first()
	#----------------------------------------------------------
	# @METHOD CLASS: guarda un objeto en la base de datos                       
	# @PARAMS: self- en objeto en si            
	#----------------------------------------------------------
	def save_to_db(self):
		# Salvar objeto en db flask alchemy
		db.session.add(self)
		db.session.commit()
#------------------------------------------------------------------------------