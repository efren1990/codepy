"""
--------------------------------FORMULARIOS DE FLASK-----------------------------------------------------
Flask provee de formularios para captar datos en su libreira
"""
# Importar la clase flask libreria flask
from flask import Flask

# Importar la libreria de render 
from flask import render_template
# Libreri Request para hacer peticiones url
from flask import request
# Importar clase para la proteccion de ataque sifer(Csrf) Cross site
from flask_wtf.csrf import CSRFProtect
# Importar make_response el cual se usa para crear cookies 
from flask import make_response
# Importar session para crear sesiones
from flask import session
# Importar redirect y url_for para realizar redirecciones en flask
from flask import redirect
from flask import url_for
"""
Importar la clase de las configuraciones de entornos y de la app
en el archivo config.py
"""
from config import DevelopmentConfig
# Importar de models la instancia de SQLAlchemy con la base de datos archivo models.py
from models import db
from models import User
from models import Comment
# Importar flash para enviar mensajes con flask
from flask import flash
"""Importar el objeto g el cual permite trabajar con cualquier variable
dentro de una misma peticion, es un objeto global y se puede acceder en 
cualquier momento, despues del after_request morira.
Dos clientes no comparten el mismo objeto g
Sierve como puente de comunicacion entre
El before_request()
La funcion de ruta
El after_request()
"""
from flask import g
# Importar libreria para operaciones json
import json
# MODULOS PROPIOS---------------------------------------------------------------------------------------
# Importar modulo forms el cual contiene la clase para nuestros formularios
import forms
# Importar funcion del archivo helpers.py para formatear una fecha numerica
from helpers import date_format
#-------------------------------------------------------------------------------------------------------
# Instancia clase flask Flask(__name__)
app = Flask(__name__, template_folder="templates")
# La llave secreta-> Se usa para evitar ataques de Cross-site request forgery el cual consiste
# en enviar datos de una pagina externa a la nuestra,
# app.secret_key = 'palabra secreta compleja pero es mejor usar variables de session'
# app.secret_key = 'mySecretKey_3443[dsds]_dwedqw'
# Pasar el debug y la llave secreta a la aplicacion
app.config.from_object(DevelopmentConfig)
# Pasar aplicacion al protector, creando una nueva instancia
# csrf = CSRFProtect(app)
csrf = CSRFProtect() # -> De esta forma se le pasan las configuraciones en el if de arranque
#Rutas--------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# @RUTAS: NO EXISTENTES / ERROR 404
#------------------------------------------------------------------------------
# errorhandler(404)->manejador de error, recibe entero con numero de error
# Se pueden agregar diferentes manejadores de errores para cada caso
@app.errorhandler(404)
# La funcion recibe el parametro error e
def page_not_found(e):
	return render_template('error.html'), 404
#------------------------------------------------------------------------------
# @RUTA: INDEX 
#------------------------------------------------------------------------------
"""
DECORADORES RESPONSE Y REQUEST
----------------------------------------------------------------------------
Se usan para realizar operaciones antes de que la url sea ejecutada por la
funcion de ruta, por ejemplo las conexiones con base de datos
"""

# @app.before_request->Se ejecuta antes de que las peticiones llegue a la funcion
@app.before_request
def before_request():
	"""Todo lo que valla dentro de la funcion before_request
	se ejecutara antes de cada peticion request de rutas

	Se puede usar para hacer validaciones en session de usuario
	"""
	print("Before request")
	# Devolver el nombre de ruta a la que se esta accediendo por el request
	print(request.endpoint)
	# Pasar un dato al objeto global g
	# g.nombreVaraible = dato
	g.test = 'test g'
	if request.endpoint == "index":
		print("Estamos en el: index")
	# Validar urls a las que puede entrar un usuario autenticado(logueado) y uno que no
	if 'username' not in session and request.endpoint in ['registro']:
		# si no esta autenticado(si el nombre de variable de session esta en la lista session) 
		# y se encuentra en la seccion de registro de mensajes
		# enviarlo al login
		return redirect(url_for('login'))

# -----------------------------------------------------------------------------------
# @app.after_request->Se ejecuta desues de que las peticiones llegue a la funcion
"""
La funcion del decorador after_request debe llevar siempre un parametro respuesta
para que se pueda retornoar lo que se envie en las otras funciones de ruta
"""
@app.after_request
def after_request(response):
	print("Se ejecuta despues de que la funcion de la ruta pedida en el reques termine")
	return response
