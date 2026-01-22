# Reporte de proyecto

## Estructura del proyecto

```
/Users/dominique/Desktop/Dam2.0/DAM-1/2º  Trimestre/Lenguaje de marcas
├── .DS_Store
├── 003-Manipulacion de documentos web
│   ├── 001-Lenguajes de script de cliente. Características y sintaxis básica. Estándares
│   │   ├── 041-varios parametros en la funcion.html
│   │   ├── 042-salida con return.html
│   │   ├── 043-creacion de una clase.html
│   │   ├── 044-instanciacion.html
│   │   ├── 045-propiedades.html
│   │   ├── 046-metodos.html
│   │   ├── 047-set y get.html
│   │   └── Ejercicio final unidad
│   │       ├── ejercicio final eval.html
│   │       └── ejercicio final eval.md
│   ├── 002-Seleccion y acceso a elementos
│   │   ├── 001- lectura.html
│   │   ├── 002-escribir.html
│   │   ├── 003-escribir html.html
│   │   ├── 004-microblog.html
│   │   ├── Archivo sin título
│   │   └── Ejercicio final unidad
│   │       ├── ejercicio final eval.html
│   │       └── ejercicio final eval.md
│   ├── 003-creacion y modificacion de elementos
│   │   ├── 001-crear elementos.html
│   │   ├── 002-crear varios botones.html
│   │   ├── 003-evento click.html
│   │   ├── 004-consumo.html
│   │   ├── 005-botones desde el json.html
│   │   ├── 006-recuperamos json tabla.html
│   │   ├── 007-creamos tabla.html
│   │   ├── 008-estilo en la tabla.html
│   │   ├── 009-creo interfaz base.html
│   │   ├── 010-me traigo elmenu.html
│   │   ├── 011-ahora m etraigo la tabla.html
│   │   ├── 012-consumo datos de la base de datos.html
│   │   ├── botones.json
│   │   └── tabla.json
│   ├── 004-Eliminacion de elemento
│   │   ├── 001-primero creo un elemento.html
│   │   ├── 002-eliminamos el elemento.html
│   │   ├── 003-creo tabla.html
│   │   ├── 004-click para eliminaar.html
│   │   ├── 005-retraso en ejecucion.html
│   │   ├── 006-bucle infinito.html
│   │   ├── 007-mini juego.html
│   │   └── 008-creador.html
│   ├── 005-Manipulacion de estilos
│   │   ├── 001-estilo en javascript.html
│   │   ├── 002-añadir clase.html
│   │   ├── 003-quitar clase.html
│   │   ├── 004-estilo condicional.html
│   │   ├── 005-variables en css.html
│   │   └── 006-funcion de calculo en css.html
│   └── 006-Publicacion web en github
│       ├── 001-Repaso de publicacion web.md
│       ├── 002-repaso de publicacion.md
│       ├── 003-publicacin de webs en GitHub Pages.md
│       ├── 004-portafolio.html
│       └── estilo.css
├── 004-Definicios de esquemas y vocabularios en lenguajes de marcas
│   ├── 001-Tecnologias para la definicion de documentos. Estructura y sintaxis
│   │   ├── 000-Introduccion.md
│   │   ├── 001-repaso xml.xml
│   │   ├── 002-debe de haber una etiqueta raiz.xml
│   │   ├── 003-case sensitive.xml
│   │   ├── 004-subetiquetas.xml
│   │   └── 005-varios telefonos.xml
│   ├── 002-creacion de descripciones de documentos
│   │   ├── 001-documento de referencia.xml
│   │   └── 002-esquema.xsd
│   └── 003-Asociacion de descripcion con documentos. Validacion
│       ├── 001-documento de referencia.xml
│       ├── 002-esquema.xsd
│       └── 003-validador.py
└── 005-Conversion y adaptacion de documentos para el intercambio de informacion
    ├── .DS_Store
    └── 001-Tecnologias de transformacion de documentos
        ├── 000-resumen.md
        ├── 001-formatos de documentos que conocemos.md
        ├── 002-pdf a texto.py
        ├── 003-texto a pdf.py
        ├── 004-excel a python.py
        ├── 005-desde python a excel.py
        └── Ejercicio final unidad
            ├── ejercicio final eval.md
            └── ejercicio final eval.py
```

## Código (intercalado)

# Lenguaje de marcas
## 003-Manipulacion de documentos web
### 001-Lenguajes de script de cliente. Características y sintaxis básica. Estándares
**041-varios parametros en la funcion.html**
```html
<script>
    function dihola(nombre,edad){
        document.write("Hola,"+nombre+"tienes, "+edad+"años, ¿Como estas?");
    }
    dihola("Jose Vicente",47)
</script>
```
**042-salida con return.html**
```html
<script>
    function dihola(nombre,edad){
        return "Hola,"+nombre+"tienes, "+edad+"años, ¿Como estas?";
    }
    document.write(dihola("Dominique",19));
</script>
```
**043-creacion de una clase.html**
```html
<script>
    class Gato()
</script>
```
**044-instanciacion.html**
```html
<script>
    class Gato {

    }
    var gato1 = new Gato();
    var gato2 = new Gato();
</script>
```
**045-propiedades.html**
```html
<script>
    class Gato {
        // Propiedades en constuctor
        constructor(){
            this.color = "";
            this.edad = 0;
            this.raza = undefined;
        }
    }
    var gato1 = new Gato();
    var gato2 = new Gato();
    console.log(gato1)
</script>
```
**046-metodos.html**
```html
<script>
    class Gato {
        // Propiedades en constuctor
        constructor(){
            this.color = "";
            this.edad = 0;
            this.raza = undefined;
        }
    }
    maulla(){
        return "Miau";
    }
    var gato1 = new Gato();
    var gato2 = new Gato();
    console.log(gato1)
    console.log(gato1.maulla())
</script>
```
**047-set y get.html**
```html
<script>
    class Gato {
        // Propiedades en constuctor
        constructor(){
            this.color = "";
            this.edad = 0;
            this.raza = undefined;
        }
    
    maulla(){
        return "Miau";
    }
    setColor(nuevocolor){this.color = nuevocolor;}
    getColor(return this.color;)
    }

    var gato1 = new Gato();
    var gato2 = new Gato();
    gato1.setColor("Naranja")
    document.write(gato1.getColor())
    console.log(gato1)
    console.log(gato1.maulla())
</script>
```
#### Ejercicio final unidad
**ejercicio final eval.html**
```html
<!doctype html>
<html lang="es">

<head>
    <meta charset="UTF-8">
</head>

<body>
    <script>
        let hoy = new Date();
        function diHola(nombre, edad) {
            return "Hola, " + nombre + " tienes " + edad + " años, ¿cómo estás?";
        }
        console.log("Hoy es: " + hoy.toLocaleDateString());
        console.log(diHola("Dominique", 19));
    </script>
</body>

</html>
```
**ejercicio final eval.md**
```markdown
En este ejercicio combino html con javascript sobre todo me centro en las fechas asi como tambien en las funciones parametrizadas el objetivo es crear un programa que procese datos estos datos son la fecha actual y un saludo personalizado y muestre los resultados directamente en la consola del navegador mediante console.log, en lugar de imprimirlo en el cuerpo de la página

---

Primero comienzo abriendo el archivo html 
```
<!doctype html>
<html lang="es">

