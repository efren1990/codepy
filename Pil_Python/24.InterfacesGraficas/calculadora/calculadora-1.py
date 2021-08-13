#xxxxxx------------------------------------------------------------->
#CALCULADORA-EJERCICIO
#xxxxxx------------------------------------------------------------->
"""

"""
from tkinter import *
# Ventana Raiz
vRaiz = Tk();
# Frame
miFrame = Frame(vRaiz);
#Empaquetado pack para que se ajuste a su contenido
miFrame.pack();
# Creamos Variable Operacion para preguntar que operacion se va  a realizar
#Se inicia vacia para cuando inicie la calculadora no efectue ninguna operacion
operacion = "";
#Variable Resultado para almacenar el resultado el cual inicia en 0
resultado = 0;
# Pantalla Calculadora------------------------------------>
# Logica->
numeroPantalla = StringVar();

pantalla = Entry(miFrame, textvariable=numeroPantalla);
# Ubicacion Pantalla
#columnspan=definir cuantas columnas abarcara el elemento
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4);
pantalla.config(bg="black", fg="#03f943", justify="right");

# Pulsaciones Teclado---------------------------------------------------------------------->
# Funcion para poner numeros en la pantalla de la Calculadora
# set()->Establece un valor en pantalla
# get()->Obtiene la informacion que hay en pantalla
def numPulsado(num):
	#Declarar variable global operacion y resultado para poder usarlas en otras funciones y conservar
	#sus valores
	global operacion;
	#Validar que operion se va a realizar o no
	if (operacion != ""):
	#si se ha pulsado el boton suma y operacion es diferente de vacion
	#evitar concatenar y poner el nuevo numero a pulsar
		numeroPantalla.set(num);
		# Pasar a vacio operacion para que se pueda concatenar numeros nuevamenta
		operacion = "";
	else: 
		# Pasar un numero a la pantalla con .set(valor) get trae el numero que esta en pantalla
		numeroPantalla.set(numeroPantalla.get() + num);
		
# Funcion Suma--------------------------------------------------------------------------->
def suma(num):
	#Trabajar con la variable global operacion
	global operacion;
	global resultado;
	#Resultado de las operaciones
	resultado+=int(num);
	# Al llamarse la funcion la variable operacion pasa a valer suma
	operacion = "suma";
	#Pasar el Resultado a la Pantalla set(valor,dato);
	numeroPantalla.set(resultado);
#----------------------------------------------------------------------------------------------#
# Funcion Igual-------------------------------------------------------------------------------->
def igual():
	# Trabajar con la variable global resultado
	global resultado;
	# sumatoria de los numeros introducidos y el actual en pantalla
	numeroPantalla.set(resultado + int(numeroPantalla.get()));
	# Resetear resultado para que al presionar suma o igual no se sume nuevamente lo ya guardado
	resultado = 0;

#-----------------------------------------------------------------------------------------------
# Fila de Botons 1----------------------------------------->
boton7 = Button(miFrame, text="7", width=3, command=lambda:numPulsado("7"));
boton7.grid(row=2, column=1);

boton8 = Button(miFrame, text="8", width=3, command=lambda:numPulsado("8"));
boton8.grid(row=2, column=2);

boton9 = Button(miFrame, text="9", width=3, command=lambda:numPulsado("9"));
boton9.grid(row=2, column=3);

botonDiv = Button(miFrame, text="/", width=3);
botonDiv.grid(row=2, column=4);
# Fila de Botons 2----------------------------------------->
"""Al poner parantesis en la funcion en python, el flujo del programa
la leera de inmediato por ende almacenara el cuatro y lo enviara
a numero pulsado generarndo un error, para esto se usan las funcinoes
lambda(funciones anonimas) la cual guardara el valor y lo pasara al hacer
click en el boton"""
boton4 = Button(miFrame, text="4", width=3, command=lambda:numPulsado("4"));
boton4.grid(row=3, column=1);

boton5 = Button(miFrame, text="5", width=3, command=lambda:numPulsado("5"));
boton5.grid(row=3, column=2);

boton6 = Button(miFrame, text="6", width=3, command=lambda:numPulsado("6"));
boton6.grid(row=3, column=3);

botonMult = Button(miFrame, text="x", width=3);
botonMult.grid(row=3, column=4);
# Fila de Botons 3----------------------------------------->
boton1 = Button(miFrame, text="1", width=3, command=lambda:numPulsado("1"));
boton1.grid(row=4, column=1);

boton2 = Button(miFrame, text="2", width=3, command=lambda:numPulsado("2"));
boton2.grid(row=4, column=2);

boton3 = Button(miFrame, text="3", width=3, command=lambda:numPulsado("3"));
boton3.grid(row=4, column=3);

botonRest = Button(miFrame, text="-", width=3);
botonRest.grid(row=4, column=4);
# Fila de Botons 4----------------------------------------->
boton0 = Button(miFrame, text="0", width=3, command=lambda:numPulsado("0"));
boton0.grid(row=5, column=1);

botonComa = Button(miFrame, text=",", width=3, command=lambda:numPulsado(","));
botonComa.grid(row=5, column=2);

botonIgual = Button(miFrame, text="=", width=3, command=lambda:igual());
botonIgual.grid(row=5, column=3);

botonSuma = Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()) );
botonSuma.grid(row=5, column=4);
#Ejecucion
vRaiz.mainloop();