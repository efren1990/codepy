"""
QUE ES FLASK--->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
"""
# Llamado de la libreria flask la clas Flask
from flask import Flask

"""Para utilizar flask es necesario crear una instacia de la clase Flask
	El objeto Flask recibe como parametro la constante __name__
"""
app = Flask(__name__)

@app.route('/') #wrap o decorador
def index():
	return 'Hola mundo, mi primera web'

# run()-> se encarga de ejecutar el servidor

app.run()