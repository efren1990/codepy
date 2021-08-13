"""
UTILIZACION DE PEEWEE 1
CREANDO TABLA ESTUDIANTES
-----------------------------------------------------------------------
Conectar a una base de datos
crear tabla 
crear objetos de tabla
"""
# Importar libreria peewee - por convencion debe importarse la libreria completa
from peewee import *

# Crear o Conectar a una base de datos sqlite
# SqliteDatabase('nombreBaseDatos.extension')
db = SqliteDatabase('students')

# Definir modelos de la base de datos, creando una clase
# la cual recibira como parametro Model, clase por defecto en peewee
class Student(Model):
	# Esta clase sera la tabla en la base de datos, 
	# donde se definiran campos y tipos de datos de cada campo
	# Definir campos - nombre y puntos
	username = CharField(max_length=255, unique=True)
	points = IntegerField(default=0)
	# Cada vez que se define un Modelo debe llevar una clase Meta de forma interna
	class Meta:
		# De esta forma se define dentro de base de datos estara el modelo
		database = db
# -------------------------------------------------------------------------------------
# Definir registros en formato json para insertar listado 
listStudents = [
	{'username':'Panchita',
	 'points': 0
	},
	{'username':'Juan',
	 'points': 4
	},
	{'username':'Aldo',
	 'points': 5
	},
	{'username':'Carolina',
	 'points': 10
	}
]
# Funcion para agregar registros a la base de datos
def add_students():
	# Recorrer lista e insertar cada registro
	for student in listStudents:
		# Para evitar insertar nuevamente los campos ya insertados, se trata la excepcion
		try:
			# Insertar registro
			# ObjetoTabla.create(campo=valor)
			Student.create(username=student['username'],points=student['points'])
		except IntegrityError:
			# Traer los datos del estudiante que ya ha sido insertado
			# Tabla.get(condicion o restriccion);
			student_record = Student.get(username=student['username'])
			# Impirmir el registro
			print("Nombre: ", student_record.username)
			print("Puntos: ", student_record.points)
			# Agregar un nuevo valor a los puntos de cada estudiante
			student_record.points = student['points']
			# Hacer un set table de los campos
			student_record.save()
# -------------------------------------------------------------------------------------
# Funcion para traer el estudiante con la nota mas alta
def top_student():
	# Seleccionar el dato y ordenarlo por orden descendiente
	# Extraer solo los datos del primer registro encontrado
	student = Student.select().order_by(Student.points.desc()).get()
	# Retornar el dato extraido
	return student
# -------------------------------------------------------------------------------------

# 
if __name__ == '__main__':
	# Conectar con la base de datos
	db.connect()
	# Crear la tabla
	# db.create_tables([Array con modelos(tablas a crear)])->
	# safe = True, evita un error si la base de datos y 
	# las tabla ya existe, no dejara que se cree nuevamente
	db.create_tables([Student], safe=True)
	# Insertar datos en tabla con la funcion creada
	add_students();
	# Imprimir Estudiante con puntos mas altos
	print("El estudiante con mejor putuacion es: {}".format(top_student().username) ) 














