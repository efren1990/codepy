"""
TwitFace Aplicacion don python y flask
--------------------------------------------------------------------------------------------
ARCHIVO DE MODELOS
Se encargar de realizar las operaciones con la base de datos
"""
#------------------------------------------------------------------------------
# IMPORTACION
#------------------------------------------------------------------------------
# Tiempos
import datetime
# flask_login -> libreria para gestionar operaciones de login y sessiones de usuarios
from flask_login import UserMixin
# UserMixing->Clase que agrega funcionalidades de; activacion, autenticacion
# Libreria flask_bcrypt -> generate_password_hash-Genera hashin y encriptacion de datos / contraseñas
from flask_bcrypt import generate_password_hash
# Peewee
from peewee import *

#------------------------------------------------------------------------------
# BASE DE DATOS
#------------------------------------------------------------------------------
DATABASE = SqliteDatabase('social.db')
#------------------------------------------------------------------------------
# MODELOS DE LAS TABLAS PEEWEE
#------------------------------------------------------------------------------
# USUARIOS ------->
# La clase usuario tendra un mixin
# Mixing->Clase diseñada con el proposito de agregar funcionalidad a otras clases
class User(UserMixin, Model):
	# Campos-->
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField(max_length=120)
	fecha_regis = DateTimeField(default=datetime.datetime.now)
	# Class Meta Modelo-->
	class Meta:
		# Base de datos ->
		database = DATABASE
		# Ordenamietno de registros por fecha 
		order_by = ('-fecha_regis')
	# Metodo de la Clase y no de Instancia: Crear un Usuario ------->
	"""Metodo de la clase, el cual permite usarse sin instanciar
	la clase, por asi decir un metod estatico
			clase.metodoDeClase()
		"""
	@classmethod
	def create_user(cls, username, email, password):
	# cls es igual a self o this en otros lenguajes
	# Try para realizar operacion de crear registro de usuario
	# si que se inserten los mismos datos
		try:
			cls.create(
				username = username,
				email = email,
				password = generate_password_hash(password)
			)
		except IntegrityError:
			# Retornar el mensaje por el error de integridad
			# raise ValueError("El usuario ya existe")
			pass

# Metodo para crear tabla de usuarios
def initialize():
	# Conexion con bd
	DATABASE.connect()
	# Crear Tablas
	DATABASE.create_tables([User], safe=True)
	# Cerrar conexion
	DATABASE.close()