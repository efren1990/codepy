"""Pasos A Seguir para conectar en una Base de Datos con Python+++++++++++++++++++++++++++++++++++"""
"""
1-Abrir Crear-Conexion
2-Crear Puntero o Cursor
3-Ejecutar Query (Consulta) SQL
4-Manejar los Resutados de la Query	
	1. Insertar, Leer, Actualizar, Borrar (Create, Read, Update, Delete) (CRUD)
5-Cerrar Puntero
6-Cerrar Conexion
"""
# Para usar la bbdd Sqlite es necesario importar su libreria
import sqlite3
# Crear una Base de Datos ya que no existe, en vez de conectarse la crea
miConexion = sqlite3.connect("bbddEj_1");

# Crear el Cursor o puntero que se encargara de Realizar las acciones del CRUD
miCursor = miConexion.cursor();

# Crear y ejecutar la consulta para crear la tabla
#miCursor.execute("CREATE TABLE PRODUCTOS (NOM_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(50))")
#Una vez sea creada la tabla es necesario anular la linea de codigo para que no se emita error de tabla ya creada

# Insertar Datos en una tabla
miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balón', 15, 'Deportes')")
# Cada vez que se hace un cambio en una tabla ya se de estructura o contenido, hay que verificar ese cambio
miConexion.commit()#Confirmar el cambio

# Cerrar una Conexion
miConexion.close();