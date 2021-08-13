#xxxxxx------------------------------------------------------------->
#INTERFCES GRAFICAS
#xxxxxx------------------------------------------------------------->
"""
TEXT->Crear entradas de Texto extenso
Button->Crea Botones
"""
# Importar Libreria
from tkinter import *

# Raiz
vRaiz = Tk();
# Contenedor Frame
usContent = Frame(vRaiz, width=800, height=600);
#Empaquetado Frame
usContent.pack();

#Para hacer que el boton introduzca un nombre en la entrada de texto nombre
#es necesario asociar el cuadro de texto con la variable que contendra el dato
#y decirle que es una cadena de caracteres
miNombre = StringVar()
"""
La variable se debe asignar con el comando textvariable=variable
y el valor se definira en la funcion que se ejecutara al aplicar el boton
"""


#Nombre de usuario
labNom = Label(usContent, text="Nombre: ");
labNom.grid(row=0, column=0);
entNom = Entry(usContent, textvariable=miNombre);
entNom.grid(row=0, column=1);
#Apellidos
labApe = Label(usContent, text="Apellidos: ");
labApe.grid(row=1, column=0);
entApe = Entry(usContent);
entApe.grid(row=1, column=1);
#Direccion
labDir = Label(usContent, text="Direccion: ");
labDir.grid(row=2, column=0);
entDir = Entry(usContent);
entDir.grid(row=2, column=1);
#Password
labPas = Label(usContent, text="Password: ");
labPas.grid(row=3, column=0);
entPas = Entry(usContent);
entPas.config(show="*");
entPas.grid(row=3, column=1)

#Comentarios----------->
#Text(contenedor, width, height)->Entrada extensa de texto
labComent = Label(usContent, text="Comentarios: ")
labComent.grid(row=4, column=0);
txComent = Text(usContent, width=15, height=5);
txComent.grid(row=4, column=1);
#Scroll en la caja de texto
#Scrollbar(contenedor, comand=cuadrotexto.yview(Vertical))->Se debe empaqquetar con el frid
scroll = Scrollbar(usContent, command=txComent.yview);
# Empaquetado del Scroll al lado derecho, por fuera del texto
#sticky="nsew"->Hace adaptar al scroll al elemento que pertenece-caja de texto
scroll.grid(row=4, column=3, sticky="nsew");
#Configurar el texto comentario para que el scroll siga el texto
#elemtnoTexto.config(yscrollcommand = elementoScroll);
txComent.config(yscrollcommand=scroll.set);
#Boton--------------------<
# Funcion para evento en el boton
def codigoBoton():
	miNombre.set("Efren");
#Fin Funcion	
# Crear Boton
# Button(contenedor, texto="TextoBotn")
btnEnvio = Button(vRaiz, text="Enviar", command=codigoBoton);
btnEnvio.pack();
#Desencadenar acciones en los botones
# command = funcion;
vRaiz.mainloop();



