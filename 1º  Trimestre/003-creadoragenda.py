while True:
    print("Dime lo que quieres hacer:")
    print("1.- Introduce el nuevo contacto")
    print("2.- Leer todos los contactos")
    opcion = input("Escoge tu opción:")
    opcion = int(opcion)
    if opcion == 1:
        nombre = input("Introduce el nombre de la persona: ")
        email = input("Introduce el email de la persona: ")
        archivo = open ("agenda.txt","a")
        archivo.write(nombre+","+email+"\n")
    elif opcion == 2:
        archivo = open("agenda.txt","r")
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
        archivo.close()
