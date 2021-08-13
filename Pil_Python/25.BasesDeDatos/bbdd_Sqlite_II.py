"""
	Inserción de varios registros
	Recuperación de varios registros
"""
#Llamado de la libreria SQLite
import sqlite3
#Conectar a la Base de datos
miConexion = sqlite3.connect("bbddEj_1")
#Crear el cursor o puntero
miCursor = miConexion.cursor()

#Array o lista con tuplas internas para cada articulo a insertar
liProductos = [
	("Camiseta", 25, "Deportes"),
	("Jarrón", 90, "Cerámica"),
	("Camión", 15, "Juguetería")
]
# Insertar varios productos de una lista
#executemany("Clausula SQL", ListaArray)
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?, ?, ?)", liProductos)
# el numero de interrogantes corresponde al numero de campos a insertar

#Confirmación de la consulta
miConexion.commit()

# Cerrar Conexión
miConexion.close()

