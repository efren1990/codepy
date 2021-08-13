"""
ARCHIVO DE MODELOS
-------------------------------------------------------------------------------------------------
El archivo de modelos realiza las operaciones con la base de datos
de la aplicacion

Tambien se crearan los modelos de la aplicacion los cuales se integran con la base de datos

Se pueden usar ORM que son paquetes que interactuan con la base de datos sin necesidad
de conocer SQL como lenguaje de base de datos
Un ORM permite trabajar con los registros de una base de datos con Programacion Orintada a Objetos
si necesidad de saber lenguaje de base de datos

"""
# Importar modulos del ORM SQL-Alchemy
from flask_sqlalchemy import SQLAlchemy
# Importar Generador de hash de contraseñas
from werkzeug.security import generate_password_hash
# Importar Validador de Password encriptadas o textos
from werkzeug.security import check_password_hash
# Importar liireria de tiempo
import datetime

# Instaciar la clase Alchemy
db = SQLAlchemy()

# Clase para el modelo de Usuarios
class User(db.Model):
	# Definir el nombre de la tabla|
	__tablename__ = 'usuarios'

	# Cada atributo de la clase se convertira en una columna en la base de datos
	# Atributos->
	id = db.Column(db.Integer, primary_key=True)#Columna id, entero, Llave primaria, autoincremental
	usuario = db.Column(db.String(50), unique=True)#Columna usuario, string, unico
	email = db.Column(db.String(40)) #Columna email, texto 40 caracteres
	comments = db.relationship('Comment')#Campo para facilitar el relacionamiento
	password = db.Column(db.String(255)) #Columna password, string 255 caracteres- hash para pasword
	fecha_registro = db.Column(db.DateTime, default=datetime.datetime.now)#Columna fecha_regustro, fecha tiempo
	# Metodo inicial
	def __init__(self, us, passw, ema):
		self.usuario = us
		self.password = self.__create_password(passw) #Encriptar contraseña
		self.email = ema
	# Metodo privado para enciptar contraseña
	def __create_password(self, password):
		return generate_password_hash(password) #Metodo que encripta un texto en un hash de 66 caracteres
	# Metodo para Validar texto plano con texto encriptado
	def verify_password(self, texto):
		# Returna un True o False
		return check_password_hash(self.password, texto)
#------------------------------------------------------------------------------
# CLASE PARA EL MODELO DE LOS COMENTARIOS
#------------------------------------------------------------------------------
"""
Relaciones entre los modelos de uno a muchos
Un usuario pode tener muchos comentarios pero que un cometario
solo le pertenece a un usuario
"""
class Comment(db.Model):
	# Nombre de la base de datos
	__tablename__	= 'comentarios'
	# Atributos - campos de la tabla
	id = db.Column(db.Integer, primary_key=True)
	# Campo para unir los dos modelos o las dos tablas db.ForeingKey('tabla.campo') - relacionar los campos
	user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
	text = db.Column(db.Text())
	create_date = db.Column(db.DateTime, default = datetime.datetime.now)
