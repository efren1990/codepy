#xxxxxx------------------------------------------------------------->
#INTERFCES GRAFICAS
#xxxxxx------------------------------------------------------------->
"""
Etiquetas de Texto
WIDGET LABEL-IMAGEN->
►widgets utilizados para mostrar texto e imagenes
►Tienen como unica finalidad mostrar texto, no se puede
interactuar con el(borrar, arrastrar, etc...) es solo un texto estatico

►variableLabel = Label(contenedor, opciones)
Opciones:
Text->Texto que se muestra en el label
Anchor->Conotrola la posicion del texto si hay espacio suficionete
		para el
Bg->Color de fondo
Bitmap->Mapa de bits que se mostrara como grafico
Bd->grosor de borde(2px por defecto)
font->Tipo de fuente a mostrar
Fg->color de la fuente
Width->Ancho de Label en caracteres(no en pixels)
height->Altura del Label en caractere(no en pixeles)
image->Muestra imagen en el label en lugar de texto
justify->Justificacion del Texto label	
"""
from tkinter import *
# Importar nuevos Widgets tkinter
from tkinter import ttk

#Crear Raiz
raiz = Tk();

# Crear Frame
frame = Frame(raiz, width=500, height=400);

# Empaquetar el frame en la raiz
frame.pack();

#IMAGENES EN LABE->
"""Tkinter solo deja trabajar imagenes gif y png por defecto para trabajar
otros formatos se debe importar otras librerias"""
# Crear imagen
#PhotoImage(flie="Ruta de la image")
miImagen = PhotoImage(file="Mouse.png");
#Creamos el Label y ponemos la imagen en vez del texto
Label(frame, image= miImagen).place(x=0, y=0);

#Ejecutamos el bucle Raiz
raiz.mainloop();