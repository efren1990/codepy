"""
LOS WIDGETS
Los widgets son elementos de una interfaz gráfica de usuario que forman parte de la Experiencia del usuario . El kivy . El módulo uix contiene clases para crear y administrar widgets.

EL WIDGET BUTTON
Es un componente de la biblioteca que funciona como un boton
"""
# Importar Clase App del modulo kiby.app
from kivy.app import App
# Importar  la clase Button para el boton
from kivy.uix.button import Button

# Funcion para realizar eventos en la funcion
def click():
    print("El Btono fue presionado")
# Funcion para Construir una instancia del widget Button
def build_button():
    bt = Button()
    bt.text = "Click"
    # Agregar un evento de funcion al boton
    # boton.on_press = funcionAsociar
    bt.on_press = click
    return bt

# Instacia de la clase App
myApp = App()
# Pasar al metodo contructor de App los widegets
myApp.build = build_button
# Ejecutar aplicacion
myApp.run()