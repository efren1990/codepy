"""
EXCEPCIONES
--------------------------------------------------------------------------------
Todo programa por bien construido que se encuentre ira en algun momento
y por las razones mas insolitas a fallar.

Excepción es todo desvío de la regla general, es un objeto cuya clase
a partir de la cual se origino se extiende a partir de la clase
exception

La clase Exception es implementada por python y posee como unica finalidad
informar al usuario programador que un determinado error ocurrio 
exhibir en que modulo y en que linea el problema se origino y otra información
que el programador que implemento a dicha excepción juzgo que eran necesarias

Las Excepciones son codigos como cualquie otro, que implican la finalizacion 
de la aplicacion y el envio de un trace-back a nuestr salida standar

----------------------------------------------------------------------------------
FORMAS DE TRATAR LAS EXCEPCIONES
----------------------------------------------------------------------------------
Levantamiento de Excepciones
--------------------------------------------------
es todo código que al percibir un problema
cre una excepción avisadole asi al programador
--------------------------------------------------
Tratamiento de Excepciones
--------------------------------------------------
es todo código que identifica errores
e implementa una solución evintando
que la aplicacion sea finalizada.
--------------------------------------------------
CÓDIGO PARA TRATAR UNA EXCEPCION
--------------------------------------------------
try: -> Indica que se va a iniciar un tratamiento de excepciones
	código
except ErrorClass1: ->define los tipos de problemas que conocemos que puden llegar a ocurrir
	tratamiento
except ErrorClass2:

"""
#Generar intencionalmente un error para levantar una excepcion en python
try: # 
	a = 10/0 #No se puede dividir por 0 ZeroDivisionError:division by zero
	print(a)
except ZeroDivisionError: #except nombreErrorArrojadoEnConsola
	print("No se puede dividir por 0")



