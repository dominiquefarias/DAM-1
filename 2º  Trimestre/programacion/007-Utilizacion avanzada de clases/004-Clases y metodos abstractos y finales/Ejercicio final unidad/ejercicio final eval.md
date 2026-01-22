
En este ejercicio el objetivo es implementar un reloj digital utilizando una estructura de clases heredada controlar un personaje en pantalla mediante las teclas W, A, S, D

---

Primero comienzo definiendo la estructura html y el estilo css utilizo fuentes para el reloj y posicionamiento absoluto para permitir el movimiento libre del personaje en el proyecto

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            background: #1a1a1a;
            color: #fff;
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .entidad {
            position: absolute;
            transition: all 0.1s;
            font-size: 2rem;
            font-weight: bold;
        }
        #personaje {
            width: 40px;
            height: 40px;
            background: plum;
            border-radius: 50%;
            box-shadow: 0 0 10px plum;
            z-index: 10;
        }
    </style>
</head>

```

Ahora implemento javascript para crear la clase abstracta de ser la cual nos sirve de base para los digitos del reloj y el personaje controlable en el proyecto esta clase maneja las coordenadas  y el elemento asociado en este caso seria el div que se crea en el html

```
    <script>
        // Clase Abstracta Ser
        class Ser {
            constructor(x, y) {
                this.x = x;
                this.y = y;
                this.elemento = document.createElement("div");
                this.elemento.classList.add("entidad");
                document.body.appendChild(this.elemento);
                this.actualizarPosicion();
            }

            actualizarPosicion() {
                this.elemento.style.left = this.x + "px";
                this.elemento.style.top = this.y + "px";
            }
        }

```

Ahora creo la clase llamada digito que heredara de la clase Ser esta clase representa las Horas, Minutos y Segundos y utilizo trigonometría para posicionar estos dígitos en un círculo alrededor del centro de la pantalla 

```
        class Digito extends Ser {
            constructor(tipo, angulo) {
                let radio = 150;
                let centroX = window.innerWidth / 2;
                let centroY = window.innerHeight / 2;
                let x = centroX + radio * Math.cos(angulo);
                let y = centroY + radio * Math.sin(angulo);
                
                super(x, y);
                this.tipo = tipo;
                this.actualizarContenido();
            }

            actualizarContenido() {
                let fecha = new Date();
                let valor = 0;
                if(this.tipo === 'horas') valor = fecha.getHours();
                if(this.tipo === 'minutos') valor = fecha.getMinutes();
                if(this.tipo === 'segundos') valor = fecha.getSeconds();
                
                this.elemento.textContent = valor < 10 ? "0" + valor : valor;
            }
        }

```

Ahora creo la clase personaje la cual heredara de la clase Ser y añado un tipo visual y métodos para que puedamoverse

```
        class Personaje extends Ser {
            constructor() {
                super(window.innerWidth / 2, window.innerHeight / 2);
                this.elemento.id = "personaje";
            }
            
            mover(dx, dy) {
                this.x += dx;
                this.y += dy;
                this.actualizarPosicion();
            }
        }

```

Por ultimo instancio los objetos y creo los eventos para esto utilizo para actualizar el reloj cada segundo y un EventListener para capturar las teclas W, A, S, D y poder mover el personaje

```
        let horas = new Digito('horas', 0);
        let minutos = new Digito('minutos', (2 * Math.PI) / 3);
        let segundos = new Digito('segundos', (4 * Math.PI) / 3);
        
        let jugador = new Personaje();

        setInterval(() => {
            horas.actualizarContenido();
            minutos.actualizarContenido();
            segundos.actualizarContenido();
        }, 1000);

        document.addEventListener("keydown", function(e) {
            let velocidad = 10;
            if (e.key === 'w' || e.key === 'W') jugador.mover(0, -velocidad);
            if (e.key === 's' || e.key === 'S') jugador.mover(0, velocidad);
            if (e.key === 'a' || e.key === 'A') jugador.mover(-velocidad, 0);
            if (e.key === 'd' || e.key === 'D') jugador.mover(velocidad, 0);
        });
    </script>
</body>
</html>

```

---

En conclusión este ejercicio integra la estructura de clases para gestionar entidades en el proyecto el uso de matemáticas en este proyectopara el diseño visual (esta vez trigonometría para la distribución circular) y la interactividad en tiempo real mediante eventos de teclado cumpliendo con todos los requisitos de implementación de una interfaz 

