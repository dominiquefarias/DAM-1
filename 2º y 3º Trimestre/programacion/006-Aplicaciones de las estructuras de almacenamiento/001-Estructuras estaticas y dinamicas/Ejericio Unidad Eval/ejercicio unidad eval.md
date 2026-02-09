'''
Crea una lista de elementos musicales: Comienza creando una lista llamada lista_musical que contenga al menos tres elementos, como nombres de artistas o géneros musicales.

Añade un nuevo elemento a la lista: Utiliza el método append() para añadir un nuevo género musical a tu lista.

Recorre y muestra los elementos de la lista: Recorre la lista utilizando un bucle for y muestra cada uno de los elementos en pantalla.

Modifica un elemento específico: Sobrescribe el segundo elemento de la lista con otro género musical que te guste.

Elimina el último elemento de la lista: Usa el método pop() para eliminar el último elemento añadido a la lista.
'''
En este ejercicio se me pide que utilice listas para agrupar varios datos y luego mediante ```append()``` añadire un nuevo elemento a la lista ya que este sirve para añadir un elemento al final de la lista. Luego con un bucle ```for``` para recorrer la lista y mostrar cada uno de los elementos en pantalla, luego modifico directamente un elemento de la lista y lo sobreescribo, y borro el ultimo elemento de la lista utilizando ```pop()``` para demostrar la modificación

---

Primero creo la lista de elementos musicales con generos de musica en este caso me pidieron al menos tres

```
lista_musical = ["Rock", "Pop", "Reggaeton"]
```

Despues me piden añadir un nuevo elemento a la lista utilizando append()

```
lista_musical.append("Indie")
```

Y ahora recorro y muestro los elementos de la lista con un bucle for

```
print("Lista musical")
for genero in lista_musical:
    print(genero)
```

Ahora modifico un elemento en la lista y lo sobreescribo

```
lista_musical[1] = "Trap"
```

Ahora se me pide que elimine el último elemento de la lista usando pop()

```
lista_musical.pop()
```

Ahora hago un print para mostrar que lo anterior se cumple

```
print("Lista final")
for genero in lista_musical:
    print(genero)
```
---

Como conclusion en este ejercicio he practicado la funcion y la manipulacion de las listas tambien he visto la facilidad de como se puedo añadir cosas nuevas con ```append()``` y recorrerlas fácilmente con un ```for``` para ver qué contiene la lista y modificar o borrar datos con ```pop()``` facilmente 