#------------------------------------------------------------------------------
# @RUTA: Index
#------------------------------------------------------------------------------
@app.route('/')
def index():
	# Imprimir variable creada en objeto g.variable
	print(g.test)
	return render_template('index.html')
#------------------------------------------------------------------------------
#  @RUTA: REGISTRO DE USUARIO
#------------------------------------------------------------------------------
@app.route('/registro', methods=["GET", "POST"])
# Funcin Ruta 1
def registro():
	# instanciar la clase para formularios
	# form.MiFormu(request.form) -> Valida si llegaron datos del formulario
	# creando una instancia con los datos que mando el cliente sino hara una nueva
	miFormulario = forms.MiFormu(request.form)
	# Si el metodo de acceso ala url es POST y si las validaciones se realizaron
	# El metodo validate()-> se encarga de ejecutar los validadores de los campos de formulario
	if request.method == 'POST' and miFormulario.validate():
		# Impirmir los datos del formulario
		print(miFormulario.userName.data)
		print(miFormulario.edad.data)
		print(miFormulario.email.data)
		print(miFormulario.comentario.data)
	else:
		print("Error en el Formulario")

	# Titulo
	tit = 'Formularios'
	# Retorno del Template
	return render_template('registro.html', titulo = tit, form = miFormulario)
#------------------------------------------------------------------------------
# @RUTA: LOGIN
#------------------------------------------------------------------------------
@app.route('/login', methods=["GET", "POST"])
def login():
	print(g) #-> objeto global g
	# Instanciar la clase del formulario de login
	login_form = forms.FormularioLoguin(request.form)
	# Validar peticion request del loguin
	if request.method == 'POST' and login_form.validate():
		# Validar Usuario -> pasar datos de formulario
		usu = login_form.username.data
		passwo = login_form.password.data
		# Consulta en base de datos accediendo al modelo User
		user = User.query.filter_by(usuario = usu).first() # SELECT * FROM usuarios WHERE usuario = usu LIMIT 1
		# Si la consulta no regresa nada dara como resultado un None dentro del obejto 
		# Validar si no es None la consulta y la contraseña con el metodo creado en el modelo User
		if user is not None and user.verify_password(passwo):
				# Validar la contraseña

			"""
				SESSIONS O SESIONES EN FLASK
				Las sesiones sirven para tener conocimiento sobre que es lo que pasa entre
				el cliente y el servidor, flask trabaja sesiones basadas en cookies, las cuales
				se encriptaran por la llave secreta y se transpotaran en los request
				Crear variable de sesiom->
				SESSION['nombre de variable'] = valor o dato
			"""
			session['username'] = usu
			session['id'] = user.id #pasar el id del usuario en la consulta
			# Retornar el template renderizado
			"""flask permite enviar mensajes por aparte,
			success_message = 'Mensaje'
			flash(success_message)
			"""
			us = login_form.username.data
			success_message = 'Bienvenido {}'.format(us)
			flash(success_message)
			# Redireccionar al Index
			return redirect(url_for('index'))

		else:
			error_message = 'Usuario o Contraseña incorrectos'
			flash(error_message)

	return render_template('login.html', form=login_form)
#------------------------------------------------------------------------------
# @RUTA: COOKIES
#------------------------------------------------------------------------------
@app.route('/cookie')
def cookie():
	"""
		Las cookies no trabajan sobre el objeto response
		para esto se usa make_response, el cual crea una respuesta, crea la cookie
	"""
	# Instanacia del response
	response = make_response(render_template('cookie.html'))
	# Crear la cookie
	response.set_cookie('cooki_personalizada', 'DgeneratioX')
	return response
#------------------------------------------------------------------------------
# @RUTA: EJEMPLO PARA IMPRIMIR COOKIES
#------------------------------------------------------------------------------
@app.route('/printer')
def printer():
	tit = 'Cookinis'
	# Traer el valor de la cookie
	# undefine se enviara si no se encuetra la cookie
	myCookies = request.cookies.get('cooki_personalizada', 'undefine')
	# Validar las session como ejercicio para imprimirla en consola
	# session es un diccionario de valores
	if 'username' in session:
		print(session['username'])
	# Retorno del template
	return render_template('printer.html', titulo=tit, cook=myCookies)
#------------------------------------------------------------------------------
# @RUTA: LOGOUT PARA DESTRUIR VARIABLES DE SESSION
#------------------------------------------------------------------------------
@app.route('/logout')
def logout():
	if 'username' in session:
		# Eliminar la session
		session.pop('username')

	return redirect(url_for('login'))
	# redirect(url_for('NombreDeFuncionDeRuta'))-> se usa para redirigir 
