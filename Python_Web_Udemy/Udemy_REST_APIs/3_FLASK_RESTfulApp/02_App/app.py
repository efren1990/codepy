"""
# APLICACION FLASK REST FUL 2
Pequeña aplicacion de articulos(recursos) en una lista de articulos
que funciona como memoria interna del sistema com practica"""

#------------------------------------------------------------------------------
# Imporatcion
#------------------------------------------------------------------------------
from flask import Flask, request
# reqparse->permite controlar los datos que se pasan a traves de una solicitud http
from flask_restful import Resource, Api, reqparse
# Importar flask-wjt para crear tokens de autenticacion de usuarios (jason web tokens)
from flask_jwt import JWT, jwt_required
# Importar las funciones del archivo security.py
from security import authenticate, identity
#------------------------------------------------------------------------------
# INSTACIA FLASK
#------------------------------------------------------------------------------
app = Flask(__name__)
# Llave secreta ------->
# La llave secreta sera usada como un hash para encriptar datos 
app.secret_key = 'myApp'
# Instacia del objeto JWT el cual recibe como parametro la app y las funciones de seguridad
# para realizar la autenticacion de usuarios
jwt = JWT(app, authenticate, identity) #/auth
"""
Al Instaciarse el objeto JWT se crea un nuevo endpoint(ruta) llamada /auth
Cuando es llamado este endpoint le enviamos un nombre de usuario y una contraseña
el objeto JWT toma esos datos y los envia a la funcion authenticate los cuales
los compara con los datos mapeados del diccionario de usuarios registrados en la bd
si los datos coninciden con los enviados en el endpoint, este retornar un usuario
el cual se convierte en una identidad(identity) payload['identity'] - el token
esta identidad es validada en la funcion identity(payload)
El jwt token no hace nada en si, pero podemos enviarlo a la proxima solicitud que hagamos
cuando enviamos un JW Token lo que hace el objeto JWT es llamar la funcion identity(payload)
y luego usa el jw token para obtener la identificacion del usuario del diccionario de id de usuarios
con el cual traera los datos de usuario que ese id representa segun el jwtoken 
y si se completa esto quiere decir que el usario fue autenticado correctamente
"""
#------------------------------------------------------------------------------
# API REST FUL
#------------------------------------------------------------------------------
api = Api(app)
# Lista de items - memoria temoporal ------->
items_list = []
#------------------------------------------------------------------------------
# RECURSOS -> CLASE ARTICULOS
#------------------------------------------------------------------------------
#NOTA: No es necesario usar jsonify porque flask_restful retorna todo en json, 
# sin embargo solo se pueden retornar diccionarios ------->
class Item(Resource):
	# Instaciar objeto que permite analizar la peticion o request - reqparse
	parser = reqparse.RequestParser()
	"""
	El parser permitira filtrar los elementos de la peticion
	y solo permitir los definidos en el parser
	Dejarlo como elemento de la clase para eviar sobreescribir codigo
	"""
	parser.add_argument('price',
												type=float,
												required=True,
												help="Este Campo no puede estar vacio.!!!"
											 )
	# Decorador que require una autenticacion de usuario antes de llamar el metodo
	# Esta autenticacion sera llevada acabo por el objeto JWT que valida el token jw token
	@jwt_required()
	# Metodo para devolver el nombre-------------------------------------------------------------------------
	def get(self, name):
		"""# Retornar datos del item segun su nombre
				for item in items_list:
				# Si el nombre es igual al parametro de la ruta funcion
					if item['name'] == name:
						# retornar el item 
						return item
		"""
		"""Funcion lambda para flitrar y ahorar codigo con bucle for
			La función filter() devuelve un iterador donde los elementos se filtran a través de una función 
			para probar si el elemento es aceptado o no.  
			filter(function, lista,diccionario,tupla_iterable)
		"""
		item = next(filter(lambda item: item['name'] == name, items_list), None)

		# Si el item no es None, quiere decir que el item esta 200, si es None el item no esta 404
		return item, 200 if item is not None else 404 

	# Metodo para crear un articulo/item----------------------------------------------------------------------
	def post(self, name):
		"""Tomar el dato tipo json de la peticion post, asociado al precio del producto
				variable = request.get_json()
				Para evitar un error por la llegada de datos que no son tipo json o contenidos vacios del cliente
				se puede usar como parametro lo siguiente
				force = True -> No es necesario definir el tipo de contenido en la peticion cliente(json/xml/etc) lo formateara, pero es mejor no usarla 
				silent = True -> No devuelve error, los cancela
		"""
		# Validar que el nombre articulo no exista ya, es decir si el resultado del filtro es diferente de None
		# if nex(filter(lambda iten: item['name'] == name, items_list), None) is not None:
		if next(filter(lambda item: item['name'] == name, items_list), None):
			return {'message':"El Articulo con el nombre {} ya fue creado".format(name)}, 400
			# Si el usuario hace una mala peticion error 400	
		# Tomar el dato parseado
		data_price = Item.parser.parse_args()
		new_item = {'name':name, 'price':data_price['price']}
		# Anñadir el item a la lista
		items_list.append(new_item)
		# Retornar el nuevo item condigo 201-Create o creado 
		return new_item, 201

	# Metodo para Eliminar un articulo/item----------------------------------------------------------------------
	def delete(self, name):
		# Llamar lalista de items de forma global
		global items_list
		# Sobreescribir la lista de items, excepto el objeto a Eliminar
		items_list = list(filter(lambda it: it['name'] != name, items_list))
		# Retorno de mensaje
		return {'message':'Item deleted'}
	
	# Metodo para crear o actualizar un articulo/item----------------------------------------------------------------------
	def put(self, name):
		# Obtener el dato del request, Parseando los datos recibidos
		data_price = Item.parser.parse_args()
		# Validar si el item existe
		item = next(filter(lambda it: it['name'] == name, items_list), None)
		# Si el elemento no exite se crea uno nuevo
		if item is None:
			new_item = {'name':name, 'price':data_price['price']}
			# Agregar el item a la lista
			items_list.append(new_item)
		else: #SI el item existe actualizar datos
			item.update(data_price)
		# Retornar el articulo
		return item
#------------------------------------------------------------------------------
# RECURSOS-> CLASE LISTA DE ARTICULOS
#------------------------------------------------------------------------------
class ItemsList(Resource):
	# Metodo para retornar la lista de articulos
	def get(self):
		# Retorno de un diccionario con la lista
		return {'items':items_list}
#------------------------------------------------------------------------------
# AÑADIR RECURSOS Y END POINTS
#------------------------------------------------------------------------------
# Añadir Recurso/------->
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
#------------------------------------------------------------------------------
# EJECUCIÓN
#------------------------------------------------------------------------------
app.run(port=5000, debug=True)