<head>
    <meta charset="UTF-8">
</head>
```
Ahora abro el body y comienzo a escribir el script
```
<body>
```
Ahora escribo el script el cual contiene una variable que almacena la fecha actual y una funcion que recibe dos parametros y retorna una cadena de texto la cual se muestra en la consola con el console.log
```
    <script>
        let hoy = new Date();
        function diHola(nombre, edad) {
            return "Hola, " + nombre + " tienes " + edad + " años, ¿cómo estás?";
        }
        console.log("Hoy es: " + hoy.toLocaleDateString());
        console.log(diHola("Dominique", 19));
    </script>
</body>
```
Ahora cierro el body y el html
```
</html>
```

---

En conclusión he aprendido a conectar html con javascript de forma en la que he podido comprobar que puedo guardar la fecha de hoy en una variable y usarla cuando quiera lo más útil ha sido entender cómo funciona el return mi función prepara el saludo mezclando el nombre y la edad y luego entrega ese texto listo para que el console.log lo muestre es como tener una pequeña fábrica de saludos dentro de mi código
```
### 002-Seleccion y acceso a elementos
**001- lectura.html**
```html
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>JavaScript</title>
        <meta charset="utf-8">
    </head>
    <body>
        
        <p>Soy un parrafo</p>
        <script>
            // Selecciono el elemento que tenga la etiqueta p
            const elemento = document.querySelector("p");
            document.write(elemento)
            document.write(elemento.textContent)
        </script>
    </body>
</html>
```
**002-escribir.html**
```html
<!DOCTYPE html>
<html lang="es">

<head>
    <title>JavaScript</title>
    <meta charset="utf-8">
    <style>
        #rojo {
            color: red;
        }

        #verde {
            color: green;
        }

        #azul {
            color: blue;
        }
    </style>
</head>

<body>
    <div id="rojo"></div>
    <div id="verde"></div>
    <div id="azul"></div>
    <script>
        document.querySelector("#rojo").textContent = "texto rojo"
        document.querySelector("#verde").textContent = "texto verde"
        document.querySelector("#azul").textContent = "texto azul"
    </script>
</body>

</html>
```
**003-escribir html.html**
```html
<!DOCTYPE html>
<html lang="es">

<head>
    <title>JavaScript</title>
    <meta charset="utf-8">
</head>

<body>
    <div></div>
    <script>
        document.querySelector("div").innerHTML = "<h1>Hola</h1>"
    </script>
</body>

</html>
```
**004-microblog.html**
```html
<!DOCTYPE html>
<html lang="es">

<head>
    <title>JavaScript</title>
    <meta charset="utf-8">
</head>

<body>
    <header>
        <h1>El blog de Domi</h1>
    </header>
    <main></main>
    <footer>(c) 2025 Dominique Farias Osorio</footer>
    <script>
        const articulos = [
            "Primer articulo", "segundo articulo", "tercer articulo"
        ];
        const contenedor = document.querySelector("main");
        for (let i = 0; i < articulos.length; i++) {
            contenedor.innerHTML += "<h3>" + articulos[i] + "</h3>";
        }
    </script>
</body>

</html>
```
#### Ejercicio final unidad
**ejercicio final eval.html**
```html

```
**ejercicio final eval.md**
```markdown

```
### 003-creacion y modificacion de elementos
**001-crear elementos.html**
```html
<!DOCTYPE html>
<html>
    <head>

    </head>
    <body>
        <nav></nav>
        <script>
            // Esto es lo que voy a crear
            let botones = ["clientes","productos","pedidos"];
            // Selecciono el contenedor
            let contenedor = document.querySelector("nav");
            // creo un boton (solo esta en la memoria)
            let boton = document.createElement("button");
            // Ahora le pongo texto al boton
            boton.textContent = "Pulsame";
            // y ahora lo pongo en el documento
            contenedor.appendChild(boton);
        </script>
    </body>
</html>
```
**002-crear varios botones.html**
```html
<!DOCTYPE html>
<html>
    <head>

    </head>
    <body>
        <nav></nav>
        <script>
            let botones = ["clientes","productos","pedidos"];
            let contenedor = document.querySelector("nav");
            botones.forEach(function(texto_boton){
                let boton = document.createElement("button");
                boton.textContent = texto_boton;
                contenedor.appendChild(boton);
            })
        </script>
    </body>
</html>
```
**003-evento click.html**
```html
<!DOCTYPE html>
<html>
    <head>

    </head>
    <body>
        <nav></nav>
        <script>
            let botones = ["clientes","productos","pedidos"];
            let contenedor = document.querySelector("nav");
            botones.forEach(function(texto_boton){
                let boton = document.createElement("button");
                boton.textContent = texto_boton;
                contenedor.appendChild(boton);
                boton.onclick = function(){
                    console.log("Has hecho click en el boton");
                }
            })
        </script>
    </body>
</html>
```
**004-consumo.html**
```html
<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           // Ves y busca
           fetch("botones.json")
           .then(function(respuesta){
                return respuesta.json(); // La respuesta viene en json
           })
           .then(function(datos){
                console.log(datos)
           })
       </script>
   </body>
</html>
```
**005-botones desde el json.html**
```html
<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("botones.json")
           .then(function(respuesta){
               return respuesta.json(); // La respuesta viene en JSON
           })
           .then(function(datos){
               // Y luego creamos botones a partir de lo que hay en el json
           		let contenedor = document.querySelector("nav")
                datos.forEach(function(texto_boton){
                	let boton = document.createElement("button")
                    boton.textContent = texto_boton;
                    contenedor.appendChild(boton);
                })
           })
       </script>
   </body>
</html>
```
**006-recuperamos json tabla.html**
```html
<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json(); // La respuesta viene en JSON
           })
           .then(function(datos){
               console.log(datos);
           })
       </script>
   </body>
</html>
```
**007-creamos tabla.html**
```html
<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json(); // La respuesta viene en JSON
           })
           .then(function(datos){
            // Selecciono el contenedor de la tabla
               let contenedor = document.querySelector("body");
               // Primero creo una tabla en memoria
               let tabla = document.createElement("table");
               contenedor.appendChild(tabla); // Al cuerpo le añado la tabla
               // Para cada una de las lineas del json:
               datos.forEach(function(linea){
               		// Primero creo una fila - table row
                   let fila = document.createElement("tr");
                   // Ahora creo tantas celdas como sea necesario
                   linea.forEach(function(celda){
                    // Creo una celda vacia HTML
                   		let data = document.createElement("td");
                        // Le pongo texto a la celda
                       	data.textContent = celda
                        // A la fila,le añado la celda
                       	fila.appendChild(data);
                   })
                   // A la tabla le añado esta fila
                   tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>


```
**008-estilo en la tabla.html**
```html
<!doctype html>
<html>
   <head>
    <style>
        table{border: 3px plum;border-collapse: collapse;}
        table tr:first-child{background:plum;color:white;}
        table tr td{padding:10px;border-right:1px solid plum;}
       </style>
    </style>
   </head>
   <body>
       <nav></nav>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json(); // La respuesta viene en JSON
           })
           .then(function(datos){
            // Selecciono el contenedor de la tabla
               let contenedor = document.querySelector("body");
               // Primero creo una tabla en memoria
               let tabla = document.createElement("table");
               contenedor.appendChild(tabla); // Al cuerpo le añado la tabla
               // Para cada una de las lineas del json:
               datos.forEach(function(linea){
               		// Primero creo una fila - table row
                   let fila = document.createElement("tr");
                   // Ahora creo tantas celdas como sea necesario
                   linea.forEach(function(celda){
                    // Creo una celda vacia HTML
                   		let data = document.createElement("td");
                        // Le pongo texto a la celda
                       	data.textContent = celda
                        // A la fila,le añado la celda
                       	fila.appendChild(data);
                   })
                   // A la tabla le añado esta fila
                   tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>


```
**009-creo interfaz base.html**
```html
<!doctype html>
<html>
   <head>
       <style>
           html,body{heigth:100%;padding: 0px;margin: 0px;display: flex;}
           nav{background: plum;flex: 1;color: whitesmoke;}
           main{flex: 4;background: papayawhip;padding: 20px;}
       </style>
   </head>
   <body>
       <nav>1</nav>
       <main>2</main>
   </body>
</html>

```
**010-me traigo elmenu.html**
```html
<!doctype html>
<html>
   <head>
       <style>
           html,body{height:100%;padding:0px;margin:0px;display:flex;width:100%;}
           nav{background:plum;flex:1;color:white;padding:20px;}
           main{flex:4;background:aliceblue;padding:20px;}
       </style>
   </head>
   <body>
       <nav>Dominique | panel</nav>
       <style>
           nav{display:flex;flex-direction:column;gap:20px;}
           nav button{border:none;background:white;color:plum;padding:20px;}
       </style>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("botones.json")
           .then(function(respuesta){
               return respuesta.json(); // La resp viene en JSON
           })
           .then(function(datos){
               // Y luego creamos botones a partir de lo que hay en el json
               let contenedor = document.querySelector("nav")
               datos.forEach(function(texto_boton){
                   let boton = document.createElement("button")
                   boton.textContent = texto_boton;
                   contenedor.appendChild(boton);
               })
           })
       </script>
       <main>2</main>
   </body>
</html>

```
**011-ahora m etraigo la tabla.html**
```html
<!doctype html>
<html>
   <head>
       <style>
           html,body{height:100%;padding:0px;margin:0px;display:flex;width:100%;}
           nav{background:plum;flex:1;color:white;padding:20px;}
           main{flex:4;background:aliceblue;padding:20px;}
       </style>
   </head>
   <body>
       <nav>Domasa | panel</nav>
       <style>
           nav{display:flex;flex-direction:column;gap:20px;}
           nav button{border:none;background:white;color:plum;padding:20px;
           text-transform:uppercase;}
       </style>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("botones.json")
           .then(function(respuesta){
               return respuesta.json(); // La resp viene en JSON
           })
           .then(function(datos){
               // Y luego creamos botones a partir de lo que hay en el json
           		let contenedor = document.querySelector("nav")
                datos.forEach(function(texto_boton){
                	let boton = document.createElement("button")
                    boton.textContent = texto_boton;
                    contenedor.appendChild(boton);
                })
           })
       </script>
       <main>2</main>
       <style>
           table{border:3px solid plum;border-collapse:collapse;background:white;}
           table tr:first-child{background:plum;color:white;}
           table tr td{padding:10px;border-right:1px solid plum;}
       </style>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json(); // La resp viene en JSON
           })
           .then(function(datos){
               // Selecciono el contenedor de la tabla
               let contenedor = document.querySelector("main");
               // Primero creo una tabla en memoria
               let tabla = document.createElement("table");
               // Al cuerpo le añado la tabla
               contenedor.appendChild(tabla); 
               // Para cada una de las lineas del json:
               datos.forEach(function(linea){
               		// Primero creo una fila - table row
                   let fila = document.createElement("tr");
                   // Ahora creo tantas celdas como sea necesario
                   linea.forEach(function(celda){
                       	// Creo una celda vacia HTML
                   		let data = document.createElement("td");
                       	// Le pongo el texto a la celda
                       	data.textContent = celda
                       	// A la fila, le añado la celda
                       	fila.appendChild(data);
                   })
                   // A la tabla le añado esta fila
                   tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>

```
**012-consumo datos de la base de datos.html**
```html
<!doctype html>
<html>
   <head>
       <style>
           html,body{height:100%;padding:0px;margin:0px;display:flex;width:100%;}
           nav{background:indigo;flex:1;color:white;padding:20px;}
           main{flex:4;background:aliceblue;padding:20px;}
       </style>
   </head>
   <body>
       <nav>Domasa | panel</nav>
       <style>
           nav{display:flex;flex-direction:column;gap:20px;}
           nav button{border:none;background:white;color:indigo;padding:20px;
           text-transform:uppercase;}
       </style>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("http://127.0.0.1:5000/tablas")
           .then(function(respuesta){
               return respuesta.json(); // La resp viene en JSON
           })
           .then(function(datos){
               // Y luego creamos botones a partir de lo que hay en el json
           		let contenedor = document.querySelector("nav")
                datos.forEach(function(texto_boton){
                	let boton = document.createElement("button")
                    boton.textContent = texto_boton;
                    contenedor.appendChild(boton);
                })
           })
       </script>
       <main>Contenido de la tabla de clientes</main>
       <style>
           table{border:3px solid indigo;border-collapse:collapse;background:white;}
           table tr:first-child{background:indigo;color:white;}
           table tr td{padding:10px;border-right:1px solid indigo;}
       </style>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("http://127.0.0.1:5000/clientes")
           .then(function(respuesta){
               return respuesta.json(); // La resp viene en JSON
           })
           .then(function(datos){
               // Selecciono el contenedor de la tabla
               let contenedor = document.querySelector("main");
               // Primero creo una tabla en memoria
               let tabla = document.createElement("table");
               // Al cuerpo le añado la tabla
               contenedor.appendChild(tabla); 
               // Para cada una de las lineas del json:
               datos.forEach(function(linea){
               		// Primero creo una fila - table row
                   let fila = document.createElement("tr");
                   // Ahora creo tantas celdas como sea necesario
                   linea.forEach(function(celda){
                       	// Creo una celda vacia HTML
                   		let data = document.createElement("td");
                       	// Le pongo el texto a la celda
                       	data.textContent = celda
                       	// A la fila, le añado la celda
                       	fila.appendChild(data);
                   })
                   // A la tabla le añado esta fila
                   tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>

```
**botones.json**
```json
[
   	"clientes",
	"pedidos",
    "productos",
    "stock",
    "empleados"
]
```
**tabla.json**
```json
[
  ["id", "nombre", "email", "telefono", "direccion", "fecha_alta"],
  [1, "María López García", "maria.lopez@example.com", "+34 612 345 678", "Calle Mayor 12, 46001 Valencia", "2024-01-15"],
  [2, "Javier Martínez Ruiz", "javier.martinez@example.com", "+34 699 123 456", "Avenida del Puerto 88, 46022 Valencia", "2024-02-03"],
  [3, "Lucía Fernández Torres", "lucia.fernandez@example.com", "+34 644 987 321", "Calle Colón 5, 46004 Valencia", "2024-03-21"],
  [4, "Carlos Navarro Giménez", "carlos.navarro@example.com", "+34 622 111 222", "Plaza del Ayuntamiento 3, 46002 Valencia", "2024-04-10"],
  [5, "Elena Serrano Vidal", "elena.serrano@example.com", "+34 633 555 999", "Calle San Vicente 45, 46007 Valencia", "2024-05-02"]
]
```
### 004-Eliminacion de elemento
**001-primero creo un elemento.html**
```html
<!doctype html>
<html>
	<head>
  </head>
  <body>
    <div id="contenedor"></div>
   	<script>
      let elemento = document.createElement("p");
      elemento.textContent = "Contenido desde JS";
      let contenedor = document.querySelector( "#contenedor");
      contenedor.appendChild(elemento);
      
    </script>
  </body>
</html>
```
**002-eliminamos el elemento.html**
```html
<!doctype html>
<html>
	<head>
  </head>
  <body>
    <div id="contenedor"></div>
   	<script>
      let elemento = document.createElement("p");
      elemento.textContent = "Contenido desde JS";
      let contenedor = document.querySelector( "#contenedor");
      contenedor.appendChild(elemento);

      elemento.remove(); //Elimina el elemento de la pantalla
      
    </script>
  </body>
</html>
```
**003-creo tabla.html**
```html
<!doctype html>
<html>
	<head>
  </head>
  <body>
    <table></table>
   	<script>
      let tabla = document.querySelector("table")
      for(let i = 0;i<20;i++){
        let fila = document.createElement("tr")
        fila.innerHTML = "<td>Prueba</td><td>Prueba</td><td>Prueba</td>"
      	tabla.appendChild(fila)
      }
    </script>
  </body>
</html>
```
**004-click para eliminaar.html**
```html
<!doctype html>
<html>
	<head>
  </head>
  <body>
    <table></table>
   	<script>
      let tabla = document.querySelector("table")
      for(let i = 0;i<20;i++){
        let fila = document.createElement("tr")
        fila.innerHTML = "<td>Prueba</td><td>Prueba</td><td>Prueba</td>"
      	tabla.appendChild(fila)
        fila.onclick = function(){	// Cuando hago click en la fila
        	this.remove()							// La elimino
        }
      }
      
    </script>
  </body>
</html>
```
**005-retraso en ejecucion.html**
```html
<!doctype html>
<html>
	<head>
  </head>
  <body>
   	<script>
        setTimeout(function(){
            console.log("Hola que tal");
        },5000);
    </script>
  </body>
</html>
```
**006-bucle infinito.html**
```html
<!doctype html>
<html>
	<head>
  </head>
  <body>
   	<script>
        let temporizador = setTimeout("bucle()",1000);

        function bucle(){
            console.log("Hola");
            clearTimeout(temporizador) // Elimino temporizador para no acumular
            temporizador = setTimeout("bucle()",1000); // Llamo de nuevo
        }
    </script>
  </body>
</html>
```
**007-mini juego.html**
```html
<!doctype html>
<html>
	<head>
    <style>
      #jugador{width:20px;height:20px;background:rgb(188, 35, 248);position:absolute;transition:all 1s;}
   	</style>
  </head>
  <body>
    <div id="jugador"></div>
   	<script>
      // Creo un temporizador porque si no, nada se pone en marcha
      let temporizador = setTimeout("bucle()",1000);
      let posicionx = 200;
      let posiciony = 200;
      
      // Fijaos que llamo a la función desde dentro de la función
      function bucle(){
        // Primero modifico un poco la posicion del personaje
        posicionx += (Math.random()-0.5)*20;
        posiciony += (Math.random()-0.5)*20;
        // Y luego pongo una posición aleatoria para el npc
      	document.querySelector("#jugador").style.left = posicionx+"px";
        document.querySelector("#jugador").style.top = posiciony+"px";
        clearTimeout(temporizador) // Elimino temporizador para no acumular
        temporizador = setTimeout("bucle()",1000); // Llamo a bucle de nuevo
      }
      
    </script>
  </body>
</html>
```
**008-creador.html**
```html
<!doctype html>
<html>
	<head>
    <style>
      .cuadrado{width:50px;height:50px;background:rgb(163, 17, 231);position:absolute;}
      .circulo{width:50px;height:50px;background:rgba(197, 49, 255, 0.911);position:absolute;border-radius:50px;}
   	</style>
  </head>
  <body>
    <button id="pulsa_cuadrado">Pulsa para crear un cuadrado</button>
    <button id="pulsa_circulo">Pulsa para crear un circulo</button>
   	<script>
      let boton_cuadrado = document.querySelector("#pulsa_cuadrado");
      let boton_circulo = document.querySelector("#pulsa_circulo");
      
      boton_cuadrado.onclick = function(){
      	let elemento = document.createElement("div")		// Creo un elemento nuevo
        elemento.classList.add("cuadrado");							// Le pongo la clase cuadrado
        elemento.style.left = Math.random()*500+"px";		// Posición aleatoria en X
        elemento.style.top = Math.random()*500+"px";		// Posición aleatoria en Y
        document.querySelector("body").appendChild(elemento)	// Añado el elemento al body
        let rojo = Math.round(Math.random()*255);				// Creo un rojo aleatorio
        let verde = Math.round(Math.random()*255);			// Creo un verde aleatorio
        let azul = Math.round(Math.random()*255);				// Creo un azul aleatorio
        elemento.style.background = "rgb("+rojo+","+verde+","+azul+")";	// Y pongo el color
      }
      boton_circulo.onclick = function(){
      	let elemento = document.createElement("div")		// Creo un elemento nuevo
        elemento.classList.add("circulo");							// Le pongo la clase cuadrado
        elemento.style.left = Math.random()*500+"px";		// Posición aleatoria en X
        elemento.style.top = Math.random()*500+"px";		// Posición aleatoria en Y
        document.querySelector("body").appendChild(elemento)	// Añado el elemento al body
        let rojo = Math.round(Math.random()*255);				// Creo un rojo aleatorio
        let verde = Math.round(Math.random()*255);			// Creo un verde aleatorio
        let azul = Math.round(Math.random()*255);				// Creo un azul aleatorio
        elemento.style.background = "rgb("+rojo+","+verde+","+azul+")";	// Y pongo el color
      }
    </script>
  </body>
</html>
```
### 005-Manipulacion de estilos
**001-estilo en javascript.html**
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <p>Esto es un parrafo o paragrafo</p>
    <script>
      let parrafo = document.querySelector("p"); // Selecciono lo que sea
      parrafo.style.color = "red";
    </script>
  </body>
