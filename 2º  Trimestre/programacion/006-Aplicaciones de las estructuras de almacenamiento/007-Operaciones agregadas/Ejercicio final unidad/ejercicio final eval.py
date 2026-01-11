import random

patron = {1, 2, 3, 4, 5, 6, 7, 8, 9}

while True:
    lista = []
    for i in range(9):
        lista.append(random.randint(1, 9))

    conjunto = set(lista)

    if conjunto == patron:
        print("El conjunto es correcto")
        print(conjunto)
        print(lista)
        
        indice = random.randint(0, 8) 
        
        lista[indice] = "_"
        print(lista)
        
        break 


