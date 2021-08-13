#---------------------------------------------------#
#POO->Programacion Orientada a Objetos
#---------------------------------------------------#
#Cosntruccion de una clase
	# class NombreClase():
#HERENCIA----------------->
"""
Cuando una clase hereda de otra ya sea metodos o propiedades

►Para que Sirve la Herencia?->
	Para reutilizar codigo en caso de crear objetos similares
"""
#USO DE LA FUNCION SUPER
#Clase Persona-------------------------------------------------------------------------->
class Persona():
	#Constructor
	def __init__(self, nombre, edad, lugResidencia):
		# PAso de Datos 
		self.nomPer = nombre;
		self.edadPer = edad;
		self.lugPer = lugResidencia;
	#Metodo->Descripcion de la persona
	def descripcion(self):
		print("Nombre: ",self.nomPer,"\nEdad: ",self.edadPer,"\nResidencia: ",self.lugPer);

# Fin Clase------------------------------------------------------------------------------->

#Clase Empleado--------------------------------------------------------------------------->
#Herencia->
class Empleado(Persona):
	#Constructor->
	def __init__(self, salario, antiguedad, nomEmpleado, edadEmpleado, resiEmpleado):
		"""super()->Hereda el constructor de la clase persona y permite pasar parametros en la
		 clase empleado"""
		super().__init__(nomEmpleado, edadEmpleado, resiEmpleado);
		self.salEmp = salario;
		self.antEmp = antiguedad;
	#Metodo Reescrito de la clase padre con super()->
	def descripcion(self):
		#Llamamos el metodo de la clase padre
		super().descripcion();
		# Agregamos al Metodo sobreescribiendo el de la clase padre en la clase actual
		print("Salario: ",self.salEmp,"\nAntiguedad: ",self.antEmp)


# Fin Clase------------------------------------------------------------------------------->

#Clase Persona-------------------------------------------------------------------------->
# Fin Clase------------------------------------------------------------------------------->

#Cosntruccion de Objetos----------------------------------------------------------------->
#Objeto Persona
objPersona = Persona("Carolina", 25, "Colombia");
objPersona.descripcion();
#Objeto Persona quien hereda de persona y permite pasar parametros para el constructor de la clase padre
objEmpleado = Empleado(820000, 5, "Adriana", 28, "Venezuela");
objEmpleado.descripcion();

# Funcion isinstance(NombreObjeto, Clase)->informa si un objeto es instancia de una clase determinada
print(isinstance(objPersona, Persona));
print(isinstance(objEmpleado, Persona));
print(isinstance(objPersona, Empleado));