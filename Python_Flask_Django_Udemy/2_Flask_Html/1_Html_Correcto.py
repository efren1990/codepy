"""
Flask->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
DESPLEGANDO HTML DE FORMA ADECUADA Y CORRECTA
-------------------------------------------------------------------------------------
Para mostrar diferentes vistas de nuestra aplicacion es necesario
crear un folder para los templates donde se crear los archivos html
a mostrar
El folder debe ser llamado templates por convencion

"""
# -------------------------------------------------------------------
# LIBRERIAS
# -------------------------------------------------------------------
from flask import Flask
from flask import request
# Para renderizar un templata html debe usarse la libreria 
from flask import render_template
# -------------------------------------------------------------------
# INSTANCIA APP FLASK
# -------------------------------------------------------------------
app = Flask(__name__)
# -------------------------------------------------------------------
# RUTAS
# -------------------------------------------------------------------
# Index->
@app.route('/')
def index():
	""" Para renderizar el template debe usarse el metodo render_template
			render_template('archivo.html')->no debe incluirse en nombre de 
			la carpeta templates"""
	return render_template('index.html')

# Servicios->
@app.route('/service')
def service():
	return "Esta es la vista sin plantilla"

# Calculadora-> 
"""Se pueden enviar variables a nuestros templates por medio
del metodo render_template("archivo", variables, , , ....)"""
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
	
	return render_template('add.html', n1=num1, n2=num2)
# -------------------------------------------------------------------
# EJECUCIÓN
# -------------------------------------------------------------------
app.run(debug=True, port=8000)