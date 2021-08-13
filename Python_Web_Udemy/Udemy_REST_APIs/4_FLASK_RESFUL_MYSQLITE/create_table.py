"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------
Archivo para crear base de datos y tablas
"""
# Libreria Sqlite3 ------->
import sqlite3
# Conexion ------->
connection = sqlite3.connect('data.db')
# Cursor ------->
cursor = connection.cursor()
# Query table ------->
# INTEGER- ENTERO AUTOINCREMENTAL EN SQLITE3
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# Ejecutar query table users------->
cursor.execute(create_table)
# Ejecutar query table items------->
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)
cursor.execute("INSERT INTO items VALUES(NULL, 'test', 9.99)")
# Commit ------->
connection.commit()
# Cierre ------->
connection.close()
