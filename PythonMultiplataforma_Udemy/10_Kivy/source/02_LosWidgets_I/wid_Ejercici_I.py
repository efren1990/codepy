
"""
EJERCICIO:
UNA PATANLLA DE VERDAD
--------------------------------------------------------------------------------------
una pantalla con varios componentes
WIDGET LAYOUT
Usado como una ventana para contener mas widgets y ubicarlos en el espacio
"""
#coding: utf-8
#autor: Sr.Joker
# --------------------------------------------------------------------------------------
# Importar modulo de la apliccion clase App
from kivy.app import App
# Importar al gestor de layouts dentro del modulo uix
from kivy.uix.floatlayout import FloatLayout
# Importar widget TextInput
from kivy.uix.textinput import TextInput
# Importar widget Button
from kivy.uix.button import Button
# Funcion click para el boton, e imprimir el texto en la caja del text input

def click_button():
    print(txt_inp.text)
# Funcion para construccion den widget
def build_widget():
    # Gestor de layout
    layout = FloatLayout()
    # como prueba para tomar el texto con le boton, pero es una mala practica
    global txt_inp
    # Crear widget Text input
    txt_inp = TextInput(text="Excribe....")
    # Resetear la propiedad size_hint el elemento
    txt_inp.size_hint = None, None
    # Agregar nuemas dimensiones ancho y alto al elemento
    txt_inp.height = 250
    txt_inp.width = 200
    # Posiciones Y(desde el borde de abajo) y X(desde el borde izquiierdo)
    txt_inp.y = 300
    txt_inp.x = 50
    # Crear widget Button
    btn = Button(text="Click")
    btn.size_hint = None, None
    # Agregar nuemas dimensiones ancho y alto al elemento
    btn.height = 100
    btn.width = 200
    # Posiciones Y(desde el borde de abajo) y X(desde el borde izquiierdo)
    btn.y = 150
    btn.x = 50
    # Agregar evento click al boton on_press
    btn.on_press = click_button
    # Agregar elementos al layout
    # miLayout.add_widget(widgets)->Agregar widgets al layout
    layout.add_widget(txt_inp)
    layout.add_widget(btn)
    # Retorno
    return layout
# Instacia de la aplicacion
myApp = App()
# Poner titulo a la ventada de la app
myApp.title = "My App eXcript"
"""
Controlar la Dimension de la pantalla pricipal de la aplicacion
es decir la dimentison de la ventada o Window de la aplicacion
Se debe importar la clase Window de modulo kivy.core.window
"""
from kivy.core.window import Window
# Dar dimension a una ventana o la App en si misma
# Window.size = ancho, alto
Window.size = 300, 600
# asocioar la fucion de construccion de widgets
myApp.build = build_widget
# Ejecutar la aplicacion
myApp.run()