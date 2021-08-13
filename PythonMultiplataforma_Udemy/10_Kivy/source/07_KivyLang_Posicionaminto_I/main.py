#condig utf-8
#############################
###### {SR}: [JOKER] ########
######  1990         ########
#############################
# Importar clase App
from kivy.app import App
# Importar clase float layout
from kivy.uix.floatlayout import FloatLayout
# Importar Clase Boton
from kivy.uix.button import Button
# Clase Gestora de layout, contendra clase gestora de layout
# Contendra todos widgets del archivo medida.kv
class RootWidget(FloatLayout):
    pass
# Clase Principa de la Aplicacion
class MedidaApp(App):
    # Metodo para construir que retorna instancia de la clase RootWidget
    def build(self):
        return RootWidget()

# Ejecutar Aplicacion{
MedidaApp().run()