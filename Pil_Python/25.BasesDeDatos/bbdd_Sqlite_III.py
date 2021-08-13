"""
Leer Informacion de una Tabla en la Base de Datos
"""
# Llamado de la libreria sqlite3
import sqlite3
# Conectar con la base de datos
miConexion = sqlite3.connect("bbddEj_1")
# Puntero o cursor
mPunt = miConexion.cursor()
# Consulta para seleccionar datos el cual sera un array
mPunt.execute("SELECT * FROM PRODUCTOS")
# Tomar los productos y pasarlos como una lista con fetchall()
liProductos = mPunt.fetchall()
# Imprimir todos los datos en consola
print(liProductos)
# Recorrer la lista con un for para imprimir las tuplas internas de los productos
for producto in liProductos:
	print(producto)
# Recorrer la lista y la tupla dato a dato
for producto in liProductos:
	print("Articulo: ",producto[0], "Precio: ", str(producto[1]), "Sección: ", producto[2])

# Comit de la conexion
miConexion.commit()
#Cierre de conexion
miConexion.close()
