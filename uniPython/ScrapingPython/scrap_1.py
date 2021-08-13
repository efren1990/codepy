"""
Aplicación: Extracción de nombres y URLs de una página HTML
¿Qué es Beautiful Soup?
“Si sólo tratas de sacar datos de una web. Beautiful Soup está aquí para ayudar “.

Beautiful Soup es una librería Python para obtener datos de HTML, XML y otros lenguajes de marcado. 
Digamos que has encontrado algunas páginas web que muestran datos relevantes para ti, como información de fechas, 
contenido, dirección, valores… pero esa web no proporciona ninguna forma de descargar los datos directamente. 
Beautiful Soup te ayuda a extraer contenido particular de una página web, elimina el marcado HTML, guardar la información e incluso 
te lo exporta en un archivo excel.

La documentación de Beautiful Soup le dará una idea de la variedad de cosas que la biblioteca Beautiful Soup le ayudará, 
desde aislar títulos y enlaces, extraer todo el texto de las etiquetas html, 
hasta alterar el HTML dentro del documento con el que está trabajando.
"""
# Es necesario de la importacion de la libreria beatifulsoap
from bs4 import BeautifulSoup
import csv
# Libreria que se encarga de leer y trabajar con urls en python , tambier permite interactuar con datos web
# urllib -> permitira hacer request a las url
import urllib3

# Objeto para el request de la conexion a la url y poder hacer las solicitudes
http = urllib3.PoolManager()
# Hacer el request de la web a escapear
web = http.request('GET', 'https://www.colciencias.gov.co/convocatorias')
# Instacia del la clase beatifulsoap(web.data)->permite extraer datos de la web
soup = BeautifulSoup(web.data)
#Estraer el titulo de la web
titulo = soup.title.text
print(titulo)

