class Persona():
	def __init__(self,nombre,apellidos):
		self.nombre = nombre
		self.apellidos = apellidos
	def dameDatos(self):
		return self.nombre+self.apellidos	

class Profesor(Persona):
	def __init__(self,nombre,apellidos):
		super().__init__(nombre,apellidos
	def dameDatos(self):
		return "Profesor: "+self.nombre+" "+self.apellidos	
		
class Alumno(Persona):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre,apellidos,email,direccion)
	def dameDatos(self):
		return "Alumno: "+self.nombre+" "+self.apellidos	
		
profesor1 = Profesor("Juan","Garcia")
print(profesor1.dameDatos())

alumno1 = Alumno("Dominique","Farias")
print(alumno1.dameDatos())

