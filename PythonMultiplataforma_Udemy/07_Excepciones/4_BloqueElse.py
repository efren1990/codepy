"""
BLOQUE ELSE EN EL TRATAMIENTO DE EXCEPCIONES
--------------------------------------------------------------------------------
Es una sub estructura de try que solo tendra su bloque de codigo ejecutado
cuando ninguna excepcion sea levantada.

Las aplicaciones deben ser construidas de tal forma que se evite el levantamiento
de una excepcion, ya que las excepciones como su mismo nombre lo sugieren deben ocurrir
la minima cantidad de veces posible y por lo tanto todo aquello que podamos hacer para
evitarlas debe ser hecho.

Debemos tener como idea fija, que ningun error ocurre naturalmente, durante la ejecicion
de nuestra aplicacion ninguna excepcion debe ser levantada, por tanto no debemos asumir
situaciones en la que la gran mayoria de las veces ocurriran excepciones.
try:
	#codigo
except:
	#Tratamiento
else:
	#Solo si ninguna excepcion fue levantada durante la ejecucion del bloque 
	de codigo dentro de la indtruccion try:
"""
def error(x):
	try:
		eval(x)
	except (ValueError, ZeroDivisionError) as e:
		# Typo de Error
		print(type(e))#Instancia de la Excepcion
	else:
		print("Ninguna Excepcion ocurrio")

error("5/2")
error("int('1')")


