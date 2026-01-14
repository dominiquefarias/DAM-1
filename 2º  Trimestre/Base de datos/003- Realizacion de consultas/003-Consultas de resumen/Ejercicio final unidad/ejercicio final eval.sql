SELECT ROUND(AVG(edad)) FROM clientes;
+------------------+
| ROUND(AVG(edad)) |
+------------------+
|               34 |
+------------------+
1 row in set (0.006 sec)

SELECT FLOOR(AVG(edad)) FROM clientes;
+------------------+
| FLOOR(AVG(edad)) |
+------------------+
|               34 |
+------------------+
1 row in set (0.006 sec)

SELECT CEIL(AVG(edad)) FROM clientes;
+-----------------+
| CEIL(AVG(edad)) |
+-----------------+
|              35 |
+-----------------+
1 row in set (0.000 sec)

SELECT * FROM clientes;
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