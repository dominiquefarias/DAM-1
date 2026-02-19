En este ejercicio realizare una integración completa de todo lo visto en la unidad para conectar una base de datos con una interfaz web comenzare en el backend diseñando la estructura de datos en sql que serian las tablas de clientes y productos y asegurando el acceso mediante la creación de un usuario con privilegios específicos despues desarrollare una "aplicacion" sencilla con Python y Flask que servirá como puente extrayendo la información y entregándola en formato json y por ultimo implementare la parte visual con html y javascript utilizando la función fetch para consumir los datos dinámicamente y mostrarlos en el navegador

---

Primero creo una base de datos y dos tablas clientes y productos con lo que se me ha dado en el ejercicio
```
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS tiendaclase;
USE tiendaclase;

-- Tabla clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(100)
);

-- Tabla productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Datos de prueba: clientes
INSERT INTO clientes (nombre, email, telefono)
VALUES
    ('Ana López', 'ana@example.com', '600123456'),
    ('Carlos Ruiz', 'carlos@example.com', '611987654'),
    ('María Gómez', 'maria@example.com', '622111222');

-- Datos de prueba: productos
INSERT INTO productos (nombre, descripcion, precio, stock)
VALUES
    ('Portátil 15"', 'Portátil de 15 pulgadas con 16GB RAM', 899.99, 10),
    ('Ratón inalámbrico', 'Ratón óptico inalámbrico', 19.90, 50),
    ('Teclado mecánico', 'Teclado con switches azules', 59.95, 30);
```
Ahora creo un servidor web con flask para mostrar los datos de las tablas en base a una plantilla entregada
```
import mysql.connector 
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/clientes")
def clientes():
    cursor = conexion.cursor() 
    cursor.execute("SELECT * FROM clientes;")  

    filas = cursor.fetchall()
    return json.dumps(filas)

@app.route("/tablas")
def tablas():
    cursor = conexion.cursor() 
    cursor.execute("SHOW TABLES;")  

    filas = cursor.fetchall()
    tablas = []
    for fila in filas:
        tablas.append(fila[0])
    return json.dumps(tablas)

if __name__ == "__main__":
    app.run(debug=True)
```
Ahora creo un usuario y le doy todos los permisos
```
CREATE USER 
'tiendaclase'@'localhost' 
IDENTIFIED  BY 'Tiendaclase123$';

GRANT USAGE ON *.* TO 'tiendaclase'@'localhost';

ALTER USER 'tiendaclase'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendaclase.* 
TO 'tiendaclase'@'localhost';

FLUSH PRIVILEGES;
```
Luego utilizo el siguiente codigo para conectarme a la base de datos mediante el usuario creado
```
import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="tiendaclase",
  password="Tiendaclase123$",
  database="tiendaclase"
)
```
Ahora utilizo el siguiente codigo para mostrar los datos de la base de datos en un servidor web
```
import mysql.connector 
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/clientes")
def clientes():
    cursor = conexion.cursor() 
    cursor.execute("SELECT * FROM clientes;")  

    filas = cursor.fetchall()
    return json.dumps(filas)

if __name__ == "__main__":
    app.run(debug=True)
```
Ahora creo un archivo html y con un script de javascript para mostrar los datos de la base de datos en un servidor web
```
<!doctype html>
<html>
   <head>
       <style>
           html,body{height:100%;padding:0px;margin:0px;display:flex;width:100%;}
           nav{background:indigo;flex:1;color:white;padding:20px;}
           main{flex:3;background:#f4f4f9;padding:20px;}
       </style>
   </head>
   <body>
       <nav>Menu</nav>
       <main>
           <h1>Clientes</h1>
           <script>
               fetch('/clientes')
                   .then(response => response.json())
                   .then(data => {
                       const clientes = document.getElementById('clientes');
                       data.forEach(cliente => {
                           const li = document.createElement('li');
                           li.textContent = `${cliente.nombre} - ${cliente.email}`;
                           clientes.appendChild(li);
                       });
                   });
           </script>
           <ul id="clientes"></ul>
       </main>
   </body>
</html>
```

---

En conclusión este ejercicio incluye todo lo visto en la unidad logrado desacoplar la base de datos de la interfaz de usuario utilizando una aplicacion intermedia construida con Flask esto demuestra el papel crucial del Backend que seria python como gestor que extrae la información cruda de MySQL y la convierte al formato estándar JSON permitiendo que el Frontend que seria JavaScript y que la consuma y la presente al usuario de forma dinámica 