"""
#EJERCICIO CON OPERADOR IN
----------------------------------------------------
"""
a = 10
b = 25
c = 66
#tomar numero y pasarlo a int
x = int(input("Digite un número: "))
# Si esta contenido
if(x == a or x == b or x == c):
	print("Esta contenido")
else:
	print("No esta contenido")

# Resolucion del problema usando IN
y = int(input("Digite el número: "))
# Validar si el numero ingresado esta
if(y in [a, b, c]):
	print("Esta contenido.");
else:
	print("No esta contenido.")
# ---------------------------------------------------------------------------
# Ejercicio Colores-----------------------
colores = ["azul", "verde", "rojo", "amarillo", "purpura", "cafe"]
# Bucle infinito while
while True:
	eleccion = input("Digite el nombre de un color ó 0 para salir: ")
	# Validar si desea salir
	if(eleccion == "0"):
		# Romper el bucle y salir
		break;
	elif (eleccion in colores):
	# Validar si se encuentra el color
		print("el color se encuentra")
	else:
		print("el color no se encuentra")