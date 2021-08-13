"""
QUE ES FLASK--->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
--------------HERENCIA DE PLANTILLAS EN FLASK--------------------------------------------------------------
FLASK permite trabajar plantillas para no repetir codigo html y asi poder
pasar los datos personalizados a cada respuesta de plantilla
ej: una seccion donde cada usuario es diferente
"""
# Llamado de la libreria flask
from flask import Flask
# Llamado de la libreria de render
from flask import render_template
# Insatacia de la clase Flask y folder de tamplates
app = Flask(__name__, template_folder='carpTemplate')

# Definición de ruta
@app.route('/plantillas/<dtaUrl>/')
# Funcion de ruta EXPLICACION
def plantillas(dtaUrl):
	# Retorno del render del template con los datos de respuesta
	return render_template('plantillas.html', dtNom = dtaUrl)

# Defición otra ruta
@app.route('/cliente')
# Funcion de ruta
def cliente():
	# Datos de respuesta
	dtsLista = ['Dato-1', 'Dato-2', 'Dato-3']
	# Retorno del template renderizado con datos de envio
	return render_template('cliente.html', lista = dtsLista)
# Confirmacion y ejecucion de la app
if __name__ == '__main__':
	app.run(debug=True, port=5000)