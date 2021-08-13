#xxxxxx------------------------------------------------------------->
#SERIALIZCION
#xxxxxx------------------------------------------------------------->
"""
¿QUE ES?
Consiste en guardar en un archivo externo una coleccion, un diccionario,
e incluso un objeto, el cual se gurdara en codificado en codigo binario.

PARA QUE?
distribuir paquetes en internet, guardar en un dispositivo externo, 
alacenar en una bbdd, en binario.

Para poder llevar a cabo el proceso de serializacion debemos utilizar
la biblioteca pickle y el uso de los metodos

dump()->volcado de datos al fichero binario externo
load()->carga de los datos del fichero binario externo

Ej-> Crear una lista(array) y guardarla en un archivo externo y despues
rescatarla
"""
#1-Importar biblioteca pickle
import pickle
#Lista con nombres a guardar
lista_Nombres = ["Pedro", "Carolina", "Ana", "Andrea", "Camila", "Alejandra"];
#Creamos fichero externo de modo escritura binaria "wb"
fichero_Binario = open("lista_Nombres", "wb");
#Volcamos la lista al fichero externo pickle.dump(infoQueremosVolcar, NombreFicheroAlQueQueremosVolcar)
pickle.dump(lista_Nombres, fichero_Binario);
# Cerramos fichero
fichero_Binario.close();
#xxxxxx------------------------------------------------------------->
#SERIALIZCION
#xxxxxx------------------------------------------------------------->
"""
Rescatar la informacion del fichero guardao (srializacion-1.py)
"""
# Importar Biblioteca
import pickle
#Creamos un archivo open(nombreArcho, permiso lectura Binario "rb")
ficheroLeer = open("lista_Nombres", "rb");
#Leer la informacion binario pickl.load(elFichero)
lista = pickle.load(ficheroLeer);
# Imprimir lista
print(lista)

