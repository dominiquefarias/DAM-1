
En este ejercicio creare un "juego" basico con una base de clases sobre una nave espacial interactiva. Combinare la estructura HTML para cargar las imágenes (nave y rocas) utilizandoJavaScript para darle vida. Tambien instanciare objetos en este caso las rocasy a capturar la entrada del usuario en este caso con las teclas W, A, S, D para actualizar la posición de la nave en cuanto el usuario toque esas teclas

---

Primero comienzo abriendo el documento html

```
<!doctype html>
<html>
```

Luego abro el head y como le pongo el estilo a los objetos rave y roca

```
<head>
    <style>
        #nave {
            position: absolute;
            width: 50px;
        }

        .roca {
            width: 50px;
        }
    </style>
</head>
```

Luego abro el body y cargo la imagen de la nave


```
<body>
    <img src="nave.png" id="nave">
</body>
```

Luego abro el script y declaro las clases 

primero declaro la clase madre con sus propiedades

```
<script>

    class Entidad {	
        constructor(x, y, a, v) {
            this.posx = x;
            this.posy = y;
            this.angulo = a;
            this.velocidad = v;
        }
    }
```

luego declaro las clases concretas para la bala, jugador y roca

```

    class Bala extends Entidad {				
        constructor(x, y, a, v) {
            super(x, y, a, v);							
        }
    }
    class Jugador extends Entidad {			
        constructor(x, y, a, v) {
            super(x, y, a, v);							
        }
    }
    class Roca extends Entidad {				
        constructor(x, y, a, e, v) {
            super(x, y, a, v);																	
            this.escala = e;								
        }
    }
```
Ahora creo las rocas poniendo cuantas rocas quiero y tambien creando un bucle para crearlas
```
    let numero_rocas = 100;													
    let rocas = [];																
    for (let i = 0; i < numero_rocas; i++) {							
        let posx_aleatoria = Math.random() * anchopagina
        let posy_aleatoria = Math.random() * altopagina
        let angulo_aleatorio = Math.random() * 360
        let escala_aleatoria = Math.random() * 1
        rocas.push(new Roca(
            posx_aleatoria,
            posy_aleatoria,
            angulo_aleatorio,
            escala_aleatoria,
            0
        ))							
    }
```

Ahora creo9 la instancia del jugador
```

    let nave = document.querySelector("#nave");
    let InstanciaJugador = new Jugador(
        Math.random() * anchopagina,
        Math.random() * altopagina,
        0, 0)		 																// 
    nave.style.left = InstanciaJugador.posx + "px";
    nave.style.top = InstanciaJugador.posy + "px";
```

Ahora creo el movimiento del jugador determinado por las teclas d, w, a, s para subir bajar ir a un lado o otro

```
    document.onkeydown = function (tecla) {		
        switch (tecla.keyCode) {
            case 87:			
                InstanciaJugador.posy -= 5;	
                break;
            case 83:			
                InstanciaJugador.posy += 5;	
                break;
            case 65:			
                InstanciaJugador.posx -= 5;	
                break;
            case 68:			
                InstanciaJugador.posx += 5;	
                break;
        }
        nave.style.left = InstanciaJugador.posx + "px";
        nave.style.top = InstanciaJugador.posy + "px";
    }
```

Ahora dibujo las rocas en la pantalla

```
    // Voy a dibujar rocas
    for (let i = 0; i < numero_rocas; i++) {
        let nueva_roca = document.createElement("img"); 
        nueva_roca.classList.add("roca")								
        nueva_roca.src = "roca.png"											
        nueva_roca.style.position = "absolute"					
        nueva_roca.style.left = rocas[i].posx + "px"					
        nueva_roca.style.top = rocas[i].posy + "px"						
        nueva_roca.style.transform = "rotate(" + rocas[i].angulo + "deg)  scale(" + rocas[i].escala + ")"	
        document.querySelector("body").appendChild(nueva_roca)
    }
```
y por ultimo cierro el documento

```
</script>

</html>
```

---

Como conclusion he logrado construir un "juego" funcional que conecta JavaScript con HTML, Tambien he aprendido a generar contenido dinámico creando instancias de rocas aleatorias, ademas he aprendido a controlar el flujo del programa mediante eventos de usuario, este sistema de posicionamiento absoluto modificado por código 