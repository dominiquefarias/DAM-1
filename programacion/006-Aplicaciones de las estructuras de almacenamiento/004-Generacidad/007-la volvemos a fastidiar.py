numeros = [1,2,"3",4,"cinco","patata"]

print(numeros)

numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]

def calculaDoble():
	for numero in numeros:
		try:
			numero = int(numero) # Primero inetento a Convertir a entero
			print(numero*2)
		except:
		# Intenta buscar el valor en la lista de numeros
			for i in range(0,len(numeros_etiquetas)):
			if numeros == numeros_etiquetas[i]:
			print(i*2)
		
calculaDoble()
