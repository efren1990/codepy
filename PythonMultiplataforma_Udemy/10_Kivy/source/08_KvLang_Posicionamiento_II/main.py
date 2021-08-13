"""
POSICIONAMIENTO EN KIVY
---------------------------------------------------------------------------------------------------------------------
Propiedades que definen el posicionamiento de los Widgets.

Existen 20 propiedades para posicionar y dimensionar widgets

El posicionamiento porcentual es manipulado por los gestores de layout, por lo tanto algunas
propiedades funcionan de forma diferente en los diferentes gestores

GESTORES DE LAYOUTS
-------------------------------------------------------------------------
Son widgets que organizan Widgets
-------------------------------------------------------------------------

###SUFIJO HINT
Propiedades que presentan el sufijo hint, significan que su valores
deben ser definidos en valores porcentuales.

Ejemplo:

    pos_hint
    size_hint

VALORES PORCENTUALES
-------------------------------------------------------------------------
Deben estar dentro del intervalo 0.0 y 1.0

Ejemplo:
    1. = 100%
    0.01 = 1%

PROPIEDADES PARA POSICIONAMIENTO PORCENTUAL
-------------------------------------------------------------------------

####POS_HINT
    La propiedad pos_hint espera un diccionario con los ejes asociados
    a valores porcentuales, todo widget presenta a la propiedad pos_hint

    Ej:
        pos_hin:{"x":1., "y": .1}
        pos_hin:{"x":1.}
        pos_hin:{"y": .5}

PROPIEDADES PARA POSICIONAMIENTO ABSOLUTO
-------------------------------------------------------------------------
Todo widget es posicionado a travez de las porpiedades X y Y, ya
que son las propiedades que determinan el posicionamiento de
un widget en una salida.

Para el posicionamiento absoluto:

Las propiedades X y Y definen a las dimensiones en pixeles

####POS - Atajo de X y Y
    La propiedad pos recibe una tupla donde el primer valor
    es atribuido a la propiedad X y el segundo valor a la
    propiedad Y
    EJ:
        Button:
            x: 30
            y: 100

        Button:
            pos: 100, 300

"""
