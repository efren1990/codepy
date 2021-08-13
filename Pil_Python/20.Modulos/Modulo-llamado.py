#xxxxxx------------------------------------------------------------->
#LLAMADO DE MODULOS
#xxxxxx------------------------------------------------------------->
"""
Para llamar un modulo en python se debe usar la instruccion import y el
nombre del archivo si la extension:

#import funMatematicas

#Para no tener que llamar las funciones del modulo sin usar el nombre se debe
llamar el modulo de la siguiente manera:

#from funMatematicas import sumar -> de esta manera se optimiza la aplicacion ya que
										solo se importa solo lo necesario del modulo

#Para llamar todo el codigo del modulo se debe:

from funMatematicas import *

"""
from funMatematicas import *

"""
PAra poder usar una funcion clase o metod del modulo importado hay que llamar
el modulo como un objeto el cual toma el nombre del archivo importado
nombreModulo.metodo-funcion-clase, etc.....

funMatematicas.sumar(4, 345);

"""
# Uso de la funcion sumar contenida en el modulo funMatematicas
sumar(4, 345);
restar(2, 20);
multiplicar(2, 48);