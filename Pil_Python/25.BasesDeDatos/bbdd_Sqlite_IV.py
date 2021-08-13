"""
------------------------------------------------------
Campos Clave en Tablas de las bases de datos
-----------------------------------------------------
"""
# Importar libreria sqlite3
import sqlite3
# Crear conexion y base de datos
miCon = sqlite3.connect("bbddEj_2")
# Crear cursor
miCur = miCon.cursor()
# Crear Tabla con campo unico O PRIMARY KEY
# triple comilla para poder saltos de linea en la consulta
miCur.execute("""
	CREATE TABLE IF NOT EXISTS PRODUCTOS (
	COD_ARTICULO VARCHAR(4) PRIMARY KEY,
	NOM_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))		
""")		
# Lista de Productos para insertar
liProductos = [
	("AR_01", "Pelota", 25, "Deportes"),
	("AR_02", "Pantalón", 25, "Conefección"),
	("AR_03", "Destornillador", 15, "Ferreteria"),
	("AR_04", "Jarrón", 45, "Cerámica")
]																								
# Ejecucion de la insercion de datos en la lista
miCur.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", liProductos)
# Confirmacion de las consulta			
miCon.commit()
# Cierre de conexión
miCur.close()
