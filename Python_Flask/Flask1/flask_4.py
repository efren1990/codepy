 """
QUE ES FLASK--->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
--------------RUTAS CON VARIOS PARAMESTROS X/X/X--------------------------------------------------------------
"""
# Llamado de la libreria flask la clas Flask
from flask import Flask
# Para trabajar con parametros en necesario importar la libreria request
from flask import request
"""Para utilizar flask es necesario crear una instacia de la clase Flask
	El objeto Flask recibe como parametro la constante __name__
"""
app = Flask(__name__)

# RUTAS----------------------------------------------------
@app.route('/') #wrap o decorador
def index():
	return 'Hola mundo'
# Una app puede tener mas de una ruta las cuales funcionarian como las secciones de la app
# Las rutas debe ir seguidas de su respectiva funcion de retorno
# El parametro de la ruta para ser activda debe ser el mismo dentro de @app.route('/nombre ruta')
@app.route('/ruta2')
def ruta2():
	return 'otro contenido...'
# RUTAS CON PARAMETROS----------------------------------------------------
# Dentro de las rutas se pueden recibir parametros get ?varParametro = dato
@app.route('/rtaParametros/')
@app.route('/rtaParametros/<name>/')
@app.route('/rtaParametros/<name>/<int:num>/')
def rtaParametros(name = 'string', num = 'numero'):
	return 'Los parametros son: {}, {}'.format(name, num)
# http://localhost:8000/rtaParametros/jucan/2345/
# Validacion y ejecucion
if __name__ == '__main__':
	app.run(debug = True, port = 8000)
