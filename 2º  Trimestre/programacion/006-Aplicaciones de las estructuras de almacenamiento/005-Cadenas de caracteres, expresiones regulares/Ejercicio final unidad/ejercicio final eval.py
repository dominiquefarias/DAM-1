nombre = "Jose Vicente"

import re

def validar_direccion(direccion):
    patron = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'
    if re.match(patron, direccion):
        return True
    else:
        return False

# Prueba la función con algunas direcciones
print(validar_direccion("Calle Mayor 10 46001"))  # Debería imprimir True
print(validar_direccion("Calle Mayor"))         # Debería imprimir False