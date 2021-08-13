"""
QUE ES FLASK--->
Flask es un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones. 
Y antes de preguntar: ¡es con licencia BSD!
--------------VARAIBLES EN HTML--------------------------------------------------------------
"""
# Importar libreria flask
from flask import Flask
# Libreira render
from flask import render_template
# Instaciar clase flask y pasar folder de templates
app = Flask(__name__, template_folder = "carpTemplate")
# Rutas--->
@app.route('/usuario/<nameUsuario>')
def usuario(nameUsuario):
	# Retornar el render del template correspondiente
	# Al pasar las variables al metodo render_template se podran imprimir en el template
	# Se pueden mandar varios tipos de datos , listas, tuplas, diccionarios
	edad = 15
	hobies = ['Correr', 'Saltar', 'Nadar']
	return render_template('usuario.html', nombre = nameUsuario, edadUs = edad, otros = hobies)

# Confirmacion y ejecucion de la app
if __name__ == '__main__':
	app.run(debug=True, port=5000)
