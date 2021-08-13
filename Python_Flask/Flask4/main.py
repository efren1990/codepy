"""
FLASK - ARCHIVOS ESTATICOS Y FUNCIONES MACRO
Flask permite el llamado de archivos script, imagenes, hojas de estilo, y frameworks frontend
Son llamados archivos estaticos statics
Flask permite crear funciones tipo macro las cuales permiten definir que contenido mostrar en las vistas
"""
# Libreria flask
from flask import Flask
# Modulo de render
from flask import render_template
# Instacia de clase Flask
app = Flask(__name__, template_folder = 'templates')
# Ruta Inicial
@app.route('/')
# Funcion de Ruta
def index():
	# Retorno del render
	return render_template('index.html')
# Validacion y ejecucion
if __name__ == '__main__':
	app.run(debug=True, port=8000)

