"""
MÓDULOS
----------------------------------------------------------------------------------
Principal estructura para la organzación de nuestros códigos, son las unidades
de organizacion de programas de mas alto nivel.

Es la estructura en la cual agrupamos códigos que desempeñan funciones semejantes
originando estrucuras especializadas que disponibilizan un conjunto de herramientas
como variables, funciones y clases para la solucion de problemas especificos al compartir
sus estructuras y permitir la facil reutilizacion de codigos.

Basicamente el modulo es un archivo de texto que posee al código python y se guarda
en el disco con extension .py

Es la estructura gerarquica principal de una aplicacion python

Los códigos implementados dentro de los módulos reciben s du name space mediante
la union del nombre del modulo y el nombre de la estructura

Cuando se guarda en carpetas diferentes el path pasa a ser parte del name space del
modulo, Distinguiendo y evitando la colision de nombres

En el momento que se importa un modulo este pasa a ser un objeto

Un conjunto de modulos dan origen a un paquete

CARACTERÍSTICAS DE LOS MODULOS
►Reutilizar a un mismo código
►Formar Namespace
►Compartir una estructura de datos

MODULOS INCLUIDOS EN PYTHON
Biblioteca estándar es el conjunto de módulos en la distribución oficial.

	Builtins -> Es el nombre del módulo que disponibiliza a los principales
							tipos, funciones y variables del lenguaje.
							Es el modulo principal de python 

"""
