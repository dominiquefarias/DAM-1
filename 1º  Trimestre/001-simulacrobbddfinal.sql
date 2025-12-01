# Iniciamos sesion en MySQL --> sudo mysql -u root -p

# Creamos la base de datos --> CREATE DATBASE portafolio1;

CREATE DATABASE portafolio1;
Query OK, 1 row affected (0,01 sec)

# Nos aseguramos de que exista la base de datos --> SHOW DATABASES;

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
| sys                |
| tienda             |
+--------------------+
11 rows in set (0,00 sec)

# Ingresamos a la base de datos --> USE portafolio1;

Database changed

# Ahora creamos una tabla:
	CREATE TABLE categoria(
		Identificador INT AUTO_INCREMENT PRIMARY KEY,
		tituloc VARCHAR(100),
		descripcionc VARCHAR(100)
	);

# Utilizo un DESCRIBE para ver la formacion de la tabla:

+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| tituloc       | varchar(100) | YES  |     | NULL    |                |
| descripcionc  | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
3 rows in set (0,01 sec)

# Creo la tabla de pieza:
CREATE TABLE pieza (
	Identificador INT(100) AUTO_INCREMENT,
	titulop VARCHAR(100),
	descripcionp VARCHAR(100),
	imagen VARCHAR(100),
	url VARCHAR(100),
	id_categoria VARCHAR(100),
	PRIMARY KEY (Identificador)
);

# Utilizo un DESCRIBE para ver la formacion de la tabla:

+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulop       | varchar(100) | YES  |     | NULL    |                |
| descripcionp  | varchar(100) | YES  |     | NULL    |                |
| imagen        | varchar(100) | YES  |     | NULL    |                |
| url           | varchar(100) | YES  |     | NULL    |                |
| id_categoria  | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
6 rows in set (0,00 sec)


# Ahora creo una foreign key

ALTER TABLE pieza
ADD CONSTRAINT pieza_a_categoria
FOREIGN KEY (id_categoria)
REFERENCES categoria(Identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

# Ahora creo una vista de ese join

CREATE VIEW piezas_categorias AS
SELECT 
pieza.Identificador AS id_pieza,
pieza.titulop,
pieza.descripcionp,
pieza.imagen,
pieza.url,
categoria.Identificador AS id_categoria,
categoria.tituloc AS titulo_categoria,
categoria.descripcionc AS descripcion_categoria
FROM pieza
LEFT JOIN categoria
ON pieza.id_categoria = categoria.Identificador;

Qué hace esto:

Crea una vista llamada piezas_categorias.

Une las tablas pieza y categoria.

Muestra:

Los datos de cada pieza (titulop, descripcionp, imagen, url).

Los datos de su categoría (tituloc, descripcionc).

Usa un LEFT JOIN, así que mostrará todas las piezas, incluso si alguna no tiene categoría asignada (el campo de categoría aparecerá como NULL).
