# Reporte de proyecto

## Estructura del proyecto

```
/Users/dominique/Desktop/Dam2.0/DAM-1/2º  Trimestre/Proyecto intermodular
├── 000-Ejercicos  Frankenstein
│   ├── Conexion PHP con MySQL
│   │   ├── 0001-CON IA.php
│   │   ├── 001-Primero creo la base de datos.sql
│   │   ├── 002-crear usuario.sql
│   │   ├── 003-primera prueba de conexion.php
│   │   ├── 004-le damos forma.php
│   │   └── 005-blog completo y bonito.php
│   ├── Conexion python y sql
│   │   ├── 001-Preparamos base de datos.py
│   │   ├── 003-plantilla de conexion.py
│   │   ├── 004-proyeccion y ordenacion.py
│   │   ├── 005-resultado como diccionario.py
│   │   ├── 006-ya no vomito.py
│   │   └── 007-resultado como json.py
│   ├── Enviar informacion
│   │   ├── 001-primer servidor.py
│   │   ├── 002- tomo parametro.py
│   │   ├── 003-microformulario.py
│   │   ├── 004-lanzamos los datos.py
│   │   └── templates
│   │       └── index.html
│   ├── Leer json
│   │   ├── 001-leer json.html
│   │   ├── 003-microservidor.py
│   │   ├── static
│   │   │   └── curriculum.json
│   │   └── templates
│   │       └── index.html
│   ├── jinja
│   │   ├── 001-estatico.py
│   │   ├── 002-multipagina.py
│   │   ├── 003-representar variable.py
│   │   ├── 004-directiva for.py
│   │   ├── 005-backoffice.py
│   │   ├── 006-backoffice con mysql.py
│   │   ├── 007-paso varias cosas.py
│   │   └── templates
│   │       ├── backoffice.html
│   │       ├── contacto.html
│   │       ├── inicio.html
│   │       ├── lista.html
│   │       ├── sobremi.html
│   │       └── variable.html
│   └── plantilla proyecto
│       ├── 001-creaar periodico.sql
│       ├── 002-insertar noticias de prueba.sql
│       ├── 003-crear usuario.sql
│       ├── 004-problema y solucion.sql
│       └── aplicacion
│           ├── admin
│           │   ├── escritorio.php
│           │   ├── index.php
│           │   └── procesalogin.php
│           ├── css
│           │   └── estilo.css
│           ├── inc
│           │   └── listar_articulos.php
│           └── index.php
├── 001-Busqueda de informacion
│   ├── 001-identificar empresas representantes
│   │   └── 001-Introduccion.md
│   ├── 002-Estructuras de las empresas
│   │   └── 001-Introduccion.md
│   ├── 003-Caracteristicas de lo departamentos
│   │   └── 001--introduccion.md
│   ├── 005-Evaluacion del volumen de negocio
│   │   ├── 001-introduccion.md
│   │   └── 002-otro modelo de negocio.md
│   └── 006-Estreategia para dar respuestas a las demandas
│       └── 001-introduccion.md
├── 002-Seleccion de un servicio o producto
│   └── 001-Identificar las necesidades
│       └── 001-introduccion.md
└── Proyectos alumnos
    ├── 001-Ana y alfredo
    │   └── index.php
    ├── 002-Sara y Piero
    │   └── index.php
    └── 003-Andres
        ├── index.php
        ├── index2.php
        └── ruleta.jpg
```

## Código (intercalado)

