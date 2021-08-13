"""
INSTRUCCION GLOBAL
------------------------------------------------------------------------------
ÁMBITO -> un ámbito es la visibilidad que cada miembro posee
								dentro de un determinado código.
ÁMBITO GLOBAL -> es el ámbito de los módulos (dentro de un archivo python)

"""
# al ser declarada dentro del módulo sera alamacenada como global y local
num = 10
glo = 5
def func():
	# Al ser declara dentro del ámbito de la función sera local
	x = 10
	# num declara en el ámbito local solo se altera dentro de la funcion
	# asi la variable sea declara con el mismo nombre en el ámbito global
	# ya que se creara en el ámbito local de la función
	num = 20
	print(x)
	print(num)
	# Alterar un variable global dentro de un ámbito local
	global glo
	glo = 55
	# Crear una variable global dentro de un ámbito local
	global gloLoc
	gloLoc = 25
# La funcion globals() retorna todas la variables globales
# print("Globals: ", globals())
print(glo)
func()
print(num)
print(glo)
print(gloLoc)
# La función locals retorna todas las variables locales
# print("Locals: ", locals())