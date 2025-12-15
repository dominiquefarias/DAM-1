# CRUD
# Create
# Read
# Update
# Delete

print("programa de gestion de clientes")

print("seleccina una opccion: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

clientes = []

while True:
    opcion = input("Escoge una opción: ")
    opcion = int(opcion)

    if opcion == 1:
        print("vamos a incertar un cliente")
        nuevocliente = input("Introduce el nombre del cliente: ")
        cliente.append(nuevocliente)
    elif opcion == 2:
        print("Vamos a ver los clientes")
        print(clientes)
    elif opcion == 3:
        ("Vamos a actualizar un cliente")
    elif opcion == 3:
        ("Vamos a eliminar un cliente")
    else:
        break

