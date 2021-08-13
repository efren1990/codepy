"""
------------------------------------------------------
Campos Clave Con Autoincremento en Tablas de las bases de datos
-----------------------------------------------------
"""
# Importar libreria sqlite3
import sqlite3
# Crear conexion y base de datos
miCon = sqlite3.connect("bbddEj_2")
# Crear cursor
miCur = miCon.cursor()
# Crear Tabla con campo unico O PRIMARY KEY Y autoincremento
# triple comilla para poder saltos de linea en la consulta
miCur.execute("""
	CREATE TABLE IF NOT EXISTS ARMAS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOM_ARMA VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))		
""")		
# Lista de Productos para insertar
liProductos = [
	("Glock 9.0", 2500, "Automáticas"),
	("S.M.W 38 Especial", 3500, "Revolver"),
	("Mp5", 4500, "Sub Ametralladoras"),
	("Deser Eagle Especial", 8000, "Automáticas")
]																								
# Ejecucion de la insercion de datos en la lista 
# NULL - > <permite la gestion del campo clave autoincremental por parte de la bd
miCur.executemany("INSERT INTO ARMAS VALUES (NULL,?,?,?)", liProductos)
# Confirmacion de las consulta			
miCon.commit()
# Cierre de conexión
miCur.close()