'''
Crear la estructura de la agenda: Miguel necesita un sistema que almacene información sobre los contactos, incluyendo nombre, apellidos, email y teléfono.
Añadir contactos a la agenda: Debe permitirle agregar nuevos contactos fácilmente.
Guardar la agenda en un archivo: Para que pueda acceder a ella desde cualquier lugar, necesita guardar la agenda en un archivo binario.
Leer la agenda del archivo: Cuando vuelva a casa, debe poder leer y visualizar su agenda.
'''
import pickle

agenda = []

while True:
	nombre = input("Dime tu nombre: ")
	apellidos = input("Dime tus apellidos: ")
	email = input("Dime tu email: ")
	telefono = input("Dime tu telefono: ")
		
	agenda.append([nombre,apellidos,email,telefono])
	print(agenda)
	archivo = open("agenda.bin","wb")
	pickle.dump(agenda,archivo)
	archivo.close