class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
    def setNombreCompleto(self,nuevonombre):
        set.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email
        
print("Gestor de clientes")
print("Selecciona una opcion:")
print("1.- Instertar nuevo cliente")
print("2.- Obtener listado de clientes")
opcion = int(input("Indica tu opcion: "))

if opcion == 1:
    print("Voy a insertar un cliente")
elif opcion == 2:
    print("Saco el listado de clientes")
