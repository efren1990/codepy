"""
#FUNCIONES DE LOS DICCIONARIOS 
---------------------------------------------------------------------

"""
# Diccionario telefonos
tel = {
				6468906:"Juan Estrada",
				6463659:"Cosme Fulanito",
				6464569:"Pablito Escobar",
				6467489:"Juanito Alimaña",
				646668:"Los de la Moto"
			}
print(tel)			
# Contar elementos Diccionario
print("Cantidad Telefonos Libreta: ", len(tel))
# Remover elemento del diccionari
del(tel[6468906])
print(tel)
print("Nueva Cantidad Telefonos Libreta: ", len(tel))
# Ver las llaves del diccionario
print("Llaves Dicionario tel: ",tel.keys())
# Ver todos lo valores diccionario
print("Valores Diccionario: ",tel.values())
# Otra forma de mostrar el valor segun la llave del diccionario
print(tel.get(6464569))
# Retornar un elemento y removerlo del diccionario (ultimo elemento)
it = tel.popitem()
print(it)
print(tel)
# validar si una llave esta en el diccionario
print(6464569 in tel)
# MEZCLAR DICCIOANRIOS----------------------------------------------
tel_b = {
					6585252:"Alphonse Capone",
					6365589:"Carlos Leder",
					6899696:"Rodriguez Gacha",
					6666666:"El coco"
				}
# Agregar el segundo diccionario al primero
# dic1.update(dic2)
tel.update(tel_b);
print(tel)
# Añadir una tupla como llave a un diccionario
tup = (10, 10, 10)
# Agregar la tupla
tel[tup] = "Poscion"
print(tel) 
