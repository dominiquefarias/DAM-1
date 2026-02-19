En este ejercicio partiremos de una lista que mezcla números reales con texto creare una función encargada de recorrerla y calcular el doble de cada valor dado que no todos los elementos pueden multiplicarse tambien utilizare un try except para detectar qué valores son válidos y cuáles no para que el programa continúe su ejecución sin pararse por errores

---

Primero se define una lista de números que incluye enteros y cadenas de texto

```
numeros = [1,4,"0",7,"seis"]
```

Luego se define una función que recorre la lista e intenta convertir cada número a entero para calcular el doble de cada número. Si no es posible, se muestra un mensaje de error.

```
print(numeros)

def calculaDoble():
	for numero in numeros:
		try:
			numero = int(numero)
			print(numero*2)
		except:
			print("(no valido)")
```

Finalmente se llamo a la función para que se ejecute.

```
calculaDoble()
```

---

En conclusión este ejercicio muestra la importancia de la gestión de errores he visto que al utilizar el bloque try except logro que el programa no se detenga abruptamente con un error fatal al encontrar un dato incompatible como 'seis' el programa captura el fallo informa al usuario y continúa procesando el resto de la lista sin interrupciones