</html>
```
**002-añadir clase.html**
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      .rojo{color:red;}
    </style>
  </head>
  <body>
    <p>Esto es un párrafo o parágrafo</p>
    <script>
      let parrafo = document.querySelector("p"); // Selecciono lo que sea
      parrafo.classList.add("rojo")
    </script>
  </body>
</html>
```
**003-quitar clase.html**
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      .rojo{color:red;}
    </style>
  </head>
  <body>
    <p class="rojo">Esto es un párrafo o parágrafo</p>
    <script>
      let parrafo = document.querySelector("p"); // Selecciono lo que sea
      parrafo.classList.remove("rojo")
    </script>
  </body>
</html>
```
**004-estilo condicional.html**
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      .rojo{background:rgb(226, 69, 69);}
      .verde{background: rgb(1, 255, 1);}
    </style>
  </head>
  <body>
    <p>Esta entrada debe tener 9 caracteres solamente</p>
    <input class="rojo">
    <script>
      let entrada = document.querySelector("input")
      entrada.onkeyup = function(){
        let valor = this.value;
        let longitud = valor.length
        if(longitud == 9){
            this.classList.add("verde")
            this.classList.remove("rojo")
        }else{
            this.classList.remove("verde")
            this.classList.add("rojo")
        }
      }
    </script>
  </body>
</html>
```
**005-variables en css.html**
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      :root{
      	--color_primario:#e782f0;
     	}
      p{color:var(--color_primario);}
      div{color:var(--color_primario);}
    </style>
  </head>
  <body>
    <p>Este es un texto</p>
    <div>Este es otro texto</div>
  </body>