#------------------------------------------------------------------------------
# @RUTA: OPERACIONES CON AJAX / Solo operaciones con el metodo POST
#------------------------------------------------------------------------------
"""La ruta que se envia en ajax debe ser la misma que en el decorador de @app"""
@app.route('/ajax-login', methods=["POST"])
# Funcion para procesar peticion ajax del javascript
def ajax_login():
	# Devolver los campos del mismo formulario del login
	# Se debe acceder al campo con el nombre que se asigno en la clase del formulario
	data = request.form['username']
	# Respuesta simulada - diccionario
	response = {'status':200, 'user':data, 'id':1, 'rol':'bg', 'r':1}
	# Retornar la respuesta en formato json
	return json.dumps(response) 
#------------------------------------------------------------------------------
# @RUTA: CREAR USUARIOS
#------------------------------------------------------------------------------
@app.route('/crear', methods=["GET", "POST"])
# Funcion de ruta: crear usuarios
def crear():
	# Insanciar el fromulario
	my_form = forms.CrearUsuario(request.form)
	# Validar ejecucion del formulario
	if request.method == "POST" and my_form.validate():
		# Insertar usuario en base de datos con SQLAlchemy
		# ------------------------------------------------
		# Instancia de la Clase User del modelo en models.py
		user = User(my_form.usuario.data,
								my_form.password.data,
								my_form.email.data)
		# Agregar el objeto que hereda de models para preparar la transaccion con la bd
		db.session.add(user)
		# Ejecutar la operacion
		db.session.commit()
		# Con SQLAlchemy no es necesario cerrar la conexion porque lo hace auitomaticamente

		# Enviar Mensajes Con flash
		success_message = 'Usuario Registrado en la Base de Datos'
		flash(success_message)
		
	return render_template('crear.html', form=my_form)
#------------------------------------------------------------------------------
# @RUTA: LISTADO DE COMENTARIOS - PAGINACIÓN
#------------------------------------------------------------------------------
@app.route('/reviews/', methods=['GET'])
@app.route('/reviews/<int:page>', methods=['GET'])#Ruta para paginar url
def reviews(page=1):
	"""Traer el listado de comentarios de la base de datos, uniendolo
 	con la tabla de usuarios""" 
 	# ClaseModelo.query.join(ClaseModeloUnir).add_columns(ClaseModelo.campoTabla)
 	# .paginate(PagianActual, CantidadElementosPagina, False->no genera errro 404 si no hay registros) 
	reg_page = 3 # Registros por pagina
	# Consulta
	comment_list = Comment.query.join(User).add_columns(User.usuario, 
																											Comment.text,
																											Comment.create_date).paginate(page, reg_page, False)
	# .paginate no es un elemento iterable entonces es necesario en el for hacer el cambio .items
	title = "Pagianción"
	t = "Comentarios:"
	# Renderizar y enviar datos - date_format ->funcion para formatear fecha
	return render_template('reviews.html', titulo=title, c_title=t, comm=comment_list, fd_format = date_format)

#------------------------------------------------------------------------------
# CREAR UN COMENTARIO CON RELACION ENTRE MODELOS O TABLAS
#------------------------------------------------------------------------------
@app.route('/comm', methods=["GET", "POST"])
def comment():
	# Instacia del forrmulario
	my_form_comment = forms.form_comment(request.form)
	# Validar la ejecucion del formulario
	if request.method == "POST" and my_form_comment.validate():
		# Pasar el id de usuario
		id_us = session['id']
		# Instacia la clase del modelo de comentarios
		comment_db = Comment(user_id = id_us,
											text = my_form_comment.commentario.data) 
		# Ejecutar consulta
		db.session.add(comment_db)
		db.session.commit()
		# Flash del mensaje
		success_message = 'Nuevo comentario creado'
		flash(success_message)
	# Titulo
	tit = 'Comentarios'
	# Retornar el template
	return render_template('comment.html', titulo=tit, form=my_form_comment)
#------------------------------------------------------------------------------
# EJECUCION
#------------------------------------------------------------------------------
# Validar el archivo actual para la ejecucion
if __name__ == '__main__':
	# Iniciar las configuraciones con la instancia del sifer
	csrf.init_app(app)
	# Pasar las configuraciones generales a la aplicacion
	db.init_app(app) # Toma las configuraciones de alchemy
	# Crear las tablas que no estan creadas si no esta en las baase de datos / si esta no la crea
	# Sincronizar la base de datos con la aplicacion
	with app.app_context():
		db.create_all() 	
	# Ejecutar la app
	app.run(port = 5000)