"""
PRIMERA APLICACION FLASK
-----------------------------------------------------------------
"""
# importar clase Flask del paquete flask
from flask import Flask
# Instanciar la clase Flask
# Indicar A Flask que la aplicacion se esta corriendo en un unico lugar
app = Flask(__name__)
# RUTEO------------------->
"""
Se usa para crear las rutas de acceso a la aplicacion web
"""
@app.route('/') # Ruta raiz o root
# Cada ruta puede tener una funcion
def home():
	return "Hola Mundo!!!"

# Ejecutar la aplicacion
app.run(port=5000, debug=True)
