En este ejercicio voy a desarrollar un programa sencillo utilizando la herencia definire una clase genérica llamada Persona para los nombres y apellidos y luego extenderemos esta funcionalidad creando clases específicas para profesores y alumnos

---

Primero creamos la superclase Persona con los parametros nombre y apellidos asi como el metodo constructor y el metodo dameDatos que nos devolvera el nombre y apellidos

```
class Persona():
	def __init__(self,nombre,apellidos):
		self.nombre = nombre
		self.apellidos = apellidos
	def dameDatos(self):
		return self.nombre+self.apellidos	
```
Ahora creamos la subclase Profesor que heredara de la superclase Persona los parametros nombre y apellidos y el metodo constructor y el metodo dameDatos que nos devolvera el nombre y apellidos

```
class Profesor(Persona):
	def __init__(self,nombre,apellidos):
		super().__init__(nombre,apellidos)
	def dameDatos(self):
		return "Profesor: "+self.nombre+" "+self.apellidos	
```

Ahora creamos la subclase Alumno que heredara de la superclase Persona los parametros nombre y apellidos y el metodo constructor y el metodo dameDatos que nos devolvera el nombre y apellidos

```
class Alumno(Persona):
	def __init__(self,nombre,apellidos):
		super().__init__(nombre,apellidos)
	def dameDatos(self):
		return "Alumno: "+self.nombre+" "+self.apellidos	
```

Ahora creamos un objeto profesor1 de la subclase Profesor y le pasamos los parametros nombre y apellidos

```
profesor1 = Profesor("Andres","Lopez")
print(profesor1.dameDatos())
```

Ahora creamos un objeto alumno1 de la subclase Alumno y le pasamos los parametros nombre y apellidos

```
alumno1 = Alumno("Azul","Salfate")
print(alumno1.dameDatos())
```

---

En conclusión, este ejercicio aunque tanto el profesor como el alumno comparten la misma base heredada de Persona el método dameDatos se muestra de manera diferente según la clase y lo que invoque 