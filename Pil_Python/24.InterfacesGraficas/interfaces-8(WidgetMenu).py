#xxxxxx------------------------------------------------------------->
#WIDGET MENU
#xxxxxx------------------------------------------------------------->
"""
Permite Crear Barras de Menus
"""
# Importar libreria
from tkinter import *
# Impotar ventanas emergentes
from tkinter import messagebox

# Ventana Raiz
vRaiz = Tk();
#xxxxxx------------------------------------------------------------->
#Funcion para Crear ventanas emergentes de informacion->
def infoAdcional():
	# Metodo para Sacar el la Ventada emergente
	messagebox.showinfo("Procesador De Scorpion", "Procesador de Texto 1.0-2018");
#xxxxxx------------------------------------------------------------->
#xxxxxx------------------------------------------------------------->
#Funcion para Crear Ventana de Aviso
def avisoLicencia():
	#Metodo para Crear una ventana de Aviso
	messagebox.showwarning("Licencia", "Producto Bajo Licencia GNU");
#xxxxxx------------------------------------------------------------->
#xxxxxx------------------------------------------------------------->
#Funcion Para crear Ventadas de pregunta si o no
def salirApp():
	#Metodo para Crear ventana de pregunta si o no
	valor = messagebox.askquestion("Salir", "¿Deseas Salir De la Aplicacion?");
	#MEtodo para crear ventana ok-cancel askokcancel->devuelve true o false
	# valor = messagebox.askokcancel("Salir", "¿Desea Salir de la Aplicacion?");
	# askquestion->Devuelve valor si(yes) o no(no)
	# Validar respuesta
	if(valor == "yes"):
		# Destruir la ventana
		vRaiz.destroy();
#xxxxxx------------------------------------------------------------->
#xxxxxx------------------------------------------------------------->
#Funcion Para crear Ventadas ok o cancel
def salirApp2():
	#MEtodo para crear ventana ok-cancel 
	valor = messagebox.askokcancel("Salir", "¿Desea Salir de la Aplicacion?");
	# askokcancel->devuelve true o false
	# Validar respuesta
	if(valor == True):
		# Destruir la ventana
		vRaiz.destroy();
#xxxxxx------------------------------------------------------------->
#xxxxxx------------------------------------------------------------->
#Funcion para cerrar un documento o reintentar abrirlo
def cerrarDocumento():
	# Metodo para ventada de cierre de documentos
	valor = messagebox.askretrycancel("Reintentar", "No es posible Cerrar, Documento Bloqueado");
	#askretrycancel->devuelve Reintentar(True), cancelar(False);
	if(valor == False):
		vRaiz.destroy();
#xxxxxx------------------------------------------------------------->

#Crear Variable donde se va a almacenar el menu
#Metodo menu-> Menu(Contenedor)
barraMenu = Menu(vRaiz);
# Configurar la raiz para contruir el menu 
#Raiz.config(menu=ElementoMenu)
vRaiz.config(menu=barraMenu, width=600, height=500);

# Elementos del Menu(opciones)->Nombre Interno
# NombreElemento = Menu(ELMenuCreado);
#tearoff=0->Elimina la barra por defecto en la caja de los sub elementos
archivoMenu = Menu(barraMenu, tearoff=0);
# Agregar Sub Elementos al elemento del menu---->
# Elemento archivo->
# elemento.add_command(label="Nombre del Sub elemento");
archivoMenu.add_command(label="Nuevo");
archivoMenu.add_command(label="Abrir");
archivoMenu.add_command(label="Guardar");
archivoMenu.add_command(label="Guardar Como");
#Crar una Separacion 
archivoMenu.add_separator();
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento);
archivoMenu.add_command(label="Salir", command=salirApp2);
# Elemento Edicion->
archivoEdicion = Menu(barraMenu, tearoff=0);
archivoEdicion.add_command(label="Atras");
archivoEdicion.add_command(label="Adelante");
archivoEdicion.add_separator();
archivoEdicion.add_command(label="Copiar");
archivoEdicion.add_command(label="Cortar");
archivoEdicion.add_command(label="Pegar");

# Elemento Herramientas->
archivoHerramientas = Menu(barraMenu);
# Elemento Ayuda->
archivoAyuda = Menu(barraMenu, tearoff=0);
archivoAyuda.add_command(label="Licencia", command=avisoLicencia);
archivoAyuda.add_command(label="Acerca de...", command=infoAdcional)
# Agregar Texto a los elementos del Menu
# menuCreado.add_cascade(label="NombreELementoInterfaz", menu=NombreELementoCreado)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu);
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion);
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas);
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda);


#Ejecucion
vRaiz.mainloop();