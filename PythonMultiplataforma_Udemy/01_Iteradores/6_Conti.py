"""
INSTRUCCION CONTINUE
Es la instruccion que interrumpe la ejecucion de un unico bucle
Solamenta salta al siguiente ciclo, ya que no finaliza la ejecucion del bucle
EJ:
Supongamos una condicion en la que estamos realizando una serie de calculos, luego
verificamos una condicion y vemos que no es necesario seguir ejecutando a los
otros calculos entonces podemos finalizar es vuelta de ciclo sin terminar
todos los calculos pero sin interrumpir el bucle
"""

i=0
print("Inicio")
while(i < 10):
	i+= 1
	# Valida si los numero dentro de i son modulo de 2
	if(i % 2 == 0):
		# Si lo son no imprime el numero
		continue
	print("Valor: ", i)
else:
	print("else while")
print("Fin")
