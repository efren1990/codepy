Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 4
6
>>> a = b;
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> a = "b";
>>> a
'b'
>>> print a
  File "<stdin>", line 1
    print a
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a)?
>>> print(a)
b
>>> #Variable: Espacio en la memoria del ordenador donde se almacena un valor que 
... #Podra Cambiar durante la ejecucion del Programa
... 
>>> 
>>> 
>>> a = 3; b = 4; c = 6;
>>> c *(a + b)
42
>>> #Operador Modulo: % :es el Resto de una Division
... 
>>> 10 % 3
1
>>> #Operador Exponente: **: 5**3
... 
>>> 5**3
125
>>> #Operador Division Entera: / :
... 
>>> 9//2
4
>>> #Variable en Pyton:Nombre-nombre-nombre3-mi_nombre-miNombre
... 
>>> miNombre = "Efren";
>>> miNombre
'Efren'
>>> print(miNombre);
Efren
>>> #En Pyton el tipo de Variable lo define el Contenido y no el Contenedor
... #Python en un Lenguaje de Programacion Orientado a Objetos
... #para Python todo es un Objeto
... 
>>> nombre = 5
>>> #type-->Muestra el tipo de varible lo denomina class ya que toma la variable como un objeto
... 
>>> type(nombre);
<class 'int'>
>>> nombre = "juan";
>>> type(nombre);
<class 'str'>
>>> nombre = 5.2;
>>> type(nombre);
<class 'float'>
>>> #El Contenido Fue Cambiando por ende el tipo de dato tambien
... 
>>> #Los Saltos de Linea con Triple Comilla
... 
>>> mensaje = """Esto es un Mensaje
... con Tres Saltos
... de Linea""";
>>> print(mensaje);
Esto es un Mensaje
con Tres Saltos
de Linea