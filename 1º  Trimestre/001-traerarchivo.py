archivo = open("Este es un primer articulo.txt","r")

lineas = archivo.readlines()

for linea in lineas:
    print(linea)
