numeros = [1,4,"0",7,"seis"]

print(numeros)

def calculaDoble():
	for numero in numeros:
		try:
			numero = int(numero) # Convierto a entero
			print(numero*2)
		except:
			print("(no valido)")
		
calculaDoble()
