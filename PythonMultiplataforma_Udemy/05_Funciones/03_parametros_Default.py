"""
PARÁMETROS DEFAULT

Tambien llamados paramtros predefinidos
son los que recibe un valor en la implementacion de lafuncion
es decir que el valor es tribuido al paramtro dentro del parentesis.
	1-Deben ser definidos de últimos
"""
# Funcion con paramtros default
def login(usuario="root", contra="123"):
	print("Usuario: "+usuario)
	print("Contraseña: "+contra)
# LLamado de la funcion
login()
# Los paramtros default son obviados cuando a la funcion se le asignan 
# argumentos a los parametros
login("Dean_66", "64885_bg")
# Siempre se deben pasar ambos paramtros, porque entoces alterara el primero siempre
login("66_sdda")
login("root", "66_sdda")