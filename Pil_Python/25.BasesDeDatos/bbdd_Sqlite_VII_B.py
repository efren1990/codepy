"""
OPERACIONES TIPO CURD CON TABLAS EN BASES DE DATOS MYSQLITE
"""
#LEER o READ--------------------------------->
# Importar librería
import sqlite3
# Conexion con base de datos
miCon = sqlite3.connect('weapons_bd')
# Cursor o puntero
miCur = miCon.cursor() 
# Ejecutar consulta reed---------------------------------------------------------------------->
# Busca todos los campos segun la CLASE en la bd
miCur.execute("SELECT * FROM WEAPONS WHERE CLASE = 'Automáticas'")
# los datos seran devieltos en un array con fetchall
armas = miCur.fetchall()
# imprimir todo el array
print(armas)
# imprimir dato a dato el array
for arma in armas:
	print("Id_arma: ",arma[0]," Nombre Arma: ",arma[1], " Precio: ",arma[2], " Clase: ", arma[3])

# Ejecutar insercion de varios archivos----------------------------------------------------->
liArmas = [
	("Colt M1911", 1000, "Automáticas"),
	("Berretta 92", 1250, "Automáticas"),
	("HK usp", 2500, "Automáticas")
]
# Consulta
#--miCur.executemany("INSERT INTO WEAPONS VALUES(NULL,?,?,?)", liArmas)

#Consulta de Actualizacion update-------------------------------------------------------------->
miCur.execute("UPDATE WEAPONS SET PRECIO=2800 WHERE NOM_WEAPON='HK usp'")

#Borrar un registro----------------------------------------------------------------------------->
# Para evitar error siempre se insertara y borrara
miCur.execute("INSERT INTO WEAPONS VALUES(NULL, 'Ak 47', 4500, 'Automáticas')")
# Confirmacion de la conexion
# Borrar Registro
miCur.execute("DELETE FROM WEAPONS WHERE NOM_WEAPON = 'Ak 47'")

miCon.commit()
# Cierre de conexion
miCon.close()

