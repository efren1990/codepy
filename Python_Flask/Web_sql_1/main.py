"""
MAIN--------------------------------------------------------------------------------------------------------
python - flask - mysql
"""
# importar modulo flask Clase flask y render template
# Importar modulo request el cual se encarga de las peticiones y envio de datos por la url
# url_for -> Metodo para poder pasar una url y poder redireccionar con redirect
# redirect -> Permite redireccionar
# flash -> permite enviar mensaje entre urls
from flask import Flask, render_template, request, url_for, redirect, flash
# Importar modulo para conectar con mysql
from flask_mysqldb import MySQL
# Instancia de la clase Flask
app = Flask(__name__, template_folder='templates')
#configuracion de conexion mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_flask'
# Instancia de la clas mysql pasando como parametro al app
mysql = MySQL(app)
# Configuracion clave secreta para una session y poder enviar mensajes con flash
# Guardando dentro de la memoria de al aplicacion
app.secret_key = 'mysecretkey'
#RUTAS------------------------------------------------------------------------------------------------------
#Index-->
@app.route('/')
# Funcion de ruta
def index():
	# Conexion para consulta
	miCur = mysql.connection.cursor()
	# Consulta sql
	miCur.execute("SELECT * FROM tb_contactos")
	# Ejecutar consulta y extraer todos los datos con fetchall()-<retorna array de datos
	datosConsulta = miCur.fetchall()
	print(datosConsulta)
	# Retorno de la platilla
	return render_template('index.html', liDatos = datosConsulta)
#Contactos------------------------------------------------------------------------------------------------------>
# Si la ruta recibe datos url get o post es necesario asignar el metodo de ruta methods = 'metodo'
@app.route('/contactos', methods=['POST'])
# Funcion de ruta
def contactos():
	# Ya que al enviar los datos del formulario se usara esta ruta
	# Se debe validar si se esta enviando datos a la ruta a travez del metodo post
	if request.method == 'POST':
		# Se usa el objeto request con el metodo form para colectar datos con el atributo name del formulario html
		# request.name['datoPropiedad name html imput'] -> capta el dato del formulario
		nom = request.form['nombre']
		tel = request.form['telefono']
		ema = request.form['email']
		# Impirmir en consola datos enviados
		print(nom)
		print(tel)
		print(ema)
		# Paso de datos a la BD--------------------------------->
		# crear cursor de la conexion
		miCur = mysql.connection.cursor()
		# Consulta sql ("Consulta", (tuplaValores))
		miCur.execute("INSERT INTO tb_contactos(nom_cont, tel_cont, ema_cont) VALUES(%s, %s, %s)", (nom, tel, ema))
		# Confirmacion de la consulta
		mysql.connection.commit()
		# Se pueden mandar mensajes entre vistas con el metodo flash
		flash('El contacto ha sido agregado')
		# Redireccionar al index con url_for y redirect
		# redirect(url_for('nombre funcion ruta'))
		return redirect(url_for('index'))
#Editar Contactos------------------------------------------------------------------------------------------------------->
@app.route('/editar/<string:idEdit>')
# Funcion de ruta
def editar_con(idEdit):
	# Consultar los datos segun el id recibido
	miCur = mysql.connection.cursor()
	# Consulta de datos
	miCur.execute("SELECT * FROM tb_contactos WHERE id_cont = {0}".format(idEdit))
	# confirmar cambios
	dato = miCur.fetchall()
	# La consulta debuelve un array con tuplas dentro, por cada fila de datos
	# por ende es necesario enviar solo el array con la posicion de la tupla 0 ya que es un solo grupo de datos
	print(dato)
	# Retornar la plantilla de edicion enviando el array con la tupla de los datos pedidos
	return render_template('edicion.html', contacto = dato[0])
# Eliminar contactos----------------------------------------------------------------------------------------------------->
# Ruta para eliminar la cual recibe un parametro /nomruta/<tipoDato:parametro>
@app.route('/eliminar/<string:idElim>')
# Funcion de ruta
def eliminar_con(idElim):
	# consulta para eliminar datos
	miCur = mysql.connection.cursor()
	# Consulta
	miCur.execute("DELETE FROM tb_contactos WHERE id_cont = {0}".format(idElim))
	# commit de la consulta
	mysql.connection.commit()
	# Envio de mensaje con flash
	flash('El contacto se elimino Satisfactoriamente')
	# Retorno de ruta, a la ruta index
	return redirect(url_for('index'))
# Atualizar Datos---------------------------------------------------------------------------------------------------------->
# Ruta
@app.route('/actualizar/<idActual>', methods=['POST'])
# Funcion de ruta
def actualizar_con(idActual):
	# Validar si se nevio una peticion atra vez del metodo post por la url 
	if request.method == 'POST':
		# Extraer los datos enviados por post
		nom = request.form["n_nom"]
		tel = request.form["n_tel"]
		ema = request.form["n_ema"]
		# Llamado de la conexion y el cursor
		miCur = mysql.connection.cursor()
		# Consulta sql
		miCur.execute("""
			UPDATE tb_contactos
			SET nom_cont = %s, tel_cont = %s, ema_cont = %s
			WHERE id_cont = %s
			""", (nom, tel, ema, idActual))
		# Confiramcion de la consulta
		mysql.connection.commit()
		# mensaje flash
		flash('Los datos han sido actualizados')
		# retorno al index
		return redirect(url_for('index'))

# Validar el archivo de ejecucion del servidor
if __name__ == '__main__':
	#Ejecutar la aplicacion
	app.run(port = 3500, debug = True)