#xxxxxx------------------------------------------------------------->
#INTERFCES GRAFICAS
#xxxxxx------------------------------------------------------------->
"""
Etiquetas de Texto
WIDGET ENTRY->
►widgets utilizado Para permitir entradas de texto por parte
del ususario

►Opciones:
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
# Importar Libreria
from tkinter import *
from tkinter import ttk 
#Raiz o Ventana Principal
ventanaRaiz = Tk();
ventanaRaiz.config(bg="#648BDA", bd="3", relief="solid");
#Frame
miFrame = Frame(ventanaRaiz, width=450, height=200, bg="#A9A9FF");
miFrame.pack();
#Crear entrada de texto
#Entry(contenedor a quien va a pertenecer)
cuadroTexto = Entry(miFrame);
#Empaquetar el cuadro de entrada de texto
cuadroTexto.place(x=10, y=10);
#Ejecucion de la Ventana
ventanaRaiz.mainloop()