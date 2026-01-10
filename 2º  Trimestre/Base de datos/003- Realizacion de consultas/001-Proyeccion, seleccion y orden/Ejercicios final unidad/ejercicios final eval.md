

---

Primero creo la base de datos clientes

```
CREATE DATABASE clientes;
```

Luego me sitúo en la base de datos clientes

```
USE clientes;
```

Ahora creo la tabla clientes con los campos nombre, apellidos y edad

```
CREATE TABLE clientes(
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	edad INT
);
```

Ahora inserto los datos en la tabla clientes

```
INSERT INTO clientes (nombre, apellidos, edad) VALUES
('Juan', 'Pérez García', 28),
('María', 'López Rodríguez', 34),
('Carlos', 'González Sánchez', 45),
('Ana', 'Martínez Fernández', 22),
('Luis', 'Ramírez Torres', 56),
('Sofía', 'Hernández Díaz', 31),
('Miguel', 'Torres Ruiz', 40),
('Elena', 'Flores Morales', 29),
('David', 'Castillo Romero', 37),
('Laura', 'Vargas Ortiz', 19);
```

Ahora selecciono todos los datos de la tabla clientes

```
SELECT * FROM clientes;
```

Lo cual me da los siguientes resultados

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
10 rows in set (0.000 sec)
```

Ahora selecciono los datos de la tabla clientes ordenados por edad

```
SELECT nombre AS 'Nombre del cliente', apellidos AS 'Apellidos del cliente', edad AS 'Edad del cliente' FROM clientes ORDER BY edad DESC;
```

Lo cual me da los siguientes resultados

```
+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Luis               | Ramírez Torres        |               56 |
| Carlos             | González Sánchez      |               45 |
| Miguel             | Torres Ruiz           |               40 |
| David              | Castillo Romero       |               37 |
| María              | López Rodríguez       |               34 |
| Sofía              | Hernández Díaz        |               31 |
| Elena              | Flores Morales        |               29 |
| Juan               | Pérez García          |               28 |
| Ana                | Martínez Fernández    |               22 |
| Laura              | Vargas Ortiz          |               19 |
+--------------------+-----------------------+------------------+
10 rows in set (0.006 sec)
```

Ahora selecciono solo el nombre y los apellidos de los clientes

```
SELECT nombre, apellidos FROM clientes;
```

Lo cual me da los siguientes resultados

```
+--------+----------------------+
| nombre | apellidos            |
+--------+----------------------+
| Juan   | Pérez García         |
| María  | López Rodríguez      |
| Carlos | González Sánchez     |
| Ana    | Martínez Fernández   |
| Luis   | Ramírez Torres       |
| Sofía  | Hernández Díaz       |
| Miguel | Torres Ruiz          |
| Elena  | Flores Morales       |
| David  | Castillo Romero      |
| Laura  | Vargas Ortiz         |
+--------+----------------------+
10 rows in set (0.000 sec)
```

Ahora selecciono solo el nombre y los apellidos de los clientes 

```
SELECT nombre AS 'Nombre del cliente', apellidos AS 'Apellidos del cliente', edad AS 'Edad del cliente' FROM clientes;
```

Lo cual me da los siguientes resultados

```
+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Juan               | Pérez García          |               28 |
| María              | López Rodríguez       |               34 |
| Carlos             | González Sánchez      |               45 |
| Ana                | Martínez Fernández    |               22 |
| Luis               | Ramírez Torres        |               56 |
| Sofía              | Hernández Díaz        |               31 |
| Miguel             | Torres Ruiz           |               40 |
| Elena              | Flores Morales        |               29 |
| David              | Castillo Romero       |               37 |
| Laura              | Vargas Ortiz          |               19 |
+--------------------+-----------------------+------------------+
10 rows in set (0.000 sec)
```

---
