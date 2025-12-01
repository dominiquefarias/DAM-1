import zipfile

origen = "trydd.html"

destino = "comprimido.zip"

archivo = zipfile.ZipFile(destino,"w", compression=zipfile.ZIP_DEFLATED)
archivo.write(origen)
