"""
QUE ES UNA REST API?
---------------------------------------------------------------

1-Es una manera de pensar cómo un servidor web responde
a sus solicitudes y a cómo se comporta un servidor web
en general.

2-No responde solo con datos

3-Responde con algo llamado Recursos, ahora un recurso es 
escencialmente solo datos, pero es un cambio en la forma 
de pensar, entonces es necesario dejar de pensar en hacer
peticiones y que el servidor responde con datos. Ahora
tenemos que empezar a pensar que estamos pidiendo un recurso
para al algo en el servidor.

4-Estos recursos pueden interactuar con la solicitud pertinente.

--------------------------------------------------------
TIPOS DE SOLICITUDES O PETICIONES REQUEST
NOTA: En esta caso al crear una API REST se juega el papel de servidor

# GET - se usa para enviar datos de vuelta - El servidor envia datos
# POST - se usa para recibir datos - el servidor recive datos
# PUT - se usa para insertar o poner datos
# DELETE - se usa para eliminar datos
"""
# -----------------------------------------------------------------------------
# EJERCICION DE TIENDAS ONLINE
# -----------------------------------------------------------------------------
"""
"""
# Importar del modulo flask
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder="templates")
# -----------------------------------------------------------------------------
# Diccionario como funcion de bbdd temporal para almacenar las tiendas
# LISTA de tiendas, cada tienda con sus articulos
dt_stores = [
	{
		'name':'Mi tienda Ejemplo',
		'items':[
			{
				'name':'Mi articulo ejemplo',
				'price':12.99
			}
		]
	}
]
# -----------------------------------------------------------------------------
# ENDPOINTS -> rutas con peticiones GET o POST, puntos de ruta
# -----------------------------------------------------------------------------
# @RUTA: root inicial
@app.route('/')
def home():
	return render_template('index.html')

# POST /store data:{name} - Crea una tienda con un nombre de pila
# -----------------------------------------------------------------------------
# @RUTA: Ruta para crear una tienda reciviendo dato post
@app.route('/store', methods=['POST']) # 'http://127.0.0.1:5000/store' 
# Metodo de ruta
def create_store():
	# Para obtener el dato de la peticion es necesario obtener el request del json
	# el dato es el nombre de la tienda enviado por el cliente
	request_data = request.get_json() # Toma el dato de la peticion echa por el cliente
	# Crear un diccionario con los datos enviados por el cliente de la nueva tineda
	new_store = {
		'name':request_data['name'],
		'items':[]
	}
	# agregar la tienda a la lista de tiendas
	dt_stores.append(new_store)
	# Retornar la nueva tienda creada
	return jsonify(new_store)
# -----------------------------------------------------------------------------

# GET /store/<string:name> - Obtiene una tienda para un nombre de pila - nombre
# -----------------------------------------------------------------------------
# @RUTA: Ruta para enviar datos de una tienda segun parametro
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/nombre_tienda'
def get_store(name):
	# Iterar la lista de tiendas
	for store in dt_stores:
		# si nombre de la tienda conicide con el dato en la peticion
		if store['name'] == name:
			# retornar los datos de la tienda
			return jsonify(store)
	# Si no se encuentra en el recorrido retornar mensaje
	return jsonify({'message':'la tienda no se encuentra'})		
	
# -----------------------------------------------------------------------------

# GET /store - Devuelve la lista de las tiendas
# -----------------------------------------------------------------------------
# @RUTA: Ruta para enviar datos de todas las tiendas
@app.route('/stores') # 'http://127.0.0.1:5000/stores'
def get_stores():
	# Retornar la Lista de tiendas en formato json como un diccionarios, ya
	# que json solo recibe diccionarios 
	return jsonify({'stores':dt_stores})
# -----------------------------------------------------------------------------


# POST /store/<string:name>/item {name:price}- crea un nuevo item dentro dentro de una tienda especifica 
# -----------------------------------------------------------------------------
# @RUTA: Ruta para crear un item en una tienda reciviendo dato post
@app.route('/store/<string:name>/item', methods=['POST']) # 'http://127.0.0.1:5000/store' 
# Metodo de ruta
def create_item_in_store(name):
	# Tomar los datos post enviados por el cliente
	request_data = request.get_json()
	# Recorrer la lista de tiendas
	for store in dt_stores:
		# Validar si existe la tienda en el parametro de ruta
		if store['name'] == name:
			# Crear un item nuevo con los datos post enviados por el cliente
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			# Agregar el item a la tienda
			store['items'].append(new_item)
			# Retornar el nuevo item
			return jsonify(new_item)
	# Si no esta la tienda
	return jsonify({'message':"La tienda no se encuetra"})
# -----------------------------------------------------------------------------

# GET /store/<string:name>/item - Obtiene todos los items de una tienda especifica
# -----------------------------------------------------------------------------
# @RUTA: Ruta para enviar datos de un o los items de una tienda segun parametro
@app.route('/store/<string:name>/items') # 'http://127.0.0.1:5000/store/nombre_tienda'
def get_items_in_store(name):
	# Recorrer la lista de tiendas
	for store in dt_stores:
		# Validar si el nombre de la tienda esta en la lista
		if store['name'] == name:
			# retornar la lista de items de la tienda en formato json
			return jsonify({'items':store['items']})
	# si no encuentra la tienda
	return json.jsonify({'message':'La tiene no se encuentra'})
# Ejecutar Servidor web modo debug
app.run(port=5000, debug=True)