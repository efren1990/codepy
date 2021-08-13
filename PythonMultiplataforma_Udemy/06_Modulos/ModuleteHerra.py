#coding: utf-8
"""
Modulo Herramientas
al agregar el under score a una variable python reconoce
que esta es de uso local y por dicha razon no debe ser importada
cuando el usuario final de la aplicacion mande a importar a todos los
símbolos de un modulo.


"""
# SÍMBOLOS PRIVADOS
_a = 10
_b = 20
_c = 30
# Nota: esta es una practica no muy conveniente, debido a que crea conflictos de depuracion

# SÍMBOLOS PUBLICOS
# Al ser importados todos los simbolos en otro archivo
# para indicarle a python la lista de símbolos que seran importados se debe usar __all__ = ["simolo", "simolo"]
__all__ = ["aa", "ab"]	# __all__ -> define la lista de simbolos que seran importados al ser llamado el modulo
aa = 0
ab = 1
ba = 2
bb = 3
suma = _a + _b +_c