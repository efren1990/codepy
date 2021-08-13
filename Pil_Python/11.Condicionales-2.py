#---------------------------------------------------#
#Estructuras de Control de flujo(Condicional If-else)
#---------------------------------------------------#
print("Verificacion de Acceso");
#Pido y almaceno edad usuario
edadUsuario = int(input("Intruduce tu edad: "));
# Valido usuario con if--elif(else if)--else
if edadUsuario < 18:
	print("No puedes Pasar");
elif edadUsuario > 100:
	print("Edad Incorrecta");
elif edadUsuario > 80:
	print("Muy Viejo, No puede Pasar");
else:
	print("Puedes Pasar :)");

print("El programa ha finalizado");


