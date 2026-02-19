En este ejercicio creo una lista que contenga todos los números del 1 al 9 utilizo un bucle infinito para generar listas aleatorias continuamente.
---

Primero importo la libreria random
```
import random
```

Ahora creo el patron de numeros
```
patron = {1,2,3,4,5,6,7,8,9}
```

Ahora creo un bucle infinito para generar numeros aleatorios
```
while True:
	lista = []
	for i in range(1,10):
		lista.append(random.radint(1,9))
	conjunto = set(lista)
```

Ahora comparamos el conjunto con el patron y si son iguales imprimimos el conjunto y la lista y eliminamos un numero aleatorio
```
	if conjunto == patron:
		print("El conjunto es correcto")
		print(conjunto)
		print(lista)
		indice = random.randint(1,9)
		lista[indice] = "_"
		print(lista)
		break 
```

---

En conclusión este ejercicio ayuda a entender la eficiencia de los conjuntos para comparar datos al convertir la lista generada aleatoriamente en un conjunto, eliminamos automáticamente los duplicados y nos despreocupamos del orden de los elementos esto nos permite validar si la lista contiene exactamente los números del 1 al 9 en una sola línea de código simplificando enormemente una lógica que con bucles tradicionales sería mucho más compleja