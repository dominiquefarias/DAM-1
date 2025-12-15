# CRUD
# Create
# Read
# Update
# Delete

class Cliente():
    def __int__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

print("programa de gestion de clientes")

print("selecciona una opcion: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

clientes = []

while True:
    opcion = input("Escoge una opción: ")
    opcion = int(opcion)

    if opcion == 1:
        print("vamos a insertar un cliente")
        nuevocliente = Cliente ()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        nuevocliente = input("Introduce el nombre del cliente: ")
        Cliente.append(nuevocliente)
    elif opcion == 2:
        print("Vamos a ver los clientes")
        print(clientes)
    elif opcion == 3:
        ("Vamos a actualizar un cliente")
    elif opcion == 3:
        ("Vamos a eliminar un cliente")
    else:
        break

