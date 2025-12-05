class Profesor():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		
class Alumno():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		
profesor1 = Profesor("Juan","Garcia","juan@email.com")
print(profesor1)

alumno1 = Alumno("Dominique","Farias","domi@email.com")
print(alumno1)