</html>
```
**006-funcion de calculo en css.html**
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      div{width:calc(50% + 100%);background:#e782f0;}
    </style>
  </head>
  <body>
    <div>Este es otro texto</div>
  </body>
</html>
```
### 006-Publicacion web en github
**001-Repaso de publicacion web.md**
```markdown
Que hace falta para publicar una web?

Dominio - loquesea.dominio
loquesea = nombre del dominio
.dominio = extensión

La combinación entre ambos elementos debe estar libre
(Nadie antes debe haber registrado esa combinación)

Ejemplo:
En mi caso: Domasa = nombre dominio
En mi caso: .com = Extensión que quiere decir comercial

Los dominios son mnemónicos (evitan que tengamos que recordar
las IP de los servidores)

En los años 80 extensiones originales de dominio:
.com
.net
.org
.biz

Poco después las extensiones geográficas
.es = España
.it = Italia
.ru = Rusia
.cl = Chile
.co = Colombia
.ve = Venezuela
.ma = Marruecos
.in = India
.ua = Ucrania
.cat = Cataluña
.ro = Rumanía
.nz = Nueva Zelanda

```
**002-repaso de publicacion.md**
```markdown
A continuación hace falta un hosting (alojamiento)
Es un servidor conectado a internet 24 horas al día
Sirviendo páginas web

Los dos más famosos:
-Apache2 (en decrecimiento)
-NGINX (en ascenso)
-Otros (IIS, flask, node)

Un alojamiento consiste:
-O bien tu te montas un ordenador en casa como servidor (hay que mantenerlo)
-O bien contratas algun tipo de hosting en la nube

Precios de hosting en la nube:
-Los hay desde gratuitos
-Hasta hostings de pago
(Pueden ir desde 1 euro al mes, hasta 1000 euros al mes)
```
**003-publicacin de webs en GitHub Pages.md**
```markdown
A continuación hace falta un hosting (alojamiento)
Es un servidor conectado a internet 24 horas al día
Sirviendo páginas web

Los dos más famosos:
-Apache2 (en decrecimiento)
-NGINX (en ascenso)
-Otros (IIS, flask, node)

Un alojamiento consiste:
-O bien tu te montas un ordenador en casa como servidor (hay que mantenerlo)
-O bien contratas algun tipo de hosting en la nube

Precios de hosting en la nube:
-Los hay desde gratuitos
-Hasta hostings de pago
(Pueden ir desde 1 euro al mes, hasta 1000 euros al mes)
```
**004-portafolio.html**
```html
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Portafolio Profesional</title>
    <link rel="stylesheet" href="estilo.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>

<body>
    <header id="inicio">
        <nav class="navbar">
            <div class="logo">Dominique</div>
            <ul class="nav-links">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#sobre-mi">Sobre Mí</a></li>
                <li><a href="#proyectos">Proyectos</a></li>
                <li><a href="#habilidades">Habilidades</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
            <div class="hamburger">
                <i class="fas fa-bars"></i>
            </div>
        </nav>
        <div class="hero">
            <div class="hero-content">
                <h1>Hola, soy <span class="highlight">Dominique</span></h1>
                <p>Desarrollador Web & Diseñador Creativo</p>
                <a href="#proyectos" class="btn">Ver Mis Proyectos</a>
            </div>
        </div>
    </header>

    <section id="sobre-mi" class="section">
        <div class="container">
            <h2 class="section-title">Sobre Mí</h2>
            <div class="about-content">
                <div class="about-text">
                    <p>Soy un apasionado por la tecnología y el diseño web. Me dedico a crear experiencias digitales
                        únicas y funcionales. Siempre estoy aprendiendo nuevas tecnologías para mejorar mis habilidades
                        y ofrecer lo mejor en cada proyecto.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="proyectos" class="section">
        <div class="container">
            <h2 class="section-title">Mis Proyectos</h2>
            <div class="projects-grid">
                <!-- Proyecto 1: Mecanografía -->
                <div class="project-card">
                    <div class="project-image">
                        <div class="placeholder-img">Mecanografía</div>
                    </div>
                    <div class="project-info">
                        <h3>Juego de Mecanografía</h3>
                        <p>Juego interactivo para practicar velocidad de escritura con estadísticas en tiempo real.</p>
                        <a href="../../../../1º  Trimestre/trydd.html" class="btn-small" target="_blank">Ver
                            Proyecto</a>
                    </div>
                </div>
                <!-- Proyecto 2: Perfil Visual -->
                <div class="project-card">
                    <div class="project-image">
                        <div class="placeholder-img">Perfil Visual</div>
                    </div>
                    <div class="project-info">
                        <h3>Perfil Profesional</h3>
                        <p>Diseño de perfil personal con layout en grid y tarjetas de información.</p>
                        <a href="../../../../1º  Trimestre/examenfinal.html" class="btn-small" target="_blank">Ver
                            Proyecto</a>
                    </div>
                </div>
                <!-- Proyecto 3: Blog Visual -->
                <div class="project-card">
                    <div class="project-image">
                        <div class="placeholder-img">Blog Visual</div>
                    </div>
                    <div class="project-info">
                        <h3>Blog de Artículos</h3>
                        <p>Diseño de blog con múltiples artículos organizados en una cuadrícula.</p>
                        <a href="../../../../1º  Trimestre/smlenguajema.html" class="btn-small" target="_blank">Ver
                            Proyecto</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="habilidades" class="section">
        <div class="container">
            <h2 class="section-title">Habilidades</h2>
            <div class="skills-container">
                <div class="skill-item"><i class="fab fa-html5"></i> HTML5</div>
                <div class="skill-item"><i class="fab fa-css3-alt"></i> CSS3</div>
                <div class="skill-item"><i class="fab fa-js"></i> JavaScript</div>
                <div class="skill-item"><i class="fab fa-git-alt"></i> Git</div>
                <div class="skill-item"><i class="fas fa-mobile-alt"></i> Responsive Design</div>
                <div class="skill-item"><i class="fas fa-paint-brush"></i> UI/UX</div>
            </div>
        </div>
    </section>

    <section id="contacto" class="section">
        <div class="container">
            <h2 class="section-title">Contáctame</h2>
            <form class="contact-form">
                <div class="form-group">
                    <input type="text" placeholder="Nombre" required>
                </div>
                <div class="form-group">
                    <input type="email" placeholder="Email" required>
                </div>
                <div class="form-group">
                    <textarea placeholder="Mensaje" rows="5" required></textarea>
                </div>
                <button type="submit" class="btn">Enviar Mensaje</button>
            </form>
            <div class="social-links">
                <a href="#"><i class="fab fa-github"></i></a>
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
            </div>
        </div>
    </section>

    <footer>
        <p>&copy; 2024 Dominique. Todos los derechos reservados.</p>
    </footer>
</body>

</html>
```
**estilo.css**
```css
/* Variables y Reset */
:root {
    --primary-color: #8b5cf6;
    --secondary-color: #7c3aed;
    --accent-color: #a78bfa;
    --bg-color: #f5f3ff;
    --text-color: #4c1d95;
    --light-text: #ffffff;
    --card-bg: #ffffff;
    --transition: all 0.3s ease;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Poppins', sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--bg-color);
}

a {
    text-decoration: none;
    color: inherit;
}

ul {
    list-style: none;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 5%;
    background-color: var(--card-bg);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
}

.logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary-color);
}

.nav-links {
    display: flex;
    gap: 2rem;
}

.nav-links a {
    font-weight: 500;
    transition: var(--transition);
}

.nav-links a:hover {
    color: var(--primary-color);
}

.hamburger {
    display: none;
    font-size: 1.5rem;
    cursor: pointer;
}

/* Hero Section */
.hero {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, #f5f3ff 0%, #ddd6fe 100%);
    padding-top: 80px;
}

.hero-content h1 {
    font-size: 3.5rem;
    margin-bottom: 1rem;
}

.highlight {
    color: var(--primary-color);
}

.hero-content p {
    font-size: 1.5rem;
    color: #4b5563;
    margin-bottom: 2rem;
}

.btn {
    display: inline-block;
    padding: 0.8rem 2rem;
    background-color: var(--primary-color);
    color: var(--light-text);
    border-radius: 50px;
    font-weight: 600;
    transition: var(--transition);
    border: none;
    cursor: pointer;
}

.btn:hover {
    background-color: var(--secondary-color);
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(37, 99, 235, 0.2);
}

/* Sections General */
.section {
    padding: 5rem 5%;
}

.section-title {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 3rem;
    color: var(--text-color);
    position: relative;
}

.section-title::after {
    content: '';
    display: block;
    width: 50px;
    height: 4px;
    background-color: var(--primary-color);
    margin: 0.5rem auto 0;
    border-radius: 2px;
}

/* About Section */
.about-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
    font-size: 1.1rem;
}

/* Projects Section */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.project-card {
    background-color: var(--card-bg);
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    transition: var(--transition);
}

.project-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
}

.project-image {
    height: 200px;
    background-color: #e5e7eb;
    display: flex;
    justify-content: center;
    align-items: center;
}

.placeholder-img {
    color: #9ca3af;
    font-weight: 600;
}

.project-info {
    padding: 1.5rem;
}

.project-info h3 {
    margin-bottom: 0.5rem;
    color: var(--text-color);
}

.project-info p {
    color: #6b7280;
    margin-bottom: 1.5rem;
    font-size: 0.95rem;
}

.btn-small {
    color: var(--primary-color);
    font-weight: 600;
    font-size: 0.9rem;
}

.btn-small:hover {
    text-decoration: underline;
}

/* Skills Section */
.skills-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1.5rem;
    max-width: 800px;
    margin: 0 auto;
}

.skill-item {
    background-color: var(--card-bg);
    padding: 1rem 2rem;
    border-radius: 50px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: var(--transition);
}

.skill-item i {
    color: var(--primary-color);
    font-size: 1.2rem;
}

.skill-item:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

/* Contact Section */
.contact-form {
    max-width: 600px;
    margin: 0 auto;
    background-color: var(--card-bg);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 1rem;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    font-family: inherit;
    font-size: 1rem;
    transition: var(--transition);
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.contact-form button {
    width: 100%;
}

.social-links {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 3rem;
}

.social-links a {
    font-size: 1.5rem;
    color: #6b7280;
    transition: var(--transition);
}

.social-links a:hover {
    color: var(--primary-color);
    transform: translateY(-3px);
}

/* Footer */
footer {
    background-color: var(--text-color);
    color: var(--light-text);
    text-align: center;
    padding: 2rem;
    margin-top: 5rem;
}

/* Responsive */
@media (max-width: 768px) {
    .nav-links {
        display: none;
    }

    .hamburger {
        display: block;
    }

    .hero-content h1 {
        font-size: 2.5rem;
    }

    .section {
        padding: 3rem 5%;
    }
}
```
## 004-Definicios de esquemas y vocabularios en lenguajes de marcas
### 001-Tecnologias para la definicion de documentos. Estructura y sintaxis
**000-Introduccion.md**
```markdown
XML = Información plana
Mismo origen que HTML

HTML lo crea Tim Berners-Lee
A partir de HMTL se generaliza XML

Es para guardar los datos

XHTML despues de crear XML
AMbos vienen filosoficamente de SGML

Son estándares que tienen notación, normativa

Son para datos que cambian

eXtensible Markup Language

```
**001-repaso xml.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>

