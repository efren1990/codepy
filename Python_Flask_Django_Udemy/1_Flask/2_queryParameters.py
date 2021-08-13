"""
Flask->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
"""
# -------------------------------------------------------------------
# QUERY PARAMETERS
"""
Son los datos que van despues de signos de interrogacion en las
url, datos get

"""
# Libreria Flask
from flask import Flask
# Para trabajar con paramtros es necesario la librerua request
from flask import request
# ----------------------------------------------------
# FLASK APP
# Instacia de la clase Flask
app = Flask(__name__)
# ----------------------------------------------------
# RUTAS
@app.route('/')
def index():
	return 'home'
# Ruta Con Parametros
@app.route('/user')
def user(param_name='', param_lastname=''):
	# Tomar el parametro argumento con el metodo .get('nombre parametro', valorVariable)
	name = request.args.get('name', param_name)
	last_name = request.args.get('last_name', param_name)
	return "Hola {} {}".format(name, last_name)
# ----------------------------------------------------
# EJECUCION
app.run(debug=True, port=5000)