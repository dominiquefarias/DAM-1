class Persona():
	def __init__(self,nombre,apellidos,email,direccion):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.direccion = direccion
	def dameDatos(self):
		return self.nombre+self.apellidos	

class Profesor(Persona):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre,apellidos,email,direccion)
		
class Alumno(Persona):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre,apellidos,email,direccion)
		
class AlumnoOnline(Alumno):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre,apellidos,email,direccion)
		
class AlumnoPresencial(Alumno):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre,apellidos,email,direccion)
		
profesor1 = Profesor("Juan","Garcia","juan@email.com","La calle de juan")
print(profesor1.dameDatos())

alumno1 = Alumno("Dominique","Farias","domi@email.com","La calle de domi")
print(alumno1.dameDatos())

