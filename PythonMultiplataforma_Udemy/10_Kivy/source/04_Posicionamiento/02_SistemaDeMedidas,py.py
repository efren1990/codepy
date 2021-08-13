"""
SISTEMA DE MEDIDA
------------------------------------------------------------------------------------------------------------------
PX    |  Pixeles ◄
M     |  Pulgadas
MM    |  Milímetros
PT    |  puntos
DP    |  pixel independiente de densidad   ◄
SP    |  Escala independiente de pixel     ◄

El sistema de medida se puede escger si es fijo o variaante (flotante responsive)

PIXEL ->
-----------------------------------------------------------
Píxel es un sistema de medida estandar utilizado por los
fabricantes de hadware y lenguajes de programación

    1 PIXEL = UN PUNTO EN EL DISPLAY

Partiendo de la idea de que una imagen se encuentra conformada
por un conglomerado de puntos.

Entonces un píxel representa el menor punto que un dispositivo
es capaz de exhibir.

El tamaño fisico del pixel varia, cuanto menor este sea, mayot sera
la resolucion.

Si una pantalla es de 1280x720 quiere decir
que son:
    1280 pixlees en el eje X - Ancho
    720 pixlees en el eje Y - Alto

-----------------------------------------------------------
DPI(dpi) ->
-----------------------------------------------------------
dpi (dots per inch o puntos por pulgada) es la medida obtenida
a partir de la division entre el tamaño fisico del display en
centimetros o pulgadas y la resolucion en pixeles.

Formula de calcular dpi:

      Tamaño Fisico Display
    ------------------------
      Resolucion Pixeles


-----------------------------------------------------------
DP(dp) ->
-----------------------------------------------------------
Densidad de pixeles es la cantidad de pixeles por pulgada
cuadrada

Formula Densidad Pantalla dt

      Longitud de Pantalla(altura) en Pixles        Pixel
    ------------------------------------------ = ---------------
     Longitud de pantalla(altura) en Pulgadas       Pulgada

Formula dp - pixel independiente de densidad

        Longitud en Pixeles * 160           pixel
    ---------------------------------- = -----------------
        Densidad pantalla                   dt

dp -> grantiza la misma posicion y dimension, independientemente de la resolucion
sp-> es el tamaño de medida de las fuentes
"""