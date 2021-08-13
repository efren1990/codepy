"""
DESPLEGANDO HTML DE FORMA LARGA NO ADECUADA
Flask->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
"""
# -------------------------------------------------------------------
# LIBRERIAS
# -------------------------------------------------------------------
from flask import Flask
from flask import request
# -------------------------------------------------------------------
# INSTANCIA FLASK APP
# -------------------------------------------------------------------
app = Flask(__name__)
# -------------------------------------------------------------------
# RUTAS
# -------------------------------------------------------------------
# INDEX->
@app.route('/')
def index():
	return """
		<!DOCTYPE html>
		<html>
			<head>
				<title>Home</title>
			</head>		
			<body>
				<p>Hola Mundo</p>
			</body>
		</html>
	"""
# SUMADORA->
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
	return """
		<!DOCTYPE html>
		<html>
			<head>
				<title>Home</title>
			</head>		
			<body>
				<h1>Total</h1>
				<h2>{} + {} = {}</h2>
			</body>
		</html>
	""".format(num1, num2, num1 + num2)

# -------------------------------------------------------------------
# EJECUCIÓN
# -------------------------------------------------------------------
app.run(debug=True, port=8000)