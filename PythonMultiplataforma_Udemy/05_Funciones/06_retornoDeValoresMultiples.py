"""
RETORNO DE VALORES MULTIPLES
Es el retorno de una lista o una tupla de valores

"""
# Funcion con retorno multiple
def func():
	return 1, 2
# Atribucion multiple, si necesidad de declarar lista, de forma empaquetada
# Principios de desempaquetamiento
a, b = func()
print(a)
print(b)
# Principios de Desempaquetamiento
t = (25, 35)
# Empaquetar Valores - Desempaquetar tupla [Siempre la misma cantidad de valores ]
c, d = t
print(c)
print(d)

# Funcion con Retorno Multiple
def potencia(z):
	cuadrado = z**2
	cubo = z**3
	return cuadrado, cubo
q, c = potencia(10)
print(q)
print(c)

