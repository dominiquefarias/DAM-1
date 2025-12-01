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
clientes = []
        
print("Gestor de clientes")
while True:
    print("Selecciona una opcion:")
    print("1.- Instertar nuevo cliente")
    print("2.- Obtener listado de clientes")
    opcion = int(input("Indica tu opcion: "))

    if opcion == 1:
        print("Voy a insertar un cliente")
        nuevocliente = Cliente()
        nombrecliente = input("Introduce nombre cliente: ")
        nuevocliente.setNombreCompleto(nombrecliente)
        emailcliente = input("Introduce el email del cliente: ")
        nuevoliente.setemail(emailcliente)
        clientes.append(nuevocliente)
    elif opcion == 2:
        print("Saco el listado de clientes")
        for cliente in clientes:
            print("------------------")
            print("Nombre:", cliente.getNombreCompleto())
            print("Email:", cliente.getEmail())
            print("------------------")
            
