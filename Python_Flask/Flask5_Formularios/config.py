"""
ARCHIVO DE CONFIGURACION
-----------------------------------------------------------------------------------
Se usa para configurar las variables de cada entorno y los mismos entornos en si
Ej:
Entorno de Desarrollo
Entorno de Produccion
"""
# Importar os para crear en variables de entorno
import os

# Clase para configuracion general
class Config(object):
	# Variable para clave secreta
	SECRET_KEY = 'mySecretKey_3443[dsds]_dwedqw'
# Calse para configuracion de entorno de Desarrollo Hereda de clase Config
class DevelopmentConfig(Config):
	# Debug
	DEBUG = True
	# AGREGAR LAS CONFIGURACIONES DEl ORM ALCHEMY
	# -----------------------------------------------------------------------
	# Sentencia para conectar a la base de datos
	# SQLALCHEMY_DATABASE_URI = 'mysql://usuario:password@localhos/nombreBaseDeDatos' 
	SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_1?charset=utf8&use_unicode=True'
	# SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_1'
	# Evitar el mensaje warning
	SQLALCHEMY_TRACK_MODIFICATIONS = False
