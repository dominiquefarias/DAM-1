
import mysql.connector


conexion = mysql.connector.connect(
    # Dirección del servidor 
    host="localhost",      
    # Nombre del usuario que tiene acceso a la base de datos
    user="dominique1",     
    # Contraseña del usuario
    password="Domi123$",   
    # Nombre de la base de datos con la que se trabajará
    database="portafolioexamen"  
)

from flask import Flask

cursor = conexion.cursor()

app = Flask(__name__)

@app.route("/")

def portafolio():
    # Ejecuto una consulta a sql a la vista que une las tablas de piezas y categorías
    cursor.execute("SELECT titulo, descripcion, fecha, nombre FROM piezasportafolio_categoriasportafolio;")
    
    # Guardo todos los resultados obtenidos de la consulta en una lista llamada filas
    filas = cursor.fetchall()

    cadena = ''' 
    <!-- Indica que el documento usa la versión html5 -->
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

    for fila in filas:

        cadena += '''
            <!-- Cada artículo contiene la información de una pieza -->
            <article> 
                <!-- Muestra la categoría -->
                <p>''' + fila[3] + '''</p>        
                <!-- Muestra el título de la pieza -->
                <h3>''' + fila[0] + '''</h3>      
                <!-- Muestra la descripción -->
                <p>''' + fila[1] + '''</p>        
                <!-- Muestra la fecha -->
                <p>''' + fila[2] + '''</p> 
            
            </article> 
        '''

    cadena += ''' 
        <!-- Cierre de la sección principal -->
        </main> 
        <!-- Pie de página del sitio -->
        <footer> 
            (c) 2025 Dominique Farias Osorio 
        <!-- Cierre del pie de página -->
        </footer> 
    <!-- Cierre del cuerpo del documento -->
    </body> 
    <!-- Cierre del documento HTML -->
    </html> 
    '''

    return cadena

if __name__ == "__main__":
    # Inicio el servidor web Flask en modo depuración para ver errores en tiempo real
    app.run(debug=True)