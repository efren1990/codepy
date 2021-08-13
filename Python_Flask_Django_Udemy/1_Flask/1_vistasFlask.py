"""
Flask->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
"""
# Llamado de la libreria Flask
from flask import Flask
"""Para utilizar flask es necesario crear una instacia de la clase Flask
	El objeto Flask recibe como parametro la constante __name__
"""
app = Flask(__name__)
# -------------------------------------------------------------------
# VISTAS
"""
Las vistas se encargan de definir que le vamos a desplegar o mostrar
a los usuarios y son basicamente funciones o metodos que definimos
dentro de nuetra aplicacion.

Par que una vista sea mostrada se debe crear una ruta
@app.route(url de la vista)

"""
@app.route('/') #->Ruta inicial cuano no hay ningun parametro url
# Definir la vista index la cual es una funcion
def index():
	return "Hola Usuario, Esta app inicia aca con Flask"
# Otra ruta
@app.route('/login')
# Funcion de vista - se recomienda que lleve el mismo nombre de la ruta, 
def login():
	return "Login de Usuarios"

# -------------------------------------------------------------------
# run()-> se encarga de ejecutar el servidor y por ende la app flask
# debug=True -> muestra un debug de errores, False si se emplea en un servidor online
# port=numero ->define el puerto de salida
app.run(debug=True, port=5000)