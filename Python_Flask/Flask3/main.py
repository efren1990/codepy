"""
FLASK Y ARCHIVOS ESTATICOS
Flask permite el llamado de archivos script, imagenes, hojas de estilo, y frameworks frontend
Son llamados archivos estaticos statics
"""
# Librerial flask
from flask import Flask
# modulo render de flask
from flask import render_template
# Instacia de la clase Flask
app = Flask(__name__, template_folder = 'templates')
# Rutas-->
@app.route('/')
# Funcion de ruta
def index():
	# Nombre titulo app
	title = "Curso Flask"
	# Rertorno del render
	return render_template('index.html', titulo = title)
# Validacion y ejecucion
if __name__ == '__main__':
	app.run(debug=True, port=8000)