"""
CLASE LISTA---------------------------------------------------------------
"""
# Ya que python trata una lista como un objeto, y todos sus elementos internos tambien
# Python ofrece metodos para realizar operaciones con listas

# LENGTH--------------------------------------------------------------------------
# Funcion que retorna cuantos elementos estan contenidios dentro de la lista
perros = ["San Bernardo", "Alaska Malamute", "Chihuahua", "Golden Retriver"]
print("Elementos en lista perros: ", len(perros))
# Conteo de listas de multiples dimensiones
gatos = [
	["calasio", "rendin", "rost"],
	["Uren", "rayn", "pardo"]
]
print("Elementos en lista gatos: ", len(gatos))
print("Elementos Indice 0 lista gatos: ", len(gatos[0]))
print("Ultimo elemento de lista indice -1:", perros[-1])