"""------------------------------------------- EJERCICIOS 1 ---------------------------------------------------"""
"""
1-Realice un algoritmo que imprima solamente su nombre en la pantalla y seguidamente finalice la aplicación
"""
print("Efren")

"""
2-Realice un algoritmo que solicite al usuario que escriba su nombre y seguidamente envíe la siguiente frase a la salida estándar:
 "Su nombre es: [nombre del usuario]".
"""
nombre = input("Ingrese su Nombre: ")
print("Su nombre es: ", nombre)


"""
-Realice un algoritmo que solicite al usuario que escriba su nombre y seguidamente envíe la siguiente frase a la salida estándar: 
"Su nombre es: [nombre del usuario]".
"""
nombre_Us = input("Ingrese su nombre: ")
edad_Us = input("Ingresew su Edad: ")
print("El nombre del usuario es: ",nombre_Us," Y La edad del usuario es: ",edad_Us)


"""4- Realice un algoritmo que solicite al usuario informar un número. 
Seguidamente, almacene a este número en una variable. Por último, envíe a ese número a la salida estándar."""
numero = input("Ingrese su Codigo: ")
print("Su codigo es: ", numero)


"""
5) Realice un algoritmo que solicite al usuario informar un número. 
Seguidamente, escriba el siguiente mensaje  "El número escrito fue:   "
"""
numero_x = input("Ingrese un Numero X: ")
print("El numero Escrito fue: ", numero_x)

"""
6) Realice un algoritmo que solicite al usuario informar 3 números. 
Seguidamente, sume los valores y envíe a la salida estándar la siguiente frase "La suma total es:  ".
"""
numeroA = float(input("Ingrese el numero 1: "))
numeroB = float(input("Ingrese el numero 2: "))
numeroC = float(input("Ingrese el numero 3: "))
suma = numeroA + numeroB + numeroC
print("La suma total de los numero es: ", suma)

"""
7) Realice un algoritmo que solicite al usuario informar 2 números. 
Seguidamente, sume los valores y envíe a la salida estándar la siguiente frase: "La suma entre <X> e <Y> es igual a <total>"
"""
numeroF = float(input("Ingrese el numero X: "))
numeroG = float(input("Ingrese el numero Y: "))
print("La suma entre", numeroF, " e ", numeroG, " es igual a: ", numeroF + numeroG)

"""
8) Realice un algoritmo que solicite las notas de las 4 pruebas semestrales al usuario. 
Seguidamente, calcule la media y envíe el valor resultante a la salida estándar:
"""
nota_1 = float(input("Ingrese la nota 1: "))
nota_2 = float(input("Ingrese la nota 2: "))
nota_3 = float(input("Ingrese la nota 3: "))
nota_4 = float(input("Ingrese la nota 4: "))
print("El total ponderado es: ", (nota_1 + nota_2 + nota_3 + nota_4) / 4)

"""
9) Realice un algoritmo que solicite al usuario que informe una medida en metros. 
Seguidamente, convierta a esta medida de metros a centímetros y envíela a la salida estándar.
"""
medida = float(input("Ingrese la medida a convertir: "))
conversion = medida * 100
print("El total en centimetro de ", medida, " Metros es: ", conversion)


"""
10) Realice un algoritmo que calcule el cubo y el cuadrado de un determinado número:
"""
numExp = float(input("Ingrese el numero para elevar al cuadrado y el cubo: "))
cuadrado = numExp ** 2;
cubo = numExp ** 3;
print("Cuadrado: ",cuadrado," Cubo: ",cubo);


"""
11) Realice un algoritmo que solicite al usuario que escriba 2 números. 
Seguidamente, imprima el total de la división en números  decimales y el total de la división en números enteros ( es decir, sin casillas decimales).
"""

"""
12) Realice un algoritmo que solicite al usuario la longitud y la altura de un cuadrado. 
Seguidamente, imprima para el usuario cuántos metros cuadrados posee el área total del cuadrado.

13) Realice un algoritmo que solicite al usuario informar una cantidad de días, horas, minutos y segundos. Seguidamente, convierta todo a segundos.

14) Realice un algoritmo que solicite al usuario informar el valor de una compra.
Seguidamente, aplique un 10% de descuento e imprima en la pantalla tanto el valor total como el valor con el descuento aplicado. 
"""
