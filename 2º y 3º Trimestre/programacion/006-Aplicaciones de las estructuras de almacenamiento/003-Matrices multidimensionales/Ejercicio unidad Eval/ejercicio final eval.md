En este ejercicio se me pide crear una agenda de contactos donde utilizaré un bucle para pedir continuamente el nombre, apellidos, email y teléfono de nuevas personas luego para guardar los datos utilizo el modulo pickle para guardarlo en un archivo binario

---

primero importo pickle

```
import pickle
```
Luego creo una lista vacia
```
agenda = []
```
Luego creo un bucle infinito donde pido los datos del contacto que serian nombre, apellidos, email y telefono
```
while True:
	nombre = input("Dime tu nombre: ")
	apellidos = input("Dime tus apellidos: ")
	email = input("Dime tu email: ")
	telefono = input("Dime tu telefono: ")
```
Luego de que el usuario inserta los datos, los agrega a la lista agenda y los guarda en un archivo binario el cual al finalizar de poner los datos los muestra por consola
```
	agenda.append([nombre,apellidos,email,telefono])
	print(agenda)
	archivo = open("agenda.bin","wb")
	pickle.dump(agenda,archivo)
	archivo.close
```

---

En conclusión con este ejercicio cree una agenda que guarda la información en mi ordenador he aprendido que con la libreria pickle se puede convertir la lista de contactos que tengo en la memoria del programa en un archivo real de esta forma cada vez que añado una persona nueva el archivo se actualiza y la información queda registrada permanentemente