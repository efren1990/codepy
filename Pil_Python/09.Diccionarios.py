#--------------------------------------------------------------------------------#
#LOS DICCIONARIOS-->

# Son Estructuras de Datos que nos permiten almacenar valores de diferente tipo
# (Enteros, Strings, decimales) e incluso listas y otros DICCIONARIOS

# La Principal Caracteristica de los Diccionarios es que los Datos se Alamacenan
# asociados a una Clave de tal forma que se crea una asociacion de tipo Clave:valor
# Para cada elemento almacenado

# Los elementos almacenados no estan ordenados. El orden es indiferente
# a la hora de alamacenar informacion en un diccionario

# En Php->Los Diccionarios serian Arrays Asociativos los cuales son estructuras
# Similares

#SINTAXIS-->
#nombreDiccionario = {"clave":"Valor"}
miDiccionario = {"Alemania":"Berlin", "Colombia":"Bogota", "Francia":"Paris", "España":"Madrid"};
#Imprimir Elemento del Diccionario(Se llama la Clave)
print(miDiccionario["Francia"]);
#Agregar un Elemento al Diccionario
miDiccionario["Italia"]="Alguna";
#Imprimir Todo el Diccionario
print(miDiccionario);
#Cambiar Valor de un Elemento en el Diccionario
miDiccionario["Italia"]="Roma";
print(miDiccionario);
#ELIMINAR-->
#Palabra clave del nomDiccionario["Clave de elemento a borrar"]
del miDiccionario["Colombia"];
print(miDiccionario);
###
midic = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3};
print(midic);
#Diccionarios Con Tuplas
miTuplin = ("España", "Francia", "Reino Unido", "Alemania");
miDiccio ={miTuplin[0]:"Madrid", miTuplin[1]:"Paris", miTuplin[2]:"Londres", miTuplin[3]:"Berlin"};
print(miDiccio);
#Formas de imprimir diccionarios con tuplas
print(miDiccio[ miTuplin[0] ]);
print(miDiccio["España"]);
#Diccionarios Con Claves contenedoras de Varios Valores
miDicVal = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":(1991, 1992, 1993, 1996, 1997, 1998)};
print(miDicVal["Equipo"]);
print(miDicVal["anillos"]);
###
# Diccionario Dentro de Otro DIcionario-->
miDic = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":(1991, 1992, 1993, 1996, 1997, 1998)}};
print(miDic["Anillos"]);
print(miDic);
###
# Metodos Utiles Con Diccionarios---->
# keys()->Saber las claves(Llaves) del diccionario
print(miDic.keys());
# values()->Saber los Valores del Diccionario
print(miDic.values());
# len(diccionario)->Saber la longitud del diccionario
print(len(miDic));


