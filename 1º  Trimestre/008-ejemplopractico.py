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
