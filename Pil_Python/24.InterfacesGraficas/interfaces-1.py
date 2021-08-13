#xxxxxx------------------------------------------------------------->
#INTERFACES GRAFICAS
#xxxxxx------------------------------------------------------------->
"""
Contruir un Frame dentro de la Ventana raiz->
"""
# Importar libreria
from tkinter import *
# Crear raiz
raiz = Tk();

#Titulo->
raiz.title("Ventana 2");

#Icono
raiz.iconbitmap("iconoPc.ico");

#Diemnsiones width height->se debe quitar para darle tamaño al frame
# raiz.geometry("800x300");->La ventana simpre se adapta al contenido

#Cambio color background
raiz.config(bg="#fec35a");
#al redimenzionar la raiz se mostrara el color de la ventana raiz 

#Crear el Frame
#Frame()
Vframe = Frame();

#Empaquetar el frame en la raiz (instroducir)
#pack()->El metodo pack permite parametros diversos

#side->indica el lado a ubicar el frame, 
#anchor->posiciona segun los putnos cardinales norte,sur,este,oeste->pack(side="left", anchor="n");

#Rellenar uno de los sectores de la raiz
#fill-> rellena en una posicion x o y agregandole->expand="True" fill="x", expand="True"
#Expandir el frame en ambas direcciones-> fill="both"
Vframe.pack(side="left", anchor="n");

#Cambiar caracteristicas del frame
Vframe.config(bg="blue");
#Tamaño del Frame
Vframe.config(width="800", height="430");
#Cambiar borde del frame->
# bd="valor"
#Grosor de borde
Vframe.config(bd="10");
#relief="valores":
	#groove-Borde tipo marco de cuadro
	#sunken
Vframe.config(relief="groove");
#hover en el frame efecto cursor
#cursor = "valor"->hand2, pirate, etc...
Vframe.config(cursor="hand2")





#Ejecuta la Ventana
#mainloop()
raiz.mainloop()
