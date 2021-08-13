"""
ARCHIVO PARA CONTROLAR LOS FORMULARIOS
-------------------------------------------------------------------------------------------

"""
# Importar modulo formularios de flask
from flask_wtf import FlaskForm
# Importar campos de wtforms
from wtforms import StringField, PasswordField, TextAreaField
# Importar validdores de formularios
from wtforms.validators import (DataRequired, ValidationError, Email, Regexp, Length, EqualTo)
# Importar modelos
from models import User
#------------------------------------------------------------------------------
# CLASE PARA FORMULARIO DE REGISTROS
#------------------------------------------------------------------------------
# Funcion para validar si un nombre de usuario ya existe, recive el formulario 
# y el campo, es llamada como un validador dentro de la clase de formulario, los
# parametros de la funcion se pasaran automaticamente
def name_exist(form, field):
	# Query para hacer consult select from where que valida si el nombre usuario ya existe
	if User.select().where(User.username == field.data).exists():
		# Retornar un error de validacion
		raise ValidationError('Ya usuario ya esta registrado.')
# Funcion para validar si el email ya existe
def email_exist(form, field):
	# Query que consulta si el email ingresado ya existe
	if User.select().where(User.email == field.data).exists():
		raise ValidationError('El Email Ya esta registrado.')
# Hereda de la clase FlaskForm
class RegisterForm(FlaskForm):
	# Campo de Usuario
	username = StringField(
		'Username',#Nombre del campo
		#Validadores->Para validar campos
		validators=[
			DataRequired(), #Valida si hay datos en el campo
			Regexp(r'^[a-zA-Z0-9_]+$'), #Valida una expresion regular
			name_exist #Funcion agregada
	])
	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(), #Valida si es un email escrito correctamente
			email_exist
		]	
	)
	password = PasswordField(
		'Password',
		validators = [
			DataRequired(),
			Length(min=6),
			EqualTo('password2', message="Los password deben coincidir") #valida si los dos campos de contraseña son iguales			
		]
	)
	password2 = PasswordField(
		'Confirm Password',
		validators=[DataRequired()]
	)
#------------------------------------------------------------------------------
# CLASE PARA EL FORMULARIO DE LOGIN
#------------------------------------------------------------------------------
class LoginForm(FlaskForm):
	# Campo Email
	email = StringField('Usuario - Email', validators = [DataRequired(), Email()])
	# campo password
	password = PasswordField('Contraseña', validators = [DataRequired()])
	