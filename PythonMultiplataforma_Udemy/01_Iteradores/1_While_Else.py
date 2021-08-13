"""
BUCLES CONDICIONALES----------------------------------
INSTRUCCION ELSE CON BUCLE WHILE
El bloque de instruccion solo se ejecutara
mietrnas la condicion sea verdadera
a no de ser que sea falsa y cambiara el flujo
de ejecucion del programa
"""
x = 0
print("Inicia bucle while----------------------------")
#Bucle while else
while(x <= 10):
	#Codigo a ejecutar dentro del bucle
	print("Dentro de while------------------------------")
	print('Flujo: ' + str(x))
	x += 1
else:
	print("Si x es mayor o igual a diez")
print("--------------------------------------------")
print("Fuera del Bucle while else")
print("--------------------------------------------")

