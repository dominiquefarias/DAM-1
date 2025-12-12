import pickle
class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
        
clientes = []

clientes.append(Cliente("Jose vicente","info@Domasa.com"))
clientes.append(Cliente("Juan","asios@Domasa.com"))

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close
