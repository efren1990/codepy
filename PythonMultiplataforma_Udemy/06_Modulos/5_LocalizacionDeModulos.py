"""
LOCALIZACIÓN DE MODULOS
---------------------------------------------------------------------------
Cuando un nuevo modulo es requerido a traves de la instrucción import python
lo buscara en una lista de directorios por el nombre definido despues de la 
instrucción import

Al instalar un paquete con pip, el mismo es almacenado en el directorio de
python: '\\python-dir\\lib\\site-packages'

Al utilizar a la instruccion import python recorre una lista de dircetorios
en busca del módulo

Los directorios donde seran buscados los módulos en python pueden ser
manipulados, ya sea por que se esta trabajando con frameworks o en la nube

El símbolo path dentro del módulo sys contiene la lista de paths
en los que python buscara los modulos

DIVERSAS CONFIGURACIONES QUE SE PUEDEN DEFINIR EN PYTHON
--------------------------------------------------------------------------
►Directorio base - es el directorio donde el script principal
fue ejecutado

►Directorio de la variable PYTHONPATH

►Directorio de la biblioteca estándar

►Directorios definidos por los archivos *.pth

"""
# Importar funcion pprint() del modulo pprint
# pprint() - realiza un impresion formateada en la salida estandar
from pprint import pprint
# Importar el módulo sys que contiene el símbolo path para ver lista de paths
import sys

# Imprimir la lista de paths
pprint(sys.path)
# LISTA DE RUTAS O PATHS IMPRESAS POR pprint(lpath)
# ['E:\\PROGRAMACION\\LenguajesAprendizaje\\Python\\PythonMultiplataforma\\06_Modulos',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32\\lib',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages']
# Agregar Un path a la lista de paths
# path.insert(posicion, "ruta")
sys.path.insert(0, "E:\\PROGRAMACION\\LenguajesAprendizaje\\Python\\PythonMultiplataforma\\06_Modulos\\4_CrearModulos")
# Imprimir la lista de paths
pprint(sys.path)
# ['E:\\PROGRAMACION\\LenguajesAprendizaje\\Python\\PythonMultiplataforma\\06_Modulos\\4_CrearModulos',
#  'E:\\PROGRAMACION\\LenguajesAprendizaje\\Python\\PythonMultiplataforma\\06_Modulos',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32\\lib',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32',
#  'C:\\Users\\X\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages']
# Importar modulo creado anteriormente
import modulete

