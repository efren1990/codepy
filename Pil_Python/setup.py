#Archivo que describe el paquete Distribuible

#1->from setuptools import setup
from setuptools import setup
#Funcion setup(argumentos de configuracion)->

setup(
	#Nombre del Paquete
	name="paqueteCalculos",
	#version
	version="1.0",
	#Descripcion
	description="Paquete de Redonde y Potencia",
	# autor del paquete
	autor="scrop",
	#Email del autor, opcional
	author_email="correo@gesto.com",
	#Url de referencia
	url="www.paginaReferencia.com",
	#IMPORTANTE packages->aca ira donde se encuentra el paquete o sub paquete que queremos empaquetar
	#la ruta que se debe seguir debe ser desde la raiz ya que el archivo setup esta en la raiz
	packages=["Paquetes","Paquetes.redondeo_Potencia"]	
	)