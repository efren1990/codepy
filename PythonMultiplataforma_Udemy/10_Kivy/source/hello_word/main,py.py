#coding: utf-8
"""
APP HELLO WORD
"""
# Importar linrerias Kivy clase App
from kivy.app import App
# Clase para etiquetas label de texto
from kivy.uix.label import Label

# Funcion que retorna un componente
def build():
    """Crear un widget el cual sera un label
        Label(txt="Texto a imprimir o mostrar")
    """
    return Label(text="Hello Word")
# Crear una instancia de la aplicacion App kivy y almacenarla en una variable}
# La cual se converitar en una instacia de la clase App de la libreria kivy
hello_word = App()
# Llamaar la funcion que retorna el label dentro de la ventana App()
hello_word.build = build
# Aplicacion minima para crear en kivy
# run()->Ejecuta la biblioteca kivy creando la ventana pricipal
hello_word.run()

