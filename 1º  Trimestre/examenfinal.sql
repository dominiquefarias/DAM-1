* En este ejercicio se trabaja con la creación y relación de tablas en MySQL, además de la generación de una vista para facilitar la consulta de datos. Primero, se crea la base de datos portafolio1 y dentro de ella las tablas categoria y pieza, donde cada pieza se asocia a una categoría mediante una clave foránea. Posteriormente, se establece la relación entre ambas tablas con FOREIGN KEY y se crea una vista llamada piezas_categorias, que combina la información de las dos tablas utilizando un LEFT JOIN. Esta vista permite visualizar de manera conjunta los datos de cada pieza junto con su categoría, simplificando el acceso y análisis de la información almacenada.

Primero inicio sesion en la base de datos a traves de el siguiente comando:
---
```
sudo mysql -u root -p
```
---
Luego creo una base de datos llamada portafolioexamen de la siguiente manera:
```
CREATE DATABASE portafolioexamen;
```
---
Luego me aseguro de que exista la base de datos con lo siguiente:
---
`SHOW DATABASES;`
---
Lo que saldria todo esto: 
---
````
+--------------------+
| Database           |
+--------------------+
| biblioteca25       |
| ejemplosclave      |
| ejemplosclaves     |
| empresadam         |
| information_schema |
| musica_videojuegos |
| mysql              |
| performance_schema |
| portafolio1        |
| portafolioexamen   |
| sys                |
| tienda             |
+--------------------+
````
---
Ahora ingreso a la base de datos:
```
USE DATABASE portafolioexamen;
```
---
Ahora comienzo a crear la tabla que me pidieron con los siguientes parametros (Identificador, nombre)
```
CREATE TABLE categoriasportafolio(
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);
```
---
Ahora autilizo un `DESCRIBE` para ver la como se ha formado la tabla:
---
```
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
```
---
Ahora creo la otra tabla que seria piezasportafolio con los siguientes parametros (Identificador,titulo,descripcion,fecha,id_categoria):
---
```
CREATE TABLE piezasportafolio(
    Identificador INT(100) AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    descripcion VARCHAR(100),
    fecha VARCHAR(100),
    id_categoria VARCHAR(100)
);
```
---
Ahora utilizo DESCRIBE  para ver como ha quedado la tabla:
---
```
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripcion   | varchar(100) | YES  |     | NULL    |                |
| fecha         | varchar(100) | YES  |     | NULL    |                |
| id_categoria  | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

-- Ahora creo una FOREIGN KEY 

ALTER TABLE piezasportafolio
ADD CONSTRAINT pieza_a_categoria
FOREIGN KEY (id_categoria)
REFERENCES categoriasportafolio(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

-- Como en la creacion de la tabla el id_categoria era varchar debo de cambiarlo a int para poder crear la foreign key lo cual utilizo un ALTER TABLE
ALTER TABLE piezasportafolio
MODIFY COLUMN id_categoria INT;

-- Lo cual ahora me deja hacer la FOREIGN KEY ya que es un numero

-- Ahora le añadire unos valores a cada tabla:
INSERT INTO categoriasportafolio VALUES(
    NULL,
    'Dominique'
);

-- Y ahora le inserto un valor a la otra tabla

INSERT INTO piezasportafolio VALUES(
    NULL,
    'Titulo de la primera entrada',
    '2025-11-03',
    'Este es la descripcion de la primera entrada',
    1
);


SELECT
FROM piezasportafolio.titulo,piezasportafolio.descripcion,piezasportafolio.fecha,categoriasportafolio.nombre,
LEFT JOIN categoriasportafolio
ON piezasportafolio.id_autor = categoriasportafolio.Identificador;
-- Ahora creo la vista y el LEFT JOIN

CREATE VIEW piezasportafolio_categoriasportadolio AS
SELECT
piezasportafolio.Identificador AS id_pieza,
piezasportafolio.titulo,
piezasportafolio.descripcion,
piezasportafolio.fecha,
categoriasportafolio.Identificador AS id_categoria,
categoriasportafolio.nombre AS titulo_categoria,
FROM piezasportafolio
LEFT JOIN categoriasportafolio
ON piezasportafolio.id_categoria = categoriasportafolio.Identificador;