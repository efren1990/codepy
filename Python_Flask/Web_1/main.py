"""
--------------------------------------------------------------------------------------------
																			WEB CON FLASK
--------------------------------------------------------------------------------------------
"""
# Archivo main quien contiene el proceso de rutas y acciones de la app
#-------------------------------------------------------------------------------------------

# Libreria flask
from flask import Flask
# Libreria render flask
from flask import render_template
#*------------------------------------------------------------------------------------------
# Instancia Clase flask
app = Flask(__name__, template_folder='templates')
# Ruta 1 - Inicial(home o index)
@app.route('/')
# Funcion de ruta - Home
def home():
	#retorno template home
	return render_template('home.html')

# Ruta 2 - nosotros
@app.route('/nosotros')
def about():
	# Retorno del template
	return render_template('nosotros.html')

# Ruta 3 - servicios
@app.route('/servicios')
def service():
	# Retorno de la vista
	return render_template('servicios.html')
#*------------------------------------------------------------------------------------------
#*------------------------------------------------------------------------------------------
# Confirmar archivo main y ejecutar servidor de la app
if __name__ == '__main__':
	# Metodo run para correr el servidor
	app.run(debug=True, port=8500)
#*------------------------------------------------------------------------------------------
