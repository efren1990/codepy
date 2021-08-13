"""
REBANADO LISTAS-------------------------------------------------------------
(slicing) - Rebanar listas se usa con el fin de obtener otra lista.
Para rebanar una lista se debe usar los : puntos indicando el inicio, fina, pasos(recorrido)
lista[inicio:fin:pasos]

"""
lets = ["P","Y","T","H","O","N"]
# Inicia en indice 0 , Hasta el elemento 2, Cada 1 paso
reb_a = lets[0:2:1]
print("Rebanada 1:", str(reb_a))
# Inicia en indice 2 , Hasta el elemento 4, Cada 1 paso
reb_b = lets[2:4:1]
print("Rebanada 2: "+ str(reb_b))
# Si no se especifica el inicio tomo el 1er indice por defecto
reb_c = lets[:4:1]
print("Rebanada 3: "+str(reb_c))
# Si no se especifica el final y el inicio tomara todo el array
reb_d = lets[:]
print("Rebanada 4: "+str(reb_d))
# Los pasos indican cada cuanto rebanar, no se debe inidicar los pasos en 0, genera error
reb_e = lets[0:6:2]
print("Rebanada 5: "+str(reb_e))