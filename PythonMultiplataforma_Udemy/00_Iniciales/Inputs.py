""""
-----------------Ingreso de Datos-----------------------
variable = input("Mensaje: ")
Se debe usar input dentro de la variable
los datos recibidos en un input son automaticamente strings
"""
#Captar dato de usuario
login = input("Ingresa tu usuario: ");
password = input("Ingresa tu contraseña: ");
edad = input("Ingresa tu Edad: ");

#Imprimir los datos de usuario
print("Su Usuario es: " + login);
print("Su usuario es: ", login);
print("Su contraseña es: ", password);
d = int(edad);
print(type(d));
print("Su edad es: " + edad);

#Imprimir Datos con marcadores
print("El Usuario Escrito es: %s, La contraseña escrita es: %s" %(login, password));
