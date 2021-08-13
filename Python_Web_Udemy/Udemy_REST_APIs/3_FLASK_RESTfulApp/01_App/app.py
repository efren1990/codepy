"""
PRIMERA APLICACION FLASK - RESTFUL
-----------------------------------------------------------------
"""
# Importar librerias flask y flaskrestfull
from flask import Flask
from flask_restful import Resource, Api
#------------------------------------------------------------------------------
# INSTANCIA FLASK
#------------------------------------------------------------------------------
app = Flask(__name__)
#------------------------------------------------------------------------------
# INICIAR NUESTROS RECURSOS DE LA API FLASK_RESTFUL
#------------------------------------------------------------------------------
"""
La api rest ful  de python funcina con recursos los recursos son estructuras
de datos u objetos.
cada recurso es una clase
Cada clase debe Heredar de la clase Resource de la libreria flask_restful
"""
api = Api(app)
# Recurso para la api flask restful ------->
class Student(Resource):
	# Metodo para devolver el nombre
	def get(self, name):
		return {'student': name}
# Agregar el recurso(clase) a la api ------->
"""Al agregar un recurso a la api sera accesible por medio de ella
	y adicionalemte se debe crear la ruta con los respectivos parametros 
	que la misma recibira"""
api.add_resource(Student, '/student/<string:name>') # 'http://127.0.0.1:5000/student/parametro'

#------------------------------------------------------------------------------
# EJCUTAR EL SERVIDOR
#------------------------------------------------------------------------------
app.run(port=5000	);