"""
#APLICACION FLASK RESTFUL SQLITE3
----------------------------------------------------------------------------
SQL-ALCHEMY -> SqlAlchemy es un orm el cual facilita las transacciones
con las bases de datos.
--------------------------------------------------------------------------
Archivo de Base de datos
"""
# Libreria SqlAlchemy ------->
from flask_sqlalchemy import SQLAlchemy

#------------------------------------------------------------------------------
# INSTANCIA DE OBJETO SQLALCHEMY
#------------------------------------------------------------------------------
"""
#COMENT-> El objeo SQLAlchemy permite crear objetos de nuestros modelos
de tablas en una base de datos y tambien nos permite insertar datos
como objetos en las mismas.
"""
db = SQLAlchemy()