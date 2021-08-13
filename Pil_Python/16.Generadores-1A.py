#---------------------------------------------------#
#GENERADORES->
#---------------------------------------------------#
#Programa para generar numeros pares

#USANDO FUNCION->
def genParesFun(limite):
	# Contador
	num = 1;
	# Array para Numeros pares
	miLista = [];
	# Bucle while
	while num < limite:
		# alamacenar el numero par
		miLista.append(num*2);
		num = num + 1;
	# Fin while

	# Retorno de datos de la Funcion
	return miLista;
# Fin Funcion

# Imprimir Ejercicio
print(genParesFun(10));

#USANDO GENERADOR->
def genParGene(limite):
	#contador
	num = 1;
	# Bucle
	while num < limite:
		#retorno del Generador
		yield num*2;
		#Sumatoria de Contador
		num = num + 1;
	# fin Bucle
# Fin funcion

# La intruccion yield construye un objeto iterable que va enviando de uno en uno
devPares = genParGene(10);
# El objeto iterable se debe recorrer con un Bucle
for i in devPares:
	print(i);
#Se puede usar next para sacar elemento por elemento del generador
devPares = genParGene(20);
print("Codigo...");
# Entre llamada y llamada el generador entra en estado de suspension hasta ser llamado
# Lo que mejora la eficiencia del programa
print(next(devPares));
print("MAs codigo...");
print(next(devPares));
print("MAs codigo...");
print(next(devPares));
