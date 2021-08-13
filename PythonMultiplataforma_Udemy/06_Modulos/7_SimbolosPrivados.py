"""
SÍMBOLOS PRIVADOS
--------------------------------------------------------------------------------
Son los nombres contenidos en el ámbito local.

Cuando los módulos son importados se transforman en objetos y las variables y funciones
declaradas en su cuerpo pasan a ser los miembros dicho objeto.

La principal diferencia entre un objeto y un módulo es que un objeto es creado a partir
de una clase y tendra siempre sin excepciones una unica instancia por aplicación por esta
caracteristica varios seran los nombres declarados en el ambito global de los módulos y estos
muchas veces no tendran ningun tipo de utilidad para los usiarios finales de los modulos.
"""
# Importar todos los símbolos del modulo herramientas
# los simbolos precededidos por un underscore _a, _b, _c no seran importados
from ModuleteHerra import *
# Importar pprint
from pprint import pprint
pprint(globals())