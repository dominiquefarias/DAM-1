import os

carpeta = input("Indica una carpeta: ")
grande = 1024*1024*1024

mapa = open("mapa.txt","w")
 
for directorio,carpetas,archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        mapa.write(ruta+"\n")
        
mapa.close()
