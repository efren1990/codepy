#coding: utf-8
"""

"""
# Importar clase App modulo kivy.app
from kivy.app import App
# Importar la clase Label
from kivy.uix.label import Label

#  Funcion para retornar una instancia del label
def build_label():
    # Instacia de la clase Label
    lb = Label()
    lb.text = "Aplicación con Python y Kivy Multiplataforma"
    lb.italic = True
    # Las medidas de la biblioteca siempre estaran en pixeles
    lb.font_size = 45
    return lb

# Instacia de la clase App
app_instance = App()

# Pasar al metod build de la clase App la asociacion de la funcion
# que retorna la instancia de Label
app_instance.build = build_label

# Ejecutar la aplicacion
app_instance.run()
