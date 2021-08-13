"""
QUE ES FLASK--->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
--------------RUTAS Y PARAMETROS--------------------------------------------------------------
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
@app.route('/rtaParametros')
def rtaParametros():
	#los paramatro son los pasados en la url por medio de una variable
	#request.arqs.get(nomVarParamtro,....,parNo) trae los datos url
	#y por defecto debe ir un dato que confirma la no existencia de datos ingresados
	parametro = request.args.get('dato1', 'noHayDatos')
	parametro2= request.args.get('dato2', 'noHayDatos')
	return 'El parametro o dato es: {}, {}'.format(parametro, parametro2)
	#http://localhost:8000/rtaParametros?dato1=dato 1&dato2=dato 2
# Validacion y ejecucion
if __name__ == '__main__':
	app.run(port = 5000)