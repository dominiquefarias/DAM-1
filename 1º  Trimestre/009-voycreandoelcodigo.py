'''
Aplicación de gestión de productos
Esta aplicación gestiona productos
'''
# Defino clases y funciones

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0

# Creamos variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos")
# Metemos al usuario en un bucle infinito
while True:
    # Le mostraremos al usuario las opciones que tiene
    print("Selecciona una opción:")
    print("1.-Crear un nuevo producto")
    print("2.-Listar productos")
    print("3.-Actualizar productos")
    print("4.-Eliminar productos")
    opcion = int(input("Escoge tu opción:"))
    # En función de la opción que coja el usuario
    if opcion == 1:
        # O bien creamos un nuevo producto
        print("Creamos un nuevo producto")
        producto1 = Producto()
        producto1.nombre = input("Introduce el nombre del producto:")
        producto1.precio = input("Introduce el precio del producto:")
        productos.append(Producto) 
    elif opcion == 2:
        # O bien listamos los productos
        print("Vamos a listar los productos")
    elif opcion == 3:
        # O bien actualizamos los productos
        print("Vamos a actualizar los productos")
    elif opcion == 4:
        # O bien eliminamos los productos
        print("Hemos eliminado los productos")
    # Y volvemos a repetir

