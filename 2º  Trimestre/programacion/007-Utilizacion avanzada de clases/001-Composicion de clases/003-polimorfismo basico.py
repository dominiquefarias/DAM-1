class Profesor():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
	def dameDatos(self):
		return self.nombre+self.apellidos	
		
class Alumno():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
	def dameDatos(self):
		return self.nombre+self.apellidos
		
profesor1 = Profesor("Juan","Garcia","juan@email.com")
print(profesor1.dameDatos())

alumno1 = Alumno("Dominique","Farias","domi@email.com")
print(alumno1.dameDatos())

