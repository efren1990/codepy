"""
APLICACION PARA UN CRUD VISUAL-----------------------------------------------------
"""
# Imporatcion de modulos y librerias->
# Libreria grafica tkinter
from tkinter import *
# Libreria de mensajes emergentes tkinter
from tkinter import messagebox
# Libreria sqlit3
import sqlite3
# VENTANA RAIZ---------------------------------------------------------------------------------
# Ventana raiz grafica
root = Tk()
# Barra de menu inicial
barraMenu = Menu(root)
# Configurar la raiz y pasar el menu
root.config(menu=barraMenu, width=300, height=500, bg="#666")
# BARA MENU------------------------------------------------------------------------------------
# Agregar Seccion menu de la base de datos al menu de la spp
bdMenu = Menu(barraMenu, tearoff=0)
# Agregar opciones a la seccion menu de la bd
bdMenu.add_command(label="Conectar")
bdMenu.add_command(label="Salir")

# Seccion de borrar campos
borCambMenu = Menu(barraMenu, tearoff=0)
# Agragar opciones de menu seccion
borCambMenu.add_command(label="Limpiar Datos")

# Seccion de menu crud
crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar") 

# Seccion de menu ayuda
helpMenu = Menu(barraMenu, tearoff=0)
helpMenu.add_command(label="Licencia")
helpMenu.add_command(label="Acerca de")

# Agregar opciondes del menu a la barra de menu
# Seccion base de datos
barraMenu.add_cascade(label="BD", menu=bdMenu)
# Seccion Limpiar datos
barraMenu.add_cascade(label="Limpiar", menu=borCambMenu)
# Seccion crud
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
# Seccion ayuda
barraMenu.add_cascade(label="Ayuda", menu=helpMenu)
#---------------------------------------------------------------------------------------
#CAMPOS----------------------------------------------------------------------------------
# Frame General 
frameCampos = Frame(root)
# Empaquetar el frame
frameCampos.pack()


# Ejecutar loop para la ventana grafica
root.mainloop()