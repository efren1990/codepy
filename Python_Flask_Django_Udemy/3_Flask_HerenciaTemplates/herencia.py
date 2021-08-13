"""
--------------HERENCIA DE PLANTILLAS EN FLASK--------------------------------------------------------------
FLASK permite trabajar plantillas para no repetir codigo html y asi poder
pasar los datos personalizados a cada respuesta de plantilla
ej: una seccion donde cada usuario es diferenten

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
app = Flask(__name__, template_folder="templates")
# -------------------------------------------------------------------
# RUTAS
# -------------------------------------------------------------------
# Index->
@app.route('/')
@app.route('/<name>')
def index(name="Mundo"):
	# Diccionario de datos
	context = {'k_name':name}
	# Envio de Diccionario desempaquetado y renderizacion
	return render_template('index.html', **context)

# -------------------------------------------------------------------
# EJECUCIÓN
# -------------------------------------------------------------------
app.run(debug=True, port=8000)
