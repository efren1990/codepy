#xxxxxx------------------------------------------------------------->
#INTERFACES GRAFICAS DE USUARIO (GUI)
#xxxxxx------------------------------------------------------------->
"""
►Son ventanas con las cuales los usuarios interactuan con el programa
son intermediarios entre el programa y el usuario.
Estan formadas por un conjunto de graficos como ventanas, botones, menus
casillas de verificacion etc.

Librerias para crear GUI
#(GUI)-graphic user interface-> interfas grafica de usuario
►tkinter◄Viene instalada por defecto con python esta incluida en el
►WxPython
►PyQT
►PyGTK
entre otras
ESTRUCTURA DE UNA VENTANA CON TKINTER

1-RAIZ:(La Ventana general)
	
	2-FRAME:(Aglutinador, Organizador de elementos)(Tambien se considera como un widget)
		
		3-WIDGETS->elementos como: botones,menus,casillas,cuadros texto...etc

		
"""

# Llamado de la Libreria tkinter la cual se usa para 

from tkinter import *

# Raiz->
raiz = Tk();
# Titulo de la Ventana raiz title("Titulo Ventana")
raiz.title("Ventana 1");
#Impedir que se pueda redimensionar una ventana
#resizable(ancho(0=false)(1=True), alto(0=false)(1=True)) 0->no 1->si
raiz.resizable(1,1);

#Cambiar icono->solo archivos .ico
#iconbitmap("Ruta del Archivo .ico")
raiz.iconbitmap("iconoPc.ico");

#Definir la dimension de la ventana
#geometry("anchoXalto");
raiz.geometry("700x300");

#Cambiar Color de Fondo
#config(propiedad="valor")
raiz.config(bg="#fec35a");#bg(nombre o hexadecimal)->background
"""
#NOTA-> al campbiar el nombre del archivo 0.interfaces.py a 0.interfaces.pyw la ventana 
grafica se abrira al darle doble click sin necesidad de ejecutarlo por consola
"""

#mainloop crea la ventana el cual es un bucle infinito->Debe estar siempre al final
raiz.mainloop();