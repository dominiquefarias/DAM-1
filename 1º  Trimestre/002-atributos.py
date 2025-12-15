import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
    print(elemento)
    print(os.path.getsize(ruta))
    print(os.path.getmtime(ruta))
    
