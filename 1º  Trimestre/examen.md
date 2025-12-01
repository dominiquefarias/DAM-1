
En este ejercicio se aplican todos los conocimientos vistos en el primer trimestre donde desarrollo una "aplicación" web utilizando python y flask, que se conecta a una base de datos para mostrar de manera mas dinamica que solo por terminal la información de un "portafolio" creado en clases
El objetivo principal es integrar los conocimientos de bases de datos, programación, generando una página con la estructurada en HTML y CSS donde los datos se extraen directamente de una vista en mysql

Este tipo de aplicación es útil en proyectos donde se requiere mostrar información actualizada en tiempo real como en portafolios o catálogos de productos

---

Primero importo mporto el módulo mysql.connector que permite a Python conectarse y trabajar con bases de datos mysql:

```

import mysql.connector

````

Luego importo Flask usada para crear aplicaciones web en python:

```

from flask import Flask

```

Ahora establezco la conexión con la base de datos mysql

```

conexion = mysql.connector.connect(
    # Dirección del servidor 
    host="localhost",
    # Nombre del usuario que tiene acceso a la base de datos
    user="dominique3",
    # Contraseña del usuario
    password="Domi123$",
    # Nombre de la base de datos con la que se trabajará
    database="portafolioexamen"
)
```

Despues creo un cursor que es el objeto que permite ejecutar sentencias sql dentro de la base de datos

```

cursor = conexion.cursor()

```

Ahora creo una instancia de la aplicación Flask que servirá como servidor web

```

app = Flask(__name__)

```

Luego uso @app.route para definir la ruta principal del sitio web 

```

@app.route("/")

```

Ahora defino la función que se ejecutará cuando el usuario visite la página principal

```
def portafolio():
    # Ejecuto una consulta a sql a la vista que une las tablas de piezas y categorías
    cursor.execute("SELECT titulo, descripcion, fecha, nombre FROM piezasportafolio_categoriasportafolio;")
    
    # Guardo todos los resultados obtenidos de la consulta en una lista llamada filas
    filas = cursor.fetchall()

```

Ahora inicio la construcción del código HTML que se devolverá al navegador

> Esto es para que en el navegador se pueda mostrar de manera ordenada lo que hicimos en html y el conjunto con python y la base de datos

```
    cadena = ''' 
    <!-- Indica que el documento usa la versión HTML5 -->
    <!doctype html> 
    <!-- Define el idioma principal del contenido como español -->
    <html lang="es"> 
    <!-- Contiene información sobre el documento, como título y estilos -->
    <head> 
        <!-- Título que aparece en la pestaña del navegador -->
        <title>Portafolio Dominique</title> 
        <!-- Define la codificación de caracteres para admitir tildes y eñes -->
        <meta charset="utf-8"> 
        <!-- Bloque de estilos CSS -->
        <style> 
            /* Estilos generales para todo el documento */
            html,body{
                /* Color de fondo gris para toda la página */
                background:grey; 
                /* Fuente tipográfica del texto */
                font-family:sans-serif; 
            }
            /* Estilos aplicados a header, main y footer */
            header,main,footer{

                background:white; /* Fondo blanco para cada sección principal */
                /* Espaciado interno de 20 píxeles */
                padding:20px;     
                /* Ancho fijo del contenido */
                width:800px;      
                /* Centrado horizontal automático */
                margin:auto;      
                /* Alineación centrada del texto */
                text-align:center;
            }
            main{
                /* Usa diseño tipo cuadrícula */
                display:grid; 
                /* Crea tres columnas automáticas */
                grid-template-columns:auto auto auto; 
                /* Espacio entre las columnas y filas */
                gap:20px; 
            }
        </style> 
    </head> 
    <!-- Cuerpo del documento visible en el navegador -->
    <body> 
        <!-- Encabezado del sitio -->
        <header> 
            <!-- Nombre del autor del portafolio -->
            <h1>Dominique Farias Osorio</h1> 
            <!-- Correo de contacto -->
            <h2>dominiquefarias21@gmail.com</h2> 
        </header>
        <!-- Sección principal donde se mostrarán los artículos -->
        <main> 
    '''
```

Luego recorro cada fila obtenida de la base de datos y agrego un bloque article por cada registro

```
    for fila in filas:

````

Cada artículo representa una pieza del portafolio

```
        cadena += '''
            <!-- Cada artículo contiene la información de una pieza -->
            <article> 
                <!-- Muestra la categoría (nombre) -->
                <p>''' + fila[3] + '''</p>        
                <!-- Muestra el título de la pieza -->
                <h3>''' + fila[0] + '''</h3>      
                <!-- Muestra la descripción -->
                <p>''' + fila[1] + '''</p>        
                <!-- Muestra la fecha -->
                <p>''' + fila[2] + '''</p> 
            
            </article> 
        '''

```

Ahora cierro la estructura del HTML agregando el pie de página y cerrando las etiquetas principales

```
    cadena += ''' 
        <!-- Cierre de la sección principal -->
        </main> 
        <!-- Pie de página del sitio -->
        <footer> 
            <!-- Mensaje de derechos de autor -->
            (c) 2025 Dominique Farias Osorio 
        <!-- Cierre del pie de página -->
        </footer> 
    <!-- Cierre del cuerpo del documento -->
    </body> 
    <!-- Cierre del documento HTML -->
    </html> 
    '''

```

Luego devuelvo el contenido html completo al navegador como respuesta de la página

```

    return cadena

```

Ahora verifico si este archivo se está ejecutando directamente

```
if __name__ == "__main__":
    # Inicio el servidor web Flask en modo depuración para ver errores en tiempo real
    app.run(debug=True)

```

---

Este ejercicio me permitió poner en práctica los conocimientos adquiridos sobre bases de datos y programación
A través de la combinación de el modulo flask, mysql y html, logre construir una "aplicación" web dinámica que muestra un una web donde desde la gestión de datos hasta su visualización en un navegador
Con este ejercicio se consoido la comprensión del desarrollo de esta "aplicación" basada en datos, integrando las distintas unidades vistas en el trimestre
