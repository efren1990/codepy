"""
#PROPIEDADES STRINGS 
---------------------------------------------------------------------
"""
# String
s = "Lista de caracteres";
# Saber caracteres string - el cual es una lista
print("STRING: ", s)
print("Cantidad de caracteres en el string: ", len(s))
# Debido a que los string son inmutables no se pueden aletar
# pero si se pueden dividir y reorganizar para generar uno nuevo
# Split para divir un string
nS = s.split(" "); #Divir por espacion en blanco
print(nS) #->string.split("Parametro de division") - devuelve lista - que es un string
# Generar nuevos strings
nSt = nS[0]+" "+nS[2]
print("NUEVO STRING: ", nSt)
# Generar nuevos string con replace
nSt_2 = s.replace("de", "");
print("NUEVO STRINSG FORMA 2: ", nSt_2)
# Los string tienene un id-------------------------------------
print("ID del String: ", id(s))
print("ID del String: ", id(nSt_2))
print("ID del String: ", id(s.replace("de", "")) )
x = id(s)
print(type(x))

