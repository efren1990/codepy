
"""
KIVY ORIENTADO A OBJETOS
--------------------------------------------------------------------------------------
Construir codigo mas orientado a objetos
"""
#coding utf-8
# Importar modulo de la apliccion clase App
from kivy.app import App
# Importar calse Label
from kivy.uix.label import Label
# Importar al gestor de layouts dentro del modulo uix
# --------------------------------------------------------------------------------------
# CLASE DE LA APLICACION
"""Recibe la Clase App de la biblioteca la cual heredara de App() class"""
# --------------------------------------------------------------------------------------
class MyAppBuidl(App):
    # Funcion de construccion interface
    def build_interface(self):
        return Label(text="Hola mundo")
# --------------------------------------------------------------------------------------
# Ejecutar aplicacion
MyAppBuidl().run()