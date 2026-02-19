En este ejercicio el objetivo es modelar la entidad Jugador de manera que cada usuario pueda tener su propia información personalizada creare dos instancias Juan y Ana y mostrare como a pesar de venir de la misma clase, cada uno evoluciona de forma distinta mientras Juan llena su lista de videojuegos jugados Ana actualiza sus preferencias musicales demostrando la independencia de los objetos en memoria

---

Primero comienzo creando una clase jugador que tenga los atributos nombre, edad, juegos_jugados y musica_favorita
```
class Jugador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.juegos_jugados = []       
        self.musica_favorita = ""   
```   

Luego creo dos instancias de la clase jugador
```
juan = Jugador("Juan", 20)
ana = Jugador("Ana", 22)
```   

Finalmente creo un programa que muestre el estado final de los jugadores
```
print("Agregando juegos")
juan.agregar_juego("Minecraft")
juan.agregar_juego("League of Legends")
juan.agregar_juego("FIFA 24")

print("Musica de ana")
ana.seleccionar_musica("Pop Rock")

print("Estado final")
print("Juan - Juegos:" ,juan.juegos_jugados)
print("Ana - Música:" ,ana.musica_favorita)
```   
---

En conclusión he comprobado que aunque juan y ana provienen de la misma clase Jugador son objetos totalmente independientes en la memoria al modificar la lista de jueegos de Juan, la de Ana permanece intacta y viceversa con la música esto confirma que cada objeto encapsula su propio estado permitiendo gestionar múltiples usuarios simultáneamente sin que sus datos se mezcle