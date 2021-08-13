#xxxxxx------------------------------------------------------------->
#INTERFCES GRAFICAS
#xxxxxx------------------------------------------------------------->
"""
REJILLA->GRID
La rejilla o grid, se usa para crear una rejilla o tabla dentro de la
interfaz grafica de python, permitiendonos ubicar elemntos de forma
correcta y alineada
"""
# Imports de librerias
from tkinter import *
from tkinter import ttk 
#Ventana raiz
vetRaiz = Tk();
# vetRaiz.config(bg="black")
#Frame para la entrada de texto
miFrame = Frame(vetRaiz, width=800, height=400);
#Empaquetar el Frame
miFrame.pack(side="left", anchor="n");

#Cuadro De Txto
txNombre = Entry(miFrame);

# Grid para Posicionamiento de elementos
"""grid(row(fila), column(columna)) para posicionar un elemento con grid
se debe usar el metodo grid con el elemento y darle las cordenadas
row -> filas-> cuenta desde 0, 1 , 2 etc
column-> columna -> cuenta desde 0 , 1 

"""
txNombre.grid(row=0, column=1, sticky="e", pady=2);

#label para el texto
labNombre = Label(miFrame, text="Nombre: ");
labNombre.config(fg="blue");
#El label quedara antes del cuadro de texto debido a la organizacion de rejill
labNombre.grid(row=0, column=0, sticky="e", pady=2);

#Mas elementos---->
lab2 = Label(miFrame, text="Apellidos: ");
lab2.grid(row=1, column=0, sticky="e", pady=2);
#Entrada
ent2 = Entry(miFrame);
ent2.grid(row=1, column=1);

#Direccion usuario
#Labels->
lab3 = Label(miFrame, text="Direccion Residencia: ");
lab3.grid(row=2, column=0, sticky="e", pady=2);
#Entrys->
ent3 = Entry(miFrame);
ent3.grid(row=2, column=1);

#Password de usuasrip
# Labels->
labPass = Label(miFrame, text="Password");
labPass.grid(row=3, column=0, sticky="e", pady=2);
# Entradas->
entPass = Entry(miFrame);
entPass.grid(row=3, column=1);
#Configuracion de la entrada del pass
#show-> Remplaza el texto ingresado por el caracter especificado
entPass.config(show="*");

# Usar sticky para ubicar los elementos segun los puntos cardinales:
"""
Norte-> n
Sur->   s
Este->  e
Oeste-> w
NortEste->  ne
SurEste->   se
NortOeste-> nw
SurOeste->  sw
"""

#Uso de Padding para separar elementos
"""
pady-> Padding vertical en eje Y
padx-> padding horizontal en eje x
"""
#Correr la Ventana
vetRaiz.mainloop();