import os
import zipfile

origen = "archivos"

destino = "archivos.zip"

archivo = zipfile.ZipFile(destino,"w", compression=zipfile.ZIP_DEFLATED)
for directorio, carpeta, archivos in os.walk(origen):
    for archivo in archivos:
        rutaarchivo = os.path.join(directorio, archivo)
        rutarelativa = os.path.realpath(rutaarchivo, origen)
        archivozip.write(rutaarchivo, rutarelativa)
archivozip.close()
