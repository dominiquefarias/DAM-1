En este ejercicio creare una clase "principal" llamada Persona creare clases como Alumno y AlumnoPresencial el objetivo es ver cómo la última clase de la cadena recibe todos los datos nombre, email, etc. de la primera

---

Primero creo la clase Persona que tiene los atributos nombre, apellidos, email y direccion. y el metodo dameDatos que devuelve el nombre y los apellidos

```
class Persona():
    def __init__(self, nombre, apellidos, email, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        
    def dameDatos(self):
        return self.nombre + " " + self.apellidos   
```
Ahora creo la clase Profesor que hereda los atributos de Persona
```
class Profesor(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)
```
Ahora creo la clase Alumno que hereda los atributos de Persona
```
class Alumno(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)
```
Ahora creo la clase AlumnoOnline que hereda los atributos de Alumno
```
class AlumnoOnline(Alumno):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)
```
Ahora creo la clase AlumnoPresencial que hereda los atributos de Alumno
```
class AlumnoPresencial(Alumno):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)
```
Ahora creo un objeto profesor1 de la clase Profesor
```
profesor1 = Profesor("Juan", "Garcia", "juan@jocarsa.com", "Dirección")
print(profesor1.dameDatos())
```
Ahora creo un objeto alumno1 de la clase AlumnoPresencial
```
alumno1 = AlumnoPresencial("Jose Vicente", "Carratala", "info@jocarsa.com", "Dirección")
print(alumno1.dameDatos())
```
---

En conclusión he mostrado cómo la información fluye a través de varios niveles de clases aunque mi objeto alumno1 pertenece a la clase AlumnoPresencial, he visto que tiene acceso a todos los datos definidos en la clase Persona como el nombre y el email esto demuestra que gracias a la herencia de las clases no necesito repetir código en cada nueva clase que creo sino que puedo aprovechar todo lo que ya programé en los niveles superiores