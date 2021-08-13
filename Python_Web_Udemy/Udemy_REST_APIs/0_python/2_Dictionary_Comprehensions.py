"""
COMPRENSIÓN DE DICCIONARIOS
-----------------------------------------------------------------------------
Es una caracteristica de python y nos permite crear nuevos diccionarios
sobre la marcha a partir de listas existentes, realizando iteraciones y
consultas dentro de las listas - Comprensión de listas.
"""
# Lista de usuarios con tuplas internas
users = [
	(1, "ryn", "daspasswo452"),
	(2, "dion", "1252ssdw"),
	(3, "laica", "er_As52"),
	(4, "handis", "dasñ_23"),
	(5, "rett", "fs_rtñ65_r")
]
"""
Crear un diccionario clave:valor, asociando la clave con el nombre de usuario
recorriendo la lista sacando cada nombre de cada tupla interna.
Asociando el el valor a la tupla completa de la lista
Comprension de listas
para crear Comprension de diccionadios
nom_diccionario = {list_clave_[]: recorrido for if etc}
"""

# username_mapping = {ClaveListaUsuarios_Variable: Valor_Variable for VariableRecorrido(Clave_Valor) in ListaUsuarios}
username_mapping = {user[1]: user for user in users}
print(username_mapping["dion"])
# EJERCION COMPRENSIÓN DE DICCIONARIOS
username_input = input("Ingresa tu usuario: ")
password_input = input("Ingresa tu contraseña: ")
# Desempaquetar el diccionario  que se creo con la Comprensión de diccionarios
_id, user_name, password = username_mapping[username_input]
# Validar la contraseña de usuario desempaquetada de la compresion del diccionario
if password == password_input:
	print("Correcto")
else:
	print("Incorrecto")
