"""
QUE ES FLASK--->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
--------------RENDERIZAR TEMPLATES--------------------------------------------------------------
"""
# Importar Framework Flask
from flask import Flask
# Para renderizar codigo html es necesario importar la libreria de flask 
from flask import render_template
# Instacia clase Flask
app = Flask(__name__, template_folder = 'carpTemplate')
# Definir ruta inicial
@app.route('/')
def index():
	# Retorno del render del template el cual reconocera la carpeta de almacenamiento
	return render_template('index.html')

# Validacion y ejecucion
if __name__=='__main__':
	app.run(debug = True, port=5000)