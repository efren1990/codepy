#coding: utf-8
"""
EL WIDGET TEXT INPUT
Permite el ingreso de datos
"""
# Importar Clase App del modulo kiby.app
from kivy.app import App
# Importar clase TextInput
from kivy.uix.textinput import TextInput

# Instacia de la clase App
myApp = App()
# Funcion que retorna el widget
def build_input():
    txt_inp = TextInput()
    # Insertar un valor de texto
    txt_inp.text = "Escribe algo"
    return txt_inp
# Pasar al metodo contructor de App los widegets
myApp.build = build_input
# Ejecutar la aplicacion
myApp.run()