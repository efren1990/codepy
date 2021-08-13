"""
#REBANANDO STRINGS - DIVIDIR STTRINGS
---------------------------------------------------------------------
Para python todo string es una lista de caracteres inmutables(no se puede adicionar o eliminar un parte de un string)
si embargo no impide manipular de diversas formas un string
o inclisive generar un nuevo string que contiene una nueva alteracion
"""
s = "Para python todo string es un lista inmutable."
print(s)
# Ya que un string es una lista, podemos acceder a cada caracter
print(s[0])
print(s[1])
# Para python todo es un string
print(type(s))
print(type(s[0]))
# Podemos acceder al ultimo caracter
print(s[-1])
# REBANADO DE STRINGS------------------
# De la misma forma que las listas
# strin[inicio:fin:pasos]
print(s[5:11:1])
r = s[5:11:1]
b = s[-11:-1:1]
print(r + b)
print(s[0:11])
# Imprimir el string inversamente
print(s[::-1])
# De 2 en 2
print(s[::2])
print("Hola Mundo")