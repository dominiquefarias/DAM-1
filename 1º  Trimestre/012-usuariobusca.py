archivo = open("mapa.txt","r")
busca = input("Introduce el termino a buscar: ")

lineas = archivo.readlines()

for linea in lineas:
    if busca in linea:
        print("######################################")
        print("Encontrado!",linea)


