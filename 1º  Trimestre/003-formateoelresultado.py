import os
import time

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
    ruta = os.path.join(carpeta, elemento)

    print("Nombre: (elemento)")
    print("Tamaño: {os.path.getsize(ruta)} bytes")
    print("Última modificación: {time.ctime(os.path.getmtime(ruta))}\n")

