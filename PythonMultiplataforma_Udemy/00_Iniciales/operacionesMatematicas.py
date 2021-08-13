"""
-------------------------------Operaciones Matematicas en python--------------------------------------------
Python permite por defecto hacer operaciones matematicas usando los operadores sencillo
Suma
resta
Multiplicacion
Division
Modulo de la Division
"""
a = 5;
b = 25;
#Suma
print("La suma es: ", a + b);
#Resta
print("La resta es: ", b - a);
#Multipliacacion
print("La Multiplicacion es: ", a * b);
#Division
print("La division es: ", b / a);
#Modulo de la Division
print("El Modulo de la Division es: ", b % a);
#Redondeo Exacto
print("3 dividido en 2 es Redondeado a: ", 3//2);
#Orden de opraciones
print("Primero se ejecutara lo de los parentesis: ", 45 + (3 * 2))

"""---------------------------------------------------------------------------------"""
num1 = input("Digite un numero: " );
print(type(num1));
print(type(int(num1)));


"""-----------------------------------------------------------------------------------"""
numA = input("Digite El numero 1: ");
numB = input("Digite el numero 2: ");
division = float(numA) / float(numB);
moduloResto = float(numA) % float(numB);
print(numA, " Dividido por ", numB, " es ingual a: ", division);
print("El modulo de: ", numA ," Dividido por: ", numB ," Es: ", moduloResto);

"""------------------------------------------------------------------------------------"""
numC = float(input("Digite un numero: "));
print("El tipo de dato es: ", type(numC));