```
**002-debe de haber una etiqueta raiz.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  
</persona>

```
**003-case sensitive.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  
</Persona>
Esto está mal

```
**004-subetiquetas.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Dominique</nombre>
  <apellidos>Farias Osorio</apellidos>
</persona>

```
**005-varios telefonos.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Dominique</nombre>
  <apellidos>Farías Osorio</apellidos>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
    ...
  </telefonos>
</persona>

```
### 002-creacion de descripciones de documentos
**001-documento de referencia.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Dominique</nombre>
  <apellidos>Farias Osorio</apellidos>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
  </telefonos>
</persona>

```
### 003-Asociacion de descripcion con documentos. Validacion
**001-documento de referencia.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Dominique</nombre>
  <apellido>Farias Osorio</apellido>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
  </telefonos>
</persona>

```
**003-validador.py**
```python
# pip3 install lxml --break-system-packages

from lxml import etree

xml_doc = etree.parse("001-documento de referencia.xml")
xsd_doc = etree.parse("002-esquema.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))

```
## 005-Conversion y adaptacion de documentos para el intercambio de informacion
### 001-Tecnologias de transformacion de documentos
**000-resumen.md**
```markdown

```
**001-formatos de documentos que conocemos.md**
```markdown
py = script en python - documento

pdf = portable document file
docx = documento de Word 
txt = texto plano
odt = open document

json = contenedor de información en objetos
javascript object notation
xml = extensible markup languaje

xlsx = Excel de Microsoft
ods = Open Document Spreadsheet

pptx = Powerpoint
odp = Open Document Presentation

sql = dump de base de datos

```
**002-pdf a texto.py**
```python
# pip3 install pypdf --break-system-packages
from pypdf import PdfReader

lector = PdfReader("librophp.pdf")
texto = ""

for pagina in lector.pages:
    texto += pagina.extract_text() + "\n"

print(texto)
```
**003-texto a pdf.py**
```python
# pip3 install fpdf --break-system-packages
from fpdf import FPDF

def text_to_pdf(text, filename="salida.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.cell(0, 10, txt=line, ln=True)

    pdf.output(filename)

text_to_pdf("Hola este es un texto desde Python")
```
**004-excel a python.py**
```python
# pip3 install pandas --break-system-packages
# pip3 install odfpy --break-system-packages

import pandas as pd

df = pd.read_excel('empresa.ods', engine='odf')
data = df.to_dict(orient='records')
print(data)
```
**005-desde python a excel.py**
```python
import pandas as pd

diccionario = [
    {
        "titular": "Noticia 1",
        "fecha": "2025-12-09",
        "contenido": "Este es el contenido de la noticia 1"
    },
    {
        "titular": "Noticia 2",
        "fecha": "2025-12-10",
        "contenido": "Este es el contenido de la noticia 2"
    },
    {
        "titular": "Noticia 3",
        "fecha": "2025-12-11",
        "contenido": "Este es el contenido de la noticia 3"
    }
]

# Convertir a DataFrame
df = pd.DataFrame(diccionario)

# Exportar a Excel
df.to_excel("noticias.xlsx", index=False)

print("Archivo creado: noticias.xlsx")
```
#### Ejercicio final unidad
**ejercicio final eval.md**
```markdown
En este ejercicio voy a trabajar con las edades de la tabla clientes para practicar la precisión en los cálculos primero usaré SQL para calcular el promedio de edad pero probaré tres formas distintas de redondear el resultado al más cercano, hacia abajo y hacia arriba para ver cómo cambian las cifras finalmente tomaré la lista completa de edades y utilizaré un programa de Python con matplotlib para crear un gráfico de pastel lo que me ayudará a ver los datos en lugar de solo ver números en una tabla

---

Primero comienzo entrando a la base de datos clientes
```
USE clientes;
```

Ahora voy a calcular el promedio redondeado al entero más cercano
```
SELECT ROUND(AVG(edad)) FROM clientes;
```
Y el resultado es:
```
+------------------+
| ROUND(AVG(edad)) |
+------------------+
|               34 |
+------------------+
1 row in set (0.006 sec)
```

Ahora voy a calcular el promedio redondeado hacia abajo al entero más cercano
```
SELECT FLOOR(AVG(edad)) FROM clientes;
```
Y el resultado es:
```
+------------------+
| FLOOR(AVG(edad)) |
+------------------+
|               34 |
+------------------+
1 row in set (0.006 sec)
```

Ahora voy a calcular la promedio redondeado hacia arriba al entero más cercano
```
SELECT CEIL(AVG(edad)) FROM clientes;
```
Y el resultado es:
```
+-----------------+
| CEIL(AVG(edad)) |
+-----------------+
|              35 |
+-----------------+
1 row in set (0.000 sec)
```

Ahora voy a mostrar todos los clientes
```
SELECT * FROM clientes;
```
Y el resultado es:
```
+--------+----------------------+------+
| nombre | apellidos            | edad |
+--------+----------------------+------+
| Juan   | Pérez García         |   28 |
| María  | López Rodríguez      |   34 |
| Carlos | González Sánchez     |   45 |
| Ana    | Martínez Fernández   |   22 |
| Luis   | Ramírez Torres       |   56 |
| Sofía  | Hernández Díaz       |   31 |
| Miguel | Torres Ruiz          |   40 |
| Elena  | Flores Morales       |   29 |
| David  | Castillo Romero      |   37 |
| Laura  | Vargas Ortiz         |   19 |
+--------+----------------------+------+
10 rows in set (0.006 sec)
```

Ahora voy a mostrar un grafico de torta de la edad de los clientes
```
import matplotlib.pyplot as pt

data = [28, 34, 45, 22, 56, 31, 40, 29, 37, 19]

pt.pie(data)
pt.show()
```

---

En conclusión este ejercicio integra el procesamiento numérico en base de datos con la visualización gráfica en programación en la fase de SQL he comprobado la importancia de las funciones escalares ROUND, FLOOR, CEIL para normalizar los resultados de funciones de agregación como AVG permitiendome controlar exactamente cómo se manejan los decimales finalmente la implementación de matplotlib en Python demuestra cómo los datos brutos pueden transformarse en información visual facilitando la interpretación rápida de la distribución en un grafico de los clientes
```
**ejercicio final eval.py**
```python

```