# Proyecto intermodular
## 000-Ejercicos  Frankenstein
### Conexion PHP con MySQL
**0001-CON IA.php**
```php
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Moderno</title>
    <style>
        /* 1. Estilos Generales */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 40px;
            color: #333;
        }

        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 40px;
        }

        /* 2. Contenedor Grid (Rejilla) */
        .blog-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsivo automático */
            gap: 25px;
            max-width: 1200px;
            margin: 0 auto;
        }

        /* 3. Diseño de la Tarjeta (Card) */
        .article-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            padding: 25px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            border-left: 5px solid #3498db; /* Un toque de color */
        }

        /* Efecto Hover */
        .article-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.12);
        }

        /* 4. Tipografía interna */
        .article-card h3 {
            margin-top: 0;
            color: #2c3e50;
            font-size: 1.5rem;
            margin-bottom: 10px;
        }

        .meta-info {
            font-size: 0.85rem;
            color: #7f8c8d;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }

        .content {
            line-height: 1.6;
            color: #555;
        }
    </style>
</head>
<body>

    <h1>Últimas Entradas</h1>

    <div class="blog-container">
        <?php
        // Configuración de la base de datos
        $host = "localhost";
        $user = "blogphp";
        $pass = "Blogphp123$";
        $db   = "blogphp";

        // Crear conexión con control de errores básico
        $conexion = new mysqli($host, $user, $pass, $db);

        // Verificar si hay error en la conexión
        if ($conexion->connect_error) {
            die("<p style='color:red; text-align:center'>Error de conexión: " . $conexion->connect_error . "</p>");
        }

        // Establecer charset a UTF-8 para evitar problemas con tildes/ñ
        $conexion->set_charset("utf8");

        $sql = "SELECT * FROM blog ORDER BY fecha DESC"; // Ordenado por fecha
        $resultado = $conexion->query($sql);

        if ($resultado->num_rows > 0) {
            while ($fila = $resultado->fetch_assoc()) {
                // IMPORTANTE: Usamos htmlspecialchars para seguridad (evitar XSS)
                $titulo = htmlspecialchars($fila['titulo']);
                $fecha = date("d/m/Y", strtotime($fila['fecha'])); // Formatear fecha
                $autor = htmlspecialchars($fila['autor']);
                $contenido = htmlspecialchars($fila['contenido']);

                // Si el contenido es muy largo, lo cortamos
                $resumen = (strlen($contenido) > 150) ? substr($contenido, 0, 150) . '...' : $contenido;

                echo '
                <article class="article-card">
                    <h3>' . $titulo . '</h3>
                    <div class="meta-info">
                        <time>📅 ' . $fecha . '</time>
                        <span>✍️ ' . $autor . '</span>
                    </div>
                    <p class="content">' . $resumen . '</p>
                </article>
                ';
            }
        } else {
            echo "<p style='text-align:center; width:100%'>No hay entradas en el blog aún.</p>";
        }

        $conexion->close();
        ?>
    </div>

</body>
</html>

```
**001-Primero creo la base de datos.sql**
```sql
prompt: 
sql to create a database called 
blogphp with table blog 
and insert several articles in spanish

CREATE DATABASE IF NOT EXISTS blogphp
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE blogphp;

CREATE TABLE IF NOT EXISTS blog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    autor VARCHAR(100) DEFAULT 'Administrador'
);

INSERT INTO blog (titulo, contenido, autor) VALUES
('Bienvenidos a mi nuevo blog',
 'Este es el primer artículo del blog. Aquí compartiré tutoriales, noticias y recursos útiles sobre programación y tecnología.',
 'Dominique Farias'),

('Cómo instalar PHP y Apache en Ubuntu',
 'En este artículo aprenderás a instalar un entorno AMP en Ubuntu utilizando los repositorios oficiales y configurando los módulos necesarios.',
 'Dominique Farias'),

('Introducción a SQL para principiantes',
 'SQL es un lenguaje fundamental para trabajar con bases de datos. En esta guía veremos las instrucciones básicas: SELECT, INSERT, UPDATE y DELETE.',
 'Dominique Farias'),

('Consejos para mejorar tu productividad como programador',
 'Organizar el tiempo, dividir el trabajo en tareas pequeñas y mantener un entorno ordenado puede ayudarte a avanzar más rápidamente en tus proyectos.',
 'Dominique Farias');

```
**002-crear usuario.sql**
```sql
CREATE USER 
'blogphp'@'localhost' 
IDENTIFIED  BY 'Blogphp123$';

GRANT USAGE ON *.* TO 'blogphp'@'localhost';

ALTER USER 'blogphp'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON blogphp.* 
TO 'blogphp'@'localhost';

FLUSH PRIVILEGES;

```
**003-primera prueba de conexion.php**
```php
<?php

  $host = "localhost";
  $user = "blogphp";
  $pass = "Blogphp123$";
  $db   = "blogphp";

  $conexion = new mysqli($host, $user, $pass, $db);

  $sql = "SELECT * FROM blog";

  $resultado = $conexion->query($sql);

  while ($fila = $resultado->fetch_assoc()) {
    var_dump($fila);
  }

  $conexion->close();
  
?>

```
**004-le damos forma.php**
```php
<?php

  $host = "localhost";
  $user = "blogphp";
  $pass = "Blogphp123$";
  $db   = "blogphp";

  $conexion = new mysqli($host, $user, $pass, $db);

  $sql = "SELECT * FROM blog";

  $resultado = $conexion->query($sql);

  while ($fila = $resultado->fetch_assoc()) {
    echo '
    	<article>
      	<h3>'.$fila['titulo'].'</h3>
        <time>'.$fila['fecha'].'</time>
        <p>'.$fila['autor'].'</p>
        <p>'.$fila['contenido'].'</p>
      </article>
    ';
  }

  $conexion->close();
  
?>

```
**005-blog completo y bonito.php**
```php
<!doctype html>
<html>
	<head>
  </head>
  <body>
  	<header>
    	<h1>Jose Vicente Carratala</h1>
      <h2>Blog superinteresante</h2>
    </header>
    <main>
      <?php

        $host = "localhost";
        $user = "blogphp";
        $pass = "Blogphp123$";
        $db   = "blogphp";

        $conexion = new mysqli($host, $user, $pass, $db);

        $sql = "SELECT * FROM blog";

        $resultado = $conexion->query($sql);

        while ($fila = $resultado->fetch_assoc()) {
          echo '
            <article>
              <h3>'.$fila['titulo'].'</h3>
              <time>'.$fila['fecha'].'</time>
              <p>'.$fila['autor'].'</p>
              <p>'.$fila['contenido'].'</p>
            </article>
          ';
        }

        $conexion->close();

      ?>
  	</main>
  	<footer>
  	</footer>
  </body>
</html>

```
### Conexion python y sql
**001-Preparamos base de datos.py**
```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

```
**003-plantilla de conexion.py**
```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

filas = cursor.fetchall()

print(filas)

```
**004-proyeccion y ordenacion.py**
```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

cursor = conexion.cursor()
cursor.execute('''
	SELECT
	nombre AS "Nombre del cliente",
	apellidos AS "apellidos del cliente",
	edad AS "Edad del cliente"
''')

filas = cursor.fetchall()

print(filas)

```
**005-resultado como diccionario.py**
```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

cursor = conexion.cursor(dictionary=True) # Diccionario
cursor.execute('''
	SELECT
	nombre AS "Nombre del cliente",
	apellidos AS "apellidos del cliente",
	edad AS "Edad del cliente"
''')

filas = cursor.fetchall()

print(filas)

```
**006-ya no vomito.py**
```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

cursor = conexion.cursor(dictionary=True) # Diccionario
cursor.execute('''
	SELECT
	nombre AS "Nombre del cliente",
	apellidos AS "apellidos del cliente",
	edad AS "Edad del cliente"
''')

filas = cursor.fetchall()

for fila in filas:
	print("Nombre",fila['Nombre del cliente'])
	print("Apellidos: ",fila['Apellidos del cliente'])
	print("Edad: ",fila['Edad del cliente'])
	print("###################")

```
**007-resultado como json.py**
```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

cursor = conexion.cursor(dictionary=True) # Diccionario
cursor.execute('''
	SELECT
	nombre AS "Nombre del cliente",
	apellidos AS "apellidos del cliente",
	edad AS "Edad del cliente"
	FROM clientes
	ORDER BY edad DESC;
''')

filas = cursor.fetchall()
resultado_json = json.dumps(filas, ensure_ascii=False,indent=2)
print(resultado_json)

for fila in filas:
	print("Nombre",fila['Nombre del cliente'])
	print("Apellidos: ",fila['Apellidos del cliente'])
	print("Edad: ",fila['Edad del cliente'])
	print("###################")s

```
### Enviar informacion
**001-primer servidor.py**
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return ""
	
