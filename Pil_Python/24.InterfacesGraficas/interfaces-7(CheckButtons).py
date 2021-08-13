#xxxxxx------------------------------------------------------------->
#BOTONES TIPO CHECKBOX
#xxxxxx------------------------------------------------------------->
"""
Botones de seleccion para preguntas de respuesta múltiple
"""
# Importar Libreria
from tkinter import *
#Ventana Raiz
vRaiz = Tk();
# Titulo de la Ventana
vRaiz.title("Agencia de Viajes");
#Asignacion de Variables get
playa = IntVar();
montain = IntVar();
turismoRural = IntVar();
# Funcion para paso de respuesta
def opcionViaje():
	# Variable para el Mensaje de Respuesta
	opcionEscogida = "";
	
	# Si la Variable get playa tiene el valor indicado
	if(playa.get() == 1):
		# Agregar opcion de Viaje a la Variable Para mensaje
		opcionEscogida+=" Playa,";

	if(montain.get() == 1):
		opcionEscogida+=" Montaña,";

	if(turismoRural.get() == 1):
		opcionEscogida+=" Turismo Rural";
	# Alamacenar las opciones escogidas en la variable respuesta
	respuestaSeleccion.config(text=opcionEscogida);
# Fin FUncion
# Crear Imagen
imagen = PhotoImage(file="Mouse.png");
# Imagen en Label
Label(vRaiz, image=imagen).pack();

# Frame para lo Botones
frame = Frame(vRaiz);
frame.pack();
#Label en el frame
Label(frame, text="Elige Destinos", width=80).pack();
# Checkbutton(ventanaRaix, text="Texto", onvalue=valorSeleccionado, offvalue=ValorNoSeleccionado).pack()
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionViaje).pack();
Checkbutton(frame, text="Montaña", variable=montain, onvalue=1, offvalue=0, command=opcionViaje).pack();
Checkbutton(frame, text="Turismo Rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionViaje).pack();
# Mensaje de Respuesta
respuestaSeleccion = Label(frame);
respuestaSeleccion.pack();
# Ejecucion
vRaiz.mainloop();