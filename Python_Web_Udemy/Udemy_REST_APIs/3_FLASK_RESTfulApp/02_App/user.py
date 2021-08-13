"""
# APLICACION FLASK REST FUL 2
Pequeña aplicacion de articulos(recursos) en una lista de articulos
que funciona como memoria interna del sistema com practica

CLASE USUARIO
"""
class Users:
	# Constructor - Estado inicial del objeto
	def __init__(self, _id, _username, _password):
		self.id = _id
		self.username = _username
		self.password = _password
	
