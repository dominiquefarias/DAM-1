import re

nombre = "Jose Vicente"

def validar_direccion(direccion):
    patron = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'
    if re.match(patron, direccion):
        return True
    else:
        return False

# Prueba la función con algunas direcciones
print(validar_direccion("Calle Mayor 10 46001"))  # Debería imprimir True
print(validar_direccion("Calle Mayor"))         # Debería imprimir False

with open("direcciones.csv", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    partes = linea.split(",")
    direccion = partes[2]  # Suponemos que la dirección está en la tercera columna
    if validar_direccion(direccion):
        print(f"Dirección válida: {direccion}")
    else:
        print(f"Dirección inválida: {direccion}")