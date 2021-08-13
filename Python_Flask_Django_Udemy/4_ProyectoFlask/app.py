"""
Archivo para la ejecucion de la Aplicacion
-------------------------------------------------------------------------------------------
"""
# Importar clase Flask y 
# g (objeto global) para almacenar todo lo que se requiere de la aplicacion haciendolo
# accesible desde cualquier lado del proyecto
from flask import (Flask, g, render_template, flash, url_for, redirect)
# Importar clase para contraseñas desemcrip
from flask_bcrypt import check_password_hash
# Importar modelos del archivo models.py
import models
# Importar Formularios del archivo forms.py
import forms
# Importar login manager
from flask_login import LoginManager, login_user, login_required
# VARIABLES GLOBALES
DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

# Instacia de la App
app = Flask(__name__)
# Llave secreta para identificar la aplicacion de otras que esten en la web
# La llave secreta tiene que ser un texto largo preferiblemente aleatorio
app.secret_key = 'dderteferertert112533554dddf_:,..[sdsdsEERWERW]_dsdsdsd'

# LOGIN MANAGER
# -----------------------------------------------------------------------------
# Instancia del Login manager
login_manager = LoginManager()
# Iniciar el login manager en la aplicacion
login_manager.init_app(app)
# Metodo login_view -> se usa para definit la vista que va a ser llamada y
# desplegada al usuario, cuando se quiere iniciar session o cuando sean redirigidos
login_manager.login_view = 'login'
# -----------------------------------------------------------------------------
# LOGIN MANAGER
# -----------------------------------------------------------------------------
"""
Metodo para cargar el usuario que esta logueado
el metodo debe llevar el decorador @flas
"""
@login_manager.user_loader
def load_user(user_id):
	try:
		# Validar los usuarios con flask_login
		return models.User.get(models.User.id == user_id)

	except models.DoesNotExist: #Si el usuario no existe
		# Retornar None
		return None
# -----------------------------------------------------------------------------
"""
Metodos de Convencion en Flask, utilizados para llamarse antes y despues
de hacer una peticion de nuetra base de datos

before_request() -> Establecer conexiones con base de datos
after_request() -> Se usa para cerrar la conexion

Los metodos no necesariamente debe ser llamados de esta forma
pero por convencion se suele usar estos nombres
"""
# Metodos de Convecion - deben llevar su decorador @app.metodo
# -----------------------------------------------------------------------------
@app.before_request
def before_request():
	""" Conecta a la base de datos antes de cada peticion"""
	# Llamado del objeto global flask
	# g.db = propiedad para definir la base de datos
	g.db = models.DATABASE #Base de datos del archivo models.py DATABAE
	# Validar si esta cerrada la conexion
	if g.db.is_closed():
		# Conectar con la base de datos
		g.db.connect()
# -----------------------------------------------------------------------------
@app.after_request
def after_request(response):
	"""Cierre de conexion con la base de datos"""
	g.db.close()
	# Retorno de respuesta
	return response
#------------------------------------------------------------------------------
# RUTAS
#------------------------------------------------------------------------------
# Ruta Registro--------------------->
@app.route('/registro', methods=('GET', 'POST'))
def register():
	# Instaciar el dormulario
	form = forms.RegisterForm()
	# Validar si no hubo inconveniente en las validaciones de campos
	if form.validate_on_submit():
		flash('Fuiste Registrado!!!', 'success')
		# Crear el Usuario o insertarlo en la base de datos
		models.User.create_user(
				username = form.username.data,
				email = form.email.data,
				password = form.password.data
		)
		# Al crear el usuario redirigir a la pagina de inicio
		return redirect(url_for('index'))
	# Retornar la vista de registro
	return render_template('register.html', form=form)
@app.route('/')
def index():
	return 'Index'
# Ruta Login--------------------->
@app.route('/login', methods=('GET', 'POST'))
def login():
	# Instaciar la clase LoginForm del modulo forms.py
	form = forms.LoginForm()
	# Validar el pase de los validators
	if form.validate_on_submit():
		try:
			# Consulta para validar si el usario existe
			user = models.User.get(models.User.email == form.email.data)
		
		except models.DoesNotExist:
			flash('Tu nombre de usuario o cotraseña no Existen.', 'error')
		else:
			# Verificar el password
			if check_password_hash(User.password, form.password.data):
				# Iniciar session con el metodo de flask
				login_user(user)
				# flash()->Encia mensajes
				flash('Has iniciado Sesión', 'success')
				# REdirigir al index
				return redirect(url_for('index'))
	# Retornar el render del template y enviar el formulario creado
	return render_template('login.html', form=form)		

# Ruta Logout--------------------->
@app.route('/logout')
# Decorador que solo permite la vista si el usuario esta logueado
@login_required
def logout():
	# Cerrar la sesion del usuario
	logout_user()
	# Enviar mensaje
	flash('Has Cerrado Sesion', 'success')
	# REdirigir al index
	return redirect(url_for('index'))
# -----------------------------------------------------------------------------
# Validar y ejecutar metodo de main
if __name__ == '__main__':
	# Insertar usuario quemado
	models.initialize()
	models.User.create_user(
		username='Cosme',
		email='cosmeFulanito@gmail.com',
		password='cosme1234' 
	)
	app.run(debug=DEBUG, host=HOST, port=PORT)