if __name__ == "__main__":
    app.run(debug=True)

```
**002- tomo parametro.py**
```python
from flask import Flask, request  # Tomo parametros de la url

app = Flask(__name__)

@app.route("/")
def inicio():
    nombre = request.args.get("nombre")
    print(nombre)
    return "Mira en la consola si ha pasado algo"

if __name__ == "__main__":
    app.run(debug=True)
    
# http://127.0.0.1:5000/?nombre=DominiqueS

```
**003-microformulario.py**
```python
from flask import Flask, render_template, request  # Tomo parametros de la url

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/envio")
def envio():
    nombre = request.args.get("nombre")
    apellidos = request.args.get("apellidos")
    print(nombre,apellidos)
    return "Mira en la consola si ha pasado algo"

if __name__ == "__main__":
    app.run(debug=True)
    
# http://127.0.0.1:5000/?nombre=DominiqueS

```
**004-lanzamos los datos.py**
```python
from flask import Flask, render_template, request  # Tomo parametros de la url

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/envio")
def envio():
   nombre = request.args.get("nombre")
   apellidos = request.args.get("apellidos")
 print(nombre,apellidos)
	return "nombre:"+nombre"-apellidos:"+apellidos

if __name__ == "__main__":
    app.run(debug=True)
    
# http://127.0.0.1:5000/?nombre=DominiqueS

