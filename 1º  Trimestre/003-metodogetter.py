class Gato():
    def __init__(self):
        self.color = ""
        
    def maulla(self):
        return "miau"
        
    def setColor(self,nuevocolor):
        self.color = nuevocolor
    
    def getColor(self):
        return self.color
        
gato1 = Gato()
gato1.color = "naranja"

gato1.setColor("naranja")

print(gato1.color)

print(gato1.getColor())
