"""-----------------------------------------OPERADORES RELACIONALES--------------------------------------------"""
"""
Son los que se usan para realizar comparaciones entre 2 o mas datos
-Mayor que: >
Menor que: <
Mayor o Igual que: >=
Menor o igual que: <=

"""
#Variable para el nombre
usuario = input("Diga su nombre: ");
edad = int(input("Gigite su Edad"));
#Validacion de la edad ingresada
if(edad < 0):
    print("Su Edad no puede ser menor que 0")
else:
    if(edad > 150):
        print("Su edad no puede ser mayor a 150 años")
    else:
        if(edad < 18):
            print("No ttienes la edad, necesitas mas de 18 años")


"""------------------------------------CONDICIONAL RESUMIDO------------------------------------------"""
if(edad < 0):
    print("Su edad no puede ser menor que 0")
elif(edad > 150):
    print("Su edad no puede ser mayor a 150 años")
elif(edad < 18):
    print("No tienes la Edad")
else:
    print("Eres mayor de Edad")