```
#### templates
**index.html**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Micro formulario</title>
        <meta charset="utf-8">
        <style>
            html,body{background: #9370DB;display:flex;justify-content:center;align-items:center;min-height:100vh;}
            form{width:300px;height:300px;padding:20px;background:white;display:flex;flex-direction:column;justify-content:center;gap:20px;}
            input{padding:20px;}
        </style>
    </head>
    <body>
        <form action="/envio" method="get">
            <input type="text" name="nombre" placeholder="Introduce tu nombre">
            <input type="text" name="apellidos" placeholder="Introduce tus apellidos">
            <input type="submit">
        </form>
    </body>
</html>
```
### Leer json
**001-leer json.html**
```html
<!DOCTYPE html>
<html lang="es">
	<head>
		<title>Plantilla fetch</title>
		<meta charset="utf-8">
	</head>
	<body>
		<script>
			fetch("curriculum.json")
			.then(function(respuesta){
				return respuesta.json();
			}
		)
		.then(function(datos){
			console.log(datos);
		})
		</script>
	</body>
</html>

```
**003-microservidor.py**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")
	
if __name__ == "__main__":
    app.run(debug=True)


```
#### static
**curriculum.json**
```json
{
	"datos_personales":{
		"nombre":"Dominique",
		"apellidos":"Farias Osorio",
		"correo":"domi@mail.com",
		"telefonos":["12345678","1234587"]
	},
	"experiencias_laborales":[
		{
			"titulo":"picker",
			"empresa":"aban",
			"tiempo":"2025"
		},
		{
			"titulo":"picker",
			"empresa":"aban",
			"tiempo":"2025"
		},
		{
			"titulo":"picker",
			"empresa":"aban",
			"tiempo":"2025"
		},
		
	]
}

```
#### templates
**index.html**
```html
<!DOCTYPE html>
<html lang="es">
	<head>
		<title>Plantilla fetch</title>
		<meta charset="utf-8">
	</head>
	<body>
		<h1>--nombre--</h1>
		<h2>--apellidos--</h2>
		<h3>--correo--</h3>
		<script>
			fetch("static/curriculum.json")
			.then(function(respuesta){
				return respuesta.json();
			}
		)
		.then(function(datos){
			console.log(datos);
			document.querySelector("h1").textContent = datos.datos_personales.nombre
			document.querySelector("h2").textContent = datos.datos_personales.apellidos
			document.querySelector("h3").textContent = datos.datos_personales.correo
		})
		</script>
	</body>
</html>

```
### jinja
**001-estatico.py**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("estatico.html")
	
if __name__ == "__main__":
    app.run(debug=True)


```
**002-multipagina.py**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")
	
if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/sobremi")
def inicio():
    return render_template("sobremi.html")
	
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/contacto")
def inicio():
    return render_template("contacto.html")
	
if __name__ == "__main__":
    app.run(debug=True)



```
**003-representar variable.py**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
	# mi nombre es la variable que esta en python
	mi_nombre = "Dominique"
	# nombre es la variable que lanzo la pagina
	return render_template("variable.html",nombre=mi_nombre)
	
if __name__ == "__main__":
    app.run(debug=True)
    




```
**004-directiva for.py**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
	mis_frutas = ["Manzanas","Peras","Platanos","Frutilla"]
	return render_template("lista.html",frutas=mis_frutas)
	
if __name__ == "__main__":
    app.run(debug=True)
    




```
**005-backoffice.py**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("backoffice.html")
	
if __name__ == "__main__":
    app.run(debug=True)


```
**006-backoffice con mysql.py**
```python
from flask import Flask, render_template

import mysql.connector

print("Bienvenidos a la aplicación")

conexion = mysql.connector.connect(

  host="localhost",        

  user="dominique5",        

  password="Domi.virt3",     

  database="portafolioexamen"   
)
cursor = conexion.cursor()
cursor.execute("SHOW TABLES;")
tablas = []
filas = cursor.fetchall()
for fila in filas:
	tablas.append(fila[0])

app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("backoffice.html",mis_tablas = tablas)
	
if __name__ == "__main__":
    app.run(debug=True)


```
**007-paso varias cosas.py**
```python
from flask import Flask, render_template

import mysql.connector

print("Bienvenidos a la aplicación")

conexion = mysql.connector.connect(

  host="localhost",        

  user="dominique5",        

  password="Domi.virt3",     

  database="portafolioexamen"   
)
cursor = conexion.cursor()
cursor.execute("SHOW TABLES;")
tablas = []
filas = cursor.fetchall()
for fila in filas:
	tablas.append(fila[0])
	
cursor.execute("SHOW COLUMNS in piezasportafolio;")
columnas = []
filas = cursor.fetchall()
for fila in filas:
	columnas.append(fila[0])
	
cursor.execute("SELECT * FROM piezasportafolio;")
contenido_tabla = cursor.fetchall()

app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template(
		"backoffice.html",
		mis_tablas = tablas,
		mis_columnas = columnas,
		mi_contenido_tabla = contenido_tabla
	)
	
if __name__ == "__main__":
    app.run(debug=True)


```
#### templates
**backoffice.html**
```html
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Backoffice</title>
        <meta charset="utf-8">
        <style>
            html,body{background: #9370DB;width: 100%;height: 100%;padding: 0px;margin: 0px;}
            main{display: flex;height: 100%;}
            header{color: black;padding: 20px;}
            nav{flex: 1;color: white;padding: 20px;display: flex;flex-direction: column;gap: 20px;}
            section{flex: 5;background: white;padding: 20px;}
            nav a{background: white;color: #9370DB;padding: 20px;}
        </style>
    </head>
    <body>
        <header>Aplicacion empresarial BKN de Dominique</header>
        <main>
            <nav>
                <a>Clientes</a>
                <a>Productos</a>
                <a>Pedidos</a>
                <section>
                    Contenido
                </section>
            </nav>
        </main>
    </body>
</html>

```
**contacto.html**
```html
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>La pagina de Dominique</title>
    </head>
    <body>
        <h1>La pagina de Dominique</h1>
        <nav>
            <a href="/">Inicio</a>
            <a href="/sobremi">Sobre mi</a>
            <a href="/contacto">Contacto</a>
        </nav>
        <p>Esta es la pagina de Contacto</p>
    </body>
</html>

```
**inicio.html**
```html
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>La pagina de Dominique</title>
    </head>
    <body>
        <h1>La pagina de Dominique</h1>
        <nav>
            <a href="/">Inicio</a>
            <a href="/sobremi">Sobre mi</a>
            <a href="/contacto">Contacto</a>
        </nav>
        <p>Esta es la pagina de inicio</p>
    </body>
</html>

```
**lista.html**
```html
<ol>
{%for fruta in frutas%}
    <li>{{fruta}}</li>
{% endfor %}
</ol>

```
**sobremi.html**
```html
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>La pagina de Dominique</title>
    </head>
    <body>
        <h1>La pagina de Dominique</h1>
        <nav>
            <a href="/">Inicio</a>
            <a href="/sobremi">Sobre mi</a>
            <a href="/contacto">Contacto</a>
        </nav>
        <p>Esta es la pagina Sobre mi</p>
    </body>
</html>

```
**variable.html**
```html
<p>Esto es un contenido estatico</p>
<p>Pero esto es un contenido dinamico: {{nombre}}</p>

```
### plantilla proyecto
**001-creaar periodico.sql**
```sql
-- Crear la base de datos
CREATE DATABASE periodico
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

-- Seleccionar la base de datos
USE periodico;

-- Tabla de autores
CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    bio TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de noticias
CREATE TABLE noticias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    autor_id INT NULL,   -- ← Debe permitir NULL

    CONSTRAINT fk_noticias_autores
        FOREIGN KEY (autor_id)
        REFERENCES autores(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);
```
**002-insertar noticias de prueba.sql**
```sql
INSERT INTO autores (nombre, email, bio) VALUES
('María López', 'maria.lopez@example.com', 'Periodista especializada en política nacional.'),
('Carlos Fernández', 'carlos.fernandez@example.com', 'Redactor de tecnología y startups.'),
('Ana Martínez', 'ana.martinez@example.com', 'Corresponsal internacional con base en Bruselas.'),
('Javier Ruiz', 'javier.ruiz@example.com', 'Experto en economía y mercados financieros.');


INSERT INTO noticias (titulo, contenido, autor_id) VALUES
('El Gobierno anuncia nuevas medidas económicas',
 'El presidente ha detallado un conjunto de reformas destinadas a impulsar el crecimiento y reducir el desempleo.',
 1),

('Una startup española desarrolla un dron autónomo revolucionario',
 'La empresa valenciana AeroTech ha presentado su nuevo dron capaz de realizar rutas complejas sin intervención humana.',
 2),

('La Unión Europea debate un nuevo acuerdo climático',
 'Los representantes de los estados miembros negocian un paquete de medidas para acelerar la transición energética.',
 3),

('El mercado bursátil cierra la semana con una subida inesperada',
 'Los principales índices han registrado incrementos tras la publicación de datos positivos sobre empleo.',
 4),

('Nuevas inversiones en energías renovables para 2025',
 'El Ministerio de Industria ha anunciado un plan que prevé incrementar la producción solar en un 30%.',
 1);
```
**003-crear usuario.sql**
```sql
CREATE USER 
'periodico'@'localhost' 
IDENTIFIED  BY 'Periodico123$';

GRANT USAGE ON *.* TO 'periodico'@'localhost';

ALTER USER 'periodico'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON periodico.* 
TO 'periodico'@'localhost';

FLUSH PRIVILEGES;
```
**004-problema y solucion.sql**
```sql
CREATE USER 
'periodico'@'localhost' 
IDENTIFIED  BY 'Periodico123$';

GRANT USAGE ON *.* TO 'periodico'@'localhost';

ALTER USER 'periodico'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON periodico.* 
TO 'periodico'@'localhost';

FLUSH PRIVILEGES;
```
#### aplicacion
**index.php**
```php
<!doctype html>
<html lang="es">

<head>
    <title>Domasa - Noticias tecnológicas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/estilo.css">
</head>

<body>
    <header>
        <h1>Domasa</h1>
        <h2>Noticias tecnológicas</h2>
    </header>
    <main>
        <?php include "inc/listar_articulos.php"; ?>
    </main>
    <footer>
    </footer>
</body>

</html>
```
##### admin
**escritorio.php**
```php
Si estas viendo esto, es que has conseguido hacer login ok
```
**index.php**
```php
Hola yo soy el back<br>
Y en primer lugar hacemos login<br>
```
**procesalogin.php**
```php
Yo te voy a procesar el login<br>
Y si es correcto, te voy a llevar al panel
```
##### css
**estilo.css**
```css
body,
html {
    width: 100%;
    height: 100%;
    margin: 0px;
    padding: 0px;
}

header,
main,
footer {
    width: 800px;
    margin: auto;
}

header,
footer {
    text-align: center;
}

main {
    display: grid;
    grid-template-columns: repeat(2, 100fr);
    gap: 20px;
}
```
##### inc
**listar_articulos.php**
```php
<?php
$host = "localhost";
$user = "periodico";
$pass = "Periodico123$";
$db = "periodico";
$conexion = new mysqli($host, $user, $pass, $db);
$sql = "SELECT * FROM noticias";
$resultado = $conexion->query($sql);
while ($fila = $resultado->fetch_assoc()) {
  echo '
            <article>
              <h3>' . $fila['titulo'] . '</h3>
              <time>' . $fila['fecha_publicacion'] . '</time>
              <p>' . $fila['autor_id'] . '</p>
              <p>' . $fila['contenido'] . '</p>
            </article>
          ';
}
$conexion->close();
```
## 001-Busqueda de informacion
### 001-identificar empresas representantes
**001-Introduccion.md**
```markdown
Ahora que tenéis una idea de negocio
(un producto/servicio)

La primera tarea que tenéis que hacer consiste en analizar el entorno de aplicación

Mi recomendación:
Primero entorno local
Luego entorno regional
Luego entorno nacional
Y luego entorno internacional

Análisis de mercado local:
1.-Paso 1: Buscamos en Google
2.-Paso 2: Usamos la "investigación en profundidad" de ChatGPT (o similares)

A continuación:
Apuntáis las empresas más representativas en un documento
Nombre de la empresa
URL
Correo si lo encontráis
Resumen de las actividades de la empresa


```
### 002-Estructuras de las empresas
**001-Introduccion.md**
```markdown
Ya tenemos localizadas a las empresas de la competencia
Tenemos que averiguar/estimar
-Volumen de la empresa
-Numero de empleados
-Capital social
-Toda la información posible

Posible origen: BORME
```
### 003-Caracteristicas de lo departamentos
**001--introduccion.md**
```markdown
Que departamentos podemos encontrar en una empresa?

Direccion
	Dirige
RRHH
	Contrataciones, psico, despidos, bienestar, 
Finanzas/contabilidad
	Plata, gestión, facturas, cobros, 
Marketing/Gestion de ventas
	Org campañas, promueve, vender, rrss, atrae clientes
Att Cliente
	Resolver problemas, garantías
Proyectos
	Organizar el año, ideas de productos, 
Informatica/Desarrollo
	Esclavos
Mantenimiento
	Limpieza, reparan cosas
Comercio Internacional/Transporte Logística
	Si hay producto fisico, analizan como llevarlo
Legal
	Controlar legalidad, copyright, asistencia jur., demandas
Dep formación
	Preparación personal nuevo, actualizaciones a empleados
Salud
	Cuida por el beneficio de la empresa

En cada una de vuestras empresas
Tenéis que pensar los departamentos deseables
Y los departamentos realistas para arrancar en un primer momento

Supuesto:
Hay 12 departamentos, supongamos 1 persona por departamento, supongamos
un sueldo bruto de 2200 euros en limpio 1500 

26.400 euros en salarios cada mes

De lo que se trata es de intentar reducir ese número a algo realista

1-3

Lo que queremos en esta subunidad es estimar los recursos que pueden ser necesarios
Y los costes asociados de arrancar este proyecto
```
### 005-Evaluacion del volumen de negocio
**001-introduccion.md**
```markdown
Caso del software de reserva de pistas:

Pregunta:
Cuantas pistas deportivas hay en Valencia Provincia

Fuente posible: 
La página del INE

Provincia de Valencia
266

CV: 542 polideportivos

Primera ronda de visitas:
12 clientes

Depende de las funciones, depende 
Una básica: SaaS - cuota
cuota inicial + soporte - puede asustar
Digamos un porcentaje a éxito

15% de lo que cueste la reserva

12€/1.5h = 15% de ese dinero sería para el software

Si el centro deportivo abre de 9 a 21
8 reservas
8 * 120
120 * 30 = 3600 euros
```
**002-otro modelo de negocio.md**
```markdown
Inicialmente la idea es vender software de reservas

Otro modelo de negocio posible:
Crear una "red social" de jugadores
Crear un app
Que enlace a unos jugadores con otros, y que jueguen
Y que reserven pistas

Esto parece un win win
Ganan los jugadores
Ganan los polideportivos
Gana la empresa que haga esa aplicación
```
### 006-Estreategia para dar respuestas a las demandas
**001-introduccion.md**
```markdown
Cuales son las demandas:
Las demandas son las necesidades del mercado
Que vosotros detectáis
Y ante las cuales proponéis una solución

Qué solución vais a proponer?
Vais a proponer un software
Vais a proponer un producto

Recomendación:
Tener al lado (cerca) a una persona que sea experta en la materia
Si es posible vosotros mismos

```
## 002-Seleccion de un servicio o producto
### 001-Identificar las necesidades
**001-introduccion.md**
```markdown
Caso del software para reserva de pistas:

Estado actual: reserva por teléfono
Propuesta: Aplicación: Más cómodo
Se podría ver la disponibilidad

24 horas al día en una app

Una aplicación podría aportar una mayor disponibilidad
La app es más cómoda / idioma
Menos carga de trabajo para una persona / automatización

(posibles cuestiones éticas)

Antecedentes:

En la revolución industrial (s18) muchos artesanos se quedaron
sin trabajo

La revolución de internet dejó sin trabajo a empleos
como carteros

```
## Proyectos alumnos
### 001-Ana y alfredo
**index.php**
```php
<!doctype>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        article {
            background: white;
        }

        @media (max-width: 500px) {
            body {
                background: red;
                font-size: 48px;
                display: flex;
                flex-direction: column;
                gap: 20px;
            }
        }

        @media (min-width: 500px) and (max-width: 1000px) {
            body {
                background: green;
            }
        }

        @media (min-width: 1000px) {
            body {
                background: blue;
                font-size: 12px;
                display: grid;
                grid-template-columns: repeat(4, 100fr);
                gap: 20px;
            }
        }
    </style>
</head>

<body>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>

</body>

</html>
```
### 002-Sara y Piero
**index.php**
```php
<!doctype>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        html,
        body {
            width: 100%;
            height: 100%;
            padding: 0px;
            margin: 0px;
        }

        body {
            display: flex;
            width: 100%;
            height: 100%;
        }

        nav {
            flex: 1;
            background: #7d50a1;
            padding: 20px;
            display: flex;
            flex-direction: column;
        }

        main {
            flex: 4;
            background: #b398e9;
            padding: 20px;
            display: grid;
            grid-template-columns: repeat(3, 100fr);
            gap: 20px;
        }

        article {
            background: white;
        }

        @media (max-width: 500px) {
            body {
                display: flex;
                width: 100%;
                height: 100%;
                flex-direction: column;
            }
        }
    </style>
</head>

<body>
    <nav>
        <a href="">Mis reservas</a>
        <a href="">Mi cuenta</a>
    </nav>
    <main>
        <article>
            <img>
            <h3>Disponible</h3>
            <p>10€ por semana</p>
            <a href="">Add to cart</a>
        </article>
        <article>
            <img>
            <h3>Disponible</h3>
            <p>10€ por semana</p>
            <a href="">Add to cart</a>
        </article>
        <article>
            <img>
            <h3>Disponible</h3>
            <p>10€ por semana</p>
            <a href="">Add to cart</a>
        </article>
        <article>
            <img>
            <h3>Disponible</h3>
            <p>10€ por semana</p>
            <a href="">Add to cart</a>
        </article>
        <article>
            <img>
            <h3>Disponible</h3>
            <p>10€ por semana</p>
            <a href="">Add to cart</a>
        </article>
        <article>
            <img>
            <h3>Disponible</h3>
            <p>10€ por semana</p>
            <a href="">Add to cart</a>
        </article>
        <article>
            <img>
            <h3>Disponible</h3>
            <p>10€ por semana</p>
            <a href="">Add to cart</a>
        </article>
        <article>
            <img>
            <h3>Disponible</h3>
            <p>10€ por semana</p>
            <a href="">Add to cart</a>
        </article>
    </main>

</body>

</html>
```
### 003-Andres
**index.php**
```php
<!doctype>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        button {
            background: indigo;
            border: none;
            border-radius: 5px;
            padding: 10px;
            color: white;
            transition: all 1s;
            box-shadow: 0px 5px 4px black;
        }

        button:hover {
            background: red;
            transform: translateY(4px);
            box-shadow: 0px 0px 2px black;
        }
    </style>
</head>

<body>
    <button>Pulsame</button>
</body>

</html>
```
**index2.php**
```php
<!doctype>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        #ruleta {
            animation: frena 10s;
        }

        @keyframes frena {
            0% {
                transform: rotate(0deg);
            }

            100% {
                transform: rotate(359deg);
            }
        }
    </style>
</head>

<body>
    <img id="ruleta" src="ruleta.jpg">
</body>

</html>
```