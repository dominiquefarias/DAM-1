
---

Primero selecciono la base de datos clientes

```
USE clientes;
```

Ahora hago una consulta que muestre los nombres y apellidos de los clientes junto con su edad incrementada en 500 años

```
SELECT nombre, apellido, edad + 500 FROM clientes;
```

Que se veria asi:

```
+--------+----------------------+------------+
| nombre | apellidos            | edad + 500 |
+--------+----------------------+------------+
| Juan   | Pérez García         |        528 |
| María  | López Rodríguez      |        534 |
| Carlos | González Sánchez     |        545 |
| Ana    | Martínez Fernández   |        522 |
| Luis   | Ramírez Torres       |        556 |
| Sofía  | Hernández Díaz       |        531 |
| Miguel | Torres Ruiz          |        540 |
| Elena  | Flores Morales       |        529 |
| David  | Castillo Romero      |        537 |
| Laura  | Vargas Ortiz         |        519 |
+--------+----------------------+------------+
10 rows in set (0.001 sec)
```

Ahora realizo una consulta similar pero esta vez disminuye la edad en 500 años

```
SELECT nombre, apellido, edad - 500 FROM clientes;
```

Que se veria asi:

```
+--------+----------------------+------------+
| nombre | apellidos            | edad - 500 |
+--------+----------------------+------------+
| Juan   | Pérez García         |       -472 |
| María  | López Rodríguez      |       -466 |
| Carlos | González Sánchez     |       -455 |
| Ana    | Martínez Fernández   |       -478 |
| Luis   | Ramírez Torres       |       -444 |
| Sofía  | Hernández Díaz       |       -469 |
| Miguel | Torres Ruiz          |       -460 |
| Elena  | Flores Morales       |       -471 |
| David  | Castillo Romero      |       -463 |
| Laura  | Vargas Ortiz         |       -481 |
+--------+----------------------+------------+
10 rows in set (0.000 sec)
```

Ahora realizo una consulta que muestre los nombres y apellidos de los clientes junto con su edad multiplicada por 500

```
SELECT nombre, apellidos, edad * 500 FROM clientes;
```

Que se veria asi:

```
+--------+----------------------+------------+
| nombre | apellidos            | edad * 500 |
+--------+----------------------+------------+
| Juan   | Pérez García         |      14000 |
| María  | López Rodríguez      |      17000 |
| Carlos | González Sánchez     |      22500 |
| Ana    | Martínez Fernández   |      11000 |
| Luis   | Ramírez Torres       |      28000 |
| Sofía  | Hernández Díaz       |      15500 |
| Miguel | Torres Ruiz          |      20000 |
| Elena  | Flores Morales       |      14500 |
| David  | Castillo Romero      |      18500 |
| Laura  | Vargas Ortiz         |       9500 |
+--------+----------------------+------------+
10 rows in set (0.000 sec)
```

Ahora realizo una consulta que muestre los nombres y apellidos de los clientes junto con su edad dividida entre 500.

```
SELECT nombre, apellidos, edad / 500 FROM clientes;
```

Que se veria asi:

```
+--------+----------------------+------------+
| nombre | apellidos            | edad / 500 |
+--------+----------------------+------------+
| Juan   | Pérez García         |     0.0560 |
| María  | López Rodríguez      |     0.0680 |
| Carlos | González Sánchez     |     0.0900 |
| Ana    | Martínez Fernández   |     0.0440 |
| Luis   | Ramírez Torres       |     0.1120 |
| Sofía  | Hernández Díaz       |     0.0620 |
| Miguel | Torres Ruiz          |     0.0800 |
| Elena  | Flores Morales       |     0.0580 |
| David  | Castillo Romero      |     0.0740 |
| Laura  | Vargas Ortiz         |     0.0380 |
+--------+----------------------+------------+
10 rows in set (0.000 sec)
```

