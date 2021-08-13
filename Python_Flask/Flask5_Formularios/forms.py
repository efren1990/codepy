"""
--------------------------------FORMULARIOS DE FLASK-----------------------------------------------------
Flask provee de formularios para captar datos en su libreira
los cuales permiten y facilitan el trabajo con datos captados
Se debe importar la clase Form
"""
# Clase Form libreria wtforms
from wtforms import Form
# Importar los tipos de campos a mostrar segun su tipo de dato
from wtforms import StringField, TextField, IntegerField, PasswordField
# Importar tipo de campo email
from wtforms.fields.html5 import EmailField
# Clase para ocultar campos de formulario
from wtforms import HiddenField
# Importar validadores de campos de wtforms
from wtforms import validators
# Importar la clase de usuario del archivo de modelos
from models import User
# -------------------------------------------------------------------------------
# VALIDADORES-> es un array con un conjunto de metodos que validan los campos
# -------------------------------------------------------------------------------
# Funcion honeypot para saber si el campo especial tiene datos porque fue modificado
def length_honeypot(form, field):
	# Contar el dato entrante si es > a 0 es porque hay datos de modificacion
	if len(field.data) > 0:
		# Crear error y enviar mensaje
		raise validators.ValidationError('I can See you boy ;)')
# Instaciar una clase para el formulario que hereda de la clase Form
class MiFormu(Form):
	# Los campos seran mostrados asignandoles el tipo de campo TipoCampo('Mostrara html')
	userName = StringField(
		'Usuario',
		[
			validators.Required(message='Ingresa el Usario...!'),
			validators.length(min=5, max=10, message='El usuario debe tener minimo 5 y maximo 10 caracteres')
		]	
	)
	edad = IntegerField(
		'Edad',
		[
			validators.Required(message='Ingresa tu edad.')
		]
	)
	email = EmailField(
		'Correo',
		[
			validators.Required(message='Ingresa tu Email.'),
			validators.Email(message='Ingrese un Email valido.')
		]
	)
	comentario = TextField(
		'Comentario',
		[
			validators.Required(message='Ingresa tu comentario...')
		]
	)
	honeypot = HiddenField('', [length_honeypot])

"""
Honeypot-> Tarro de miel
Consiste en crear un campo vacio oculto
como señuelo para detectar atacantes de spam
 el usuario normal no puede llenar este campo ya
 que el esta oculto
Es mas facil que realizar un captcha
"""
#------------------------------------------------------------------------------
# FORMULARIO LOGIN
#------------------------------------------------------------------------------
class FormularioLoguin(Form):
	username = StringField(
		'Usuario',
		[
			validators.Required(message="El Usuario es requerido"),
			validators.length(min=5, max=10, message="El usuario debe tener minimo 5 y maximo 10 caracteres")
		]
	)
	password = PasswordField(
		'Contraseña',
		[
			validators.Required(message="Ingrese una contraseña")
		]
	)

#------------------------------------------------------------------------------
# FUNCION PARA EVITAR DUPLICIDAD DE CAMPOS
#------------------------------------------------------------------------------
# Metodo para validar un nombre de usuario y evitar errores de duplicidad -
# El metodo sera llamado en el archivo main.py en la validacion de usuario
def validar_usuario(form, field):
	# Obtener el dato del usuario
	usuario = field.data
	# Consulta en la base de datos
	us = User.query.filter_by(usuario = usuario).first()
	# Validar si el usuario esta
	if us is not None:
		# Devolver mensaje de error
		raise validators.ValidationError('El usuario ya se encuntra registrado')	
#------------------------------------------------------------------------------
# FORMULARIO CREAR USUARIO
#------------------------------------------------------------------------------
class CrearUsuario(Form):

	usuario = StringField(
		'Usuario',
		[
			validators.Required(message="Completa el campo de Usuario"),
			validators.Length(min=6, max=12, message="El Usuario debe contener entre 6 y 12 caracteres"),
			validar_usuario #Metodo creado internamente
		]
	)
	email = StringField(
		'Email',
		[
			validators.Required(message="Completa el campo de Email."),
			validators.Email(message="Ingrese un Email Valido."),
			validators.Length(min=5, max=50, message='Ingrese un Email valido.')
		]
	)
	password = PasswordField(
		'Contraseña',
		[
			validators.Required(message="Completa el Campo Contraseña")
		]
	)
	
#------------------------------------------------------------------------------
# FORMULARIO COMENTARIO
#------------------------------------------------------------------------------
class form_comment(Form):
	commentario = TextField(
		'Comentario',
		[
			validators.Required(message="Debes incluir un comentario...")
		]
	)
