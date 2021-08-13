"""
------------------------------------------------------
Campos Unicos no repetibles en Tablas de las bases de datos
-----------------------------------------------------
"""
# Importar libreria
import sqlite3
# Base de datos y conexion
miCon = sqlite3.connect("weapons_bd")
# Cursor
miCur = miCon.cursor()
# Crear Tabla con clave,autoincrement y campo único - UNIQUE
miCur.execute("""
	CREATE TABLE IF NOT EXISTS WEAPONS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOM_WEAPON VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	CLASE VARCHAR(50)
	)
""")
# Lista de productos a insertar
liProductos = [
	("Colt 45", 1450, "Automáticas"),
	("Glock 9mm", 780, "Automáticas"),
	("Famas rx", 4500, "Ametralladoras"),
	("S.W 38 espec", 2200, "Revolvers")
]
# Ejecutar la consulta
miCur.executemany("INSERT INTO WEAPONS VALUES(NULL,?,?,?)", liProductos)
# Confirmar cambios
miCon.commit()
# Cerrar conexión
miCon.close()