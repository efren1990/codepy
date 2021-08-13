"""
QUE ES FLASK--->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
--------------METODO RUN--------------------------------------------------------------
"""
# Llamado de la libreria flask la clas Flask
from flask import Flask

"""Para utilizar flask es necesario crear una instacia de la clase Flask
	El objeto Flask recibe como parametro la constante __name__
"""
app = Flask(__name__)


@app.route('/') #wrap o decorador
def index():
	return 'Hola mundo'
	

# run()-> se encarga de ejecutar el servidor
# Run puede responder en el puerto que le indiquemos
# La cantidad de puertos que tiene nuestra computadora es 2**16
# de los cuales los primeros 1024 ya se encuentran ocupados
# debug = true permite realizar cambion sin necesidad de correr la consola en cada cambion
# Validacion de buenas practicas flask
if __name__ == '__main__':
	app.run(debug = True, port = 8000)