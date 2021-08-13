#xxxxxx------------------------------------------------------------->
#INTERFCES GRAFICAS
#xxxxxx------------------------------------------------------------->
"""
Etiquetas de Texto
WIDGET LABEL->
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

#Crear un Label-> Label(Contenedor, valoresConfigurables) font=("fuente ins. en el ordenador", tamañoPX)
label = Label(frame, text="Hola...., Esto es Python Con la Libreria Tkinter", fg="gray", font=("Comic Sans Ms", 14));

#Empaquetar el label
#pack()->Empaqueta el texto y ajusta la ventana 
#palce(coorX, coorY)->nos permite ubicar el label donde queramos y respeta el tamaño de la raiz
label.place(x=10, y=10);
#Siplificacion del codigo
# Label(frame, "Hola...,Esto es Pythoon").place(x=10, x=10);


# Ejecutar la Ventana
raiz.mainloop();

