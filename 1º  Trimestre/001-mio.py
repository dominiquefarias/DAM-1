class Cliente:
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}"

print("Programa de Gestión de Clientes")

clientes = []

while True:
    print("\nSelecciona una opción: ")
    print("1.- Insertar un cliente")
    print("2.- Listar clientes")
    print("3.- Actualizar cliente")
    print("4.- Eliminar cliente")
    print("5.- Salir")

    try:
        opcion = int(input("Escoge una opción: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    if opcion == 1:
        print("Vamos a insertar un cliente:")
        nuevocliente = Cliente()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la dirección del cliente: ")
        clientes.append(nuevocliente)
        print("Cliente agregado correctamente.")

    elif opcion == 2:
        print("Lista de clientes:")
        if not clientes:
            print("No hay clientes registrados.")
        else:
            for idx, cliente in enumerate(clientes):
                print(f"{idx + 1}. {cliente}")

    elif opcion == 3:
        if not clientes:
            print("No hay clientes para actualizar.")
            continue
        try:
            index = int(input("Introduce el número del cliente que deseas actualizar: ")) - 1
            if 0 <= index < len(clientes):
                cliente = clientes[index]
                print(f"Actualizando cliente: {cliente}")
                cliente.nombre = input("Nuevo nombre (dejar en blanco para mantener): ") or cliente.nombre
                cliente.email = input("Nuevo email (dejar en blanco para mantener): ") or cliente.email
                cliente.direccion = input("Nueva dirección (dejar en blanco para mantener): ") or cliente.direccion
                print("Cliente actualizado.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Entrada no válida.")

    elif opcion == 4:
        if not clientes:
            print("No hay clientes para eliminar.")
            continue
        try:
            index = int(input("Introduce el número del cliente que deseas eliminar: ")) - 1
            if 0 <= index < len(clientes):
                eliminado = clientes.pop(index)
                print(f"Cliente eliminado: {eliminado.nombre}")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Entrada no válida.")

    elif opcion == 5:
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

