archivo = open("Este es un primer articulo","r")

lineas = archivo.readlines()

for linea in lineas:
    prin(linea)
