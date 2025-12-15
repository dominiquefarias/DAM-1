import os

carpeta = input("Indica una carpeta: ")
 
for directorio,carpetas,archivos in os.walk(carpeta):
    print(directorio)
    print(carpeta)
    print(archivos)
