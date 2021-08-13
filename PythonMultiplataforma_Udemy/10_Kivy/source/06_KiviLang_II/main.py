"""
HELLO WORD CON KIVY LANG
Usando el lenguaje kigylang

"""
# Importar clase App
from kivy.app import App
# Importar la clase Label
from kivy.uix.label import Label

"""
Clase que construye la interface grafica el nombre de la clase influye
en el archivo de extencion .kv para el lenguaje KivyLang.

EL NOMBRE DEL ARCHIVO DEBE LLEVAR EL PRIMER NOMBRE DE LA CLASE DE CONSTRUCCION DE INTEFACES
ESTE PRIMER NOMBRE DEBE SER EN MINUSCUALA EJEMPLO
    class ConstructorInter():
        pass
ARCHIVO: constructor.kv 
"""
# La clase constructora de interfaces recibe la clase App como parametro
class HelloApp(App):
    pass
# Ejecutar la aplicaion llamando la clase
HelloApp().run()