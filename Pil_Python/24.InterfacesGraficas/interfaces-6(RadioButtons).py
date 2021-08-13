#xxxxxx------------------------------------------------------------->
#BOTONES DE RADIO(RADIOBUTTONS)
#xxxxxx------------------------------------------------------------->
"""
Botones de seleccion para preguntas de respuesta unica
"""
# Libreria
from tkinter import *
# Raiz
vRaiz = Tk();
#Asignar variable a los radiobuttons
varOpcion = IntVar();
# Funcion Imprimi-------------------------------->
def imprimir():
	# Imprimir el Valor del Radiobutton seleccionado
	# Traer el Valor con el metodo get()
	# print(varOpcion.get())
	#Validar el valor para imprimir el genero seleccionado
	if(varOpcion.get() == 1):
		#Cambiar texto de un label con config
		etiqueta.config(text="Seleccionaste Masculino");
	elif(varOpcion.get() == 2):
		etiqueta.config(text="Has elegido Femenino");
	else:
		etiqueta.config(text="Has elegido Otras Opciones");  
#------------------------------------------------#
#Label
Label(vRaiz, text="Selecciona Tu Genero: ").pack();
#Boton de radio
#Radiobutton(Contenedor, text="seleccion", variable=variableAsignacion, value=ValorSeleccion);
Radiobutton(vRaiz, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack();
Radiobutton(vRaiz, text="Femenino",variable=varOpcion, value=2, command=imprimir).pack();
Radiobutton(vRaiz, text="Otras Opciones",variable=varOpcion, value=3, command=imprimir).pack();
etiqueta = Label(vRaiz);
# Empaquetado
etiqueta.pack();



#loop
vRaiz.mainloop();