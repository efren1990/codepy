#xxxxxx------------------------------------------------------------->
#VENTANAS EMERGENTES II->
#xxxxxx------------------------------------------------------------->
"""
Ventana para guardar o abrir archivos
"""
# Importar libreria
from tkinter import *
# Modulo para Ventana
from tkinter import filedialog

# Ventana Raiz
vRaiz = Tk();
#xxxxxx------------------------------------------------------------->
#Funcion para abrir la ventana
def fichero():
	# Metodo para abrir un fichero
	#askopenfilename(title="titulo", initialdir="Si se quiere especificar una ruta inicial")
	#filetype="definir la extencion que se quiere ver inicialmente"->tiene que ser una 2 tuplas inicialmente
	fichero = filedialog.askopenfilename(title="Abrir", initialdir="c:", filetypes=(("Ficheros Excel", "*.xlsx",),
		("Ficheros De Texto", "*.txt"), ("Todos los ficheros", "*.")) );
	# Imprimir lo alamacenado en fichero
	print(fichero);
#xxxxxx------------------------------------------------------------->
# Boton para ejecutar la funcion que ejecutara la ventana
Button(vRaiz, text="Abrir Arcivo", command=fichero).pack();
# Ejecucion
vRaiz.mainloop();