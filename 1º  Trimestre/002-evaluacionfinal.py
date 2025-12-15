# Definición de la clase Cliente: sirve como molde para crear objetos cliente
class Cliente():
    # Constructor que se ejecuta automáticamente al crear un nuevo cliente
    def __init__(self, nombre, apellidos, email):
        # Guarda los datos en atributos del objeto
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
    

# Muestra el título del programa en pantalla
print("##### Gestión de clientes v0.1 #####")
print("###### Dominique Farías Oso ######")

# Crea una lista vacía para almacenar los objetos Cliente
clientes = []

# Bucle infinito: se repetirá hasta que el usuario decida salir manualmente
while True:
    # Muestra las opciones del menú principal
    print("Escoge una opción: ")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Actualizar a un cliente")
    print("4.-Eliminar un cliente")

    # Pide al usuario que escriba una opción (1, 2, 3 o 4)
    opcion = int(input("Escoge una opción: "))
    
    # --- OPCIÓN 1: Insertar un nuevo cliente ---
    if opcion == 1:
        # Pide los datos del cliente al usuario
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")

        # Crea un objeto Cliente con esos datos
        # y lo añade al final de la lista "clientes"
        clientes.append(Cliente(nombre, apellidos, email))

    # --- OPCIÓN 2: Listar todos los clientes ---
    elif opcion == 2:
        identificador = 0  # Se usa para mostrar el número de cliente (ID)
        for cliente in clientes:  # Recorre cada cliente de la lista
            print("Este es el cliente con ID", identificador)
            # Muestra los datos del cliente
            print(cliente.nombre, cliente.apellidos, cliente.email)
            identificador += 1  # Suma 1 al ID para el siguiente cliente

    # --- OPCIÓN 3: Actualizar un cliente existente ---
    elif opcion == 3:
        # Pide el ID del cliente que se desea modificar
        identificador = int(input("Introduce el id para modificar: "))
        # Pide los nuevos datos
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")

        # Actualiza los datos del cliente en la posición indicada
        clientes[identificador].nombre = nombre
        clientes[identificador].apellidos = apellidos
        clientes[identificador].email = email

    # --- OPCIÓN 4: Eliminar un cliente ---
    elif opcion == 4:
        # Pide el ID del cliente que se desea eliminar
        identificador = int(input("Introduce el id para eliminar: "))
        # Pide confirmación antes de eliminar
        confirmacion = input("¿Estas seguro? (S/N): ")
        clientes.pop(identificador)

        # Si el usuario confirma con "S" o "s", intenta eliminar de nuevo
        if confirmacion == "S" or confirmacion == "s":
            clientes.pop(identificador)
        # Si el usuario responde "N" o "n", se cancela la operación
        elif confirmacion == "N" or confirmacion == "n":
            print("Cancelado")
        # Si se escribe otra cosa, muestra mensaje de error
        else:
            print("opción no valida")

