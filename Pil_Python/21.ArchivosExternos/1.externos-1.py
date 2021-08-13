#xxxxxx------------------------------------------------------------->
#ARCHIVOS EXTERNOS(MANEJO DE ARCHIVOS)
#xxxxxx------------------------------------------------------------->
#1-Importar Modulo io de la biblioteca de python
from io import open

#2-Abrir el archivo con el metodo opne(nombreArchivo, ModoAbrirArchivo)
#►Modos de Abrir Archivo->lectura(r),escritura(w),append(agregar a un archivo ya existente con info)
archivoTexto = open("archivo.txt","w");

#3-Escribir en el archivo con write("lo que queremos escribir")
frase = "Estupendo, estoy creando un archivo de texto\nEs Genial\nSuper Genial"
archivoTexto.write(frase);

#4-Cierre del archivo con el metodo close()
archivoTexto.close()

##Abrir un Archivo en modo lectura
#1-Abri con el arguento r en el metodo open("archivo", "r")
archivoTexto = open("archivo.txt","r");
#2-Leer y alamacenar el texto con el metodo read()
texto = archivoTexto.read()
#3-Cierre del Archivo
archivoTexto.close();

print(texto);

##Alamacenar la informacion de un archivo en una lista
#1-Abrir el archivo en modo lectura
archivoTexto = open("archivo.txt","r");
#2-Usar metodo readlines() para convertir el texto en una lista manipulable
myLista = archivoTexto.readlines();
#3-Cierre del Archivo
archivoTexto.close();
#4-Impresion de la lista
print(myLista);
# Impresion de una linea del array
print(myLista[0]);
print("===================================================================");
for i in myLista:
	print(i);
print("===================================================================");

##AGREGAR TEXTO A UN ARCHIVO
#1-Abrir el archivo en modo append con open("archivo","a")
archivoTexto = open("archivo.txt","a");
#2-Escribir en el archivo
archivoTexto.write("\nSiempre es una Buena ocasion para estudiar Python");
#3-Cerrar archivo
archivoTexto.close();

#MANIPULACION DEL PUNTERO AL ABRIR EL ARCHIVO EXTERNO
#1-Abrir el archivo en modo lectura
archTexto = open("archivo.txt","r");
print(archTexto.read());
#2-Ubicar el puntero con el metodo
	#►seek(numeroCaracteresSituarPuntero)
archTexto.seek(0);#-Desplazar el puntero al comienzo

print(archTexto.read());
#3-Cerrar Archivo
archTexto.close();

##El metodo read hace lecturas, ingresando parametro, hasta donde se quiere leer
print("=======================================================================");
#Abrir Archivo
archTexto = open("archivo.txt","r");
#Realizar lectura hasta cierto caracter
print(archTexto.read(25));
#Si se imprime otra vez el archivo se realizara desde donde se dejo el puntero con seek
print(archTexto.read())

print("=======================================================================");
#Poner el cursor en la mitad de un archivo de texto
#1-Abrir el archivo
arcText = open("archivo.txt","r");
#Leer el texto con read() contarlo con len() y dividirlo en 2
arcText.seek(len(arcText.read())/2);
print(arcText.read());

print("=======================================================================");
#ABRIR EL ARCHIVO EN MODO DE LECTURA Y ESCRITURA
arcTexto = open("archivo.txt","r+");#Lectura y escritura "r+"
arcTexto.write("Texto al comienzo por no setear el cursor, ");

#> arcTexto.writelines(arrayPosicionCambiarTextoLinea)
