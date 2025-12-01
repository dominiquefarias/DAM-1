import zipfile

origen = "trydd.html"

destino = "comprimido.zip"

archivo = zipfile.ZipFile(destino,"w")
archivo.write(origen)
