En este ejercicio utilizare las listas y los diccionarios primero utilizaremos una lista para almacenar una colección ordenada de títulos de videojuegos y accederemos a ellos mediante su índice posteriormente daremos un paso más creando un diccionario para un personaje combinando claves y valores para organizar información variada como texto números e incluso listas anidadas dentro de la propia estructura

---

Primero defino una lista con tres videojuegos e imprimo la lista
```
videojuegos = ["The Legend of Zelda", "Super Mario Odyssey", "Hollow Knight"]
print("Lista de videojuegos:", videojuegos)
```
Ahora defino una variable que almacena el primer videojuego de la lista
```
primer_juego = videojuegos[0]
print("Primer videojuego:", primer_juego)
```
Ahora creo un diccionario con el personaje donde pongo el nombre, nivel, habilidades, objetos y la edad e imprimo la informacion
```
personaje = {
    "nombre": "Link",
    "nivel": 10,
    "habilidades": [
        "Espada Maestra", 
        "Escudo Hyliano"
    ],
    "objetos": [
        "Poción Roja", 
        "Mapa", 
        "Brújula"
    ],
    "edad": 17 
}

print("Información del personaje:", personaje)
```
Ahora defino una variable que almacena el nombre del personaje e imprimo el nombre
```
nombre = personaje["nombre"]
print("Nombre del personaje:", nombre)
```
Tambien defino una variable que almacena la primera habilidad del personaje y la imprimo
```
primera_habilidad = personaje["habilidades"][0]
print("Primera habilidad:", primera_habilidad)
```

---

En conclusión este ejercicio me ha servido para entender la distinción fundamental entre listas y diccionarios en he visto que las listas son ideales para secuencias ordenadas de elementos simples mientras que los diccionarios son la herramienta perfecta para definir objetos con múltiples atributos como una ficha de personaje además he comprobado que ambas estructuras son compatibles permitiéndonos anidar listas dentro de diccionarios para organizar datos complejos