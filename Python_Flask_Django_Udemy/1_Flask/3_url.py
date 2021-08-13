"""
Flask->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
"""
# -------------------------------------------------------------------
# URL´S
# -------------------------------------------------------------------
# Importar librerias y paquetes
from flask import Flask
from flask import request
# -------------------------------------------------------------------
# FLASK APP INSTANCE
app = Flask(__name__)
# -------------------------------------------------------------------
# RUTAS
# Tomar toda informacion en una ruta
@app.route('/<data_url>')
def index(data_url="Mundo"):
	# Request del parametro
	data = request.args.get('data_url', data_url)
	# Retorno
	return "Hola {}".format(data);
#Ruta de Visa Sumador - toma los paramemtros despues de la ruta add/<params>
# Una funcion puede ser definida para distintas rutas
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
	# return "{} + {} = {}".format(num1, num2, int(num1) + int(num2))
	return "{} + {} = {}".format(num1, num2, num1 + num2)
# -------------------------------------------------------------------
# EJECUCIÓN
app.run(debug=True, port=8000)
