En este ejercicio voy a conectar python con sql para gestionar una agenda de clientes primero creo la base de datos
Una vez creada la base de datos utilizo tres scripts ya hechos en clases de python diferentes para conectarme a la base de datos uno para ver todos los datos, otro para ordenar la información por apellidos, y un tercero para obtener los resultados en un formato más organizado ordenados por edad

---

Primero creo la base de datos clientes y utilizo el comando USE para seleccionarla
```
CREATE DATABASE IF NOT EXISTS clientes;

USE clientes;
```
Ahora si creo la tabla clientes con los campos id, nombre, apellidos y edad e inserto algunos datos 
```
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    edad INT
);

INSERT INTO clientes (nombre, apellidos, edad) VALUES
('Juan', 'Lopez', 45),
('Javier', 'Martines', 46),
('Ana', 'Garcia', 28),
('Pedro', 'Rodriguez', 35);


```

Ahora creo el usuario clientes y le asigno los permisos necesarios para acceder a la base de datos clientes
```
CREATE USER 
'clientes'@'localhost' 
IDENTIFIED  BY 'Clientes123$';

GRANT USAGE ON *.* TO 'clientes'@'localhost';

ALTER USER 'clientes'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON clientes.* TO 'clientes'@'localhost';

FLUSH PRIVILEGES;
```

Ahora con la plantilla de conexion.py la utilizo para conectarme a la base de datos clientes y mostrar los datos de los clientes

```
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="clientes",        
  password="Clientes123$",     
  database="clientes"   
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

filas = cursor.fetchall()

print(filas)
```

Ahora con la plantilla de proyeccion y ordenacion.py la utilizo para conectarme a la base de datos clientes y mostrar los datos de los clientes ordenados por apellidos

```
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="clientes",        
  password="Clientes123$",     
  database="clientes"   
)

cursor = conexion.cursor()
cursor.execute('''
	SELECT
	nombre,
	apellidos
	FROM clientes
	ORDER BY apellidos ASC;
''')

filas = cursor.fetchall()

print(filas)


```

Ahora con la plantilla de resultado como diccionario.py la utilizo para conectarme a la base de datos clientes y mostrar los datos de los clientes ordenados por edad en orden descendente

```
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="clientes",        
  password="Clientes123$",     
  database="clientes"   
)

cursor = conexion.cursor(dictionary=True) # Diccionario
cursor.execute('''
	SELECT
	nombre AS "Nombre del cliente",
	apellidos AS "Apellidos del cliente",
	edad AS "Edad del cliente"
	FROM clientes
	ORDER BY edad DESC;
''')

filas = cursor.fetchall()

print(filas)

```

---

En conclusion he logrado conectar python con sql para gestionar una agenda de clientes creando una base de datos y un usuario propio los plantillas de python desarrollados confirman que la conexión es estable y que podemos extraer la información de los clientes de manera personalizada ya sea como lista simple, ordenada por apellidos, o estructurada con etiquetas claras para saber qué es cada dato