En este ejercicio voy a trabajar con las edades de la tabla clientes para practicar la precisión en los cálculos primero usaré SQL para calcular el promedio de edad pero probaré tres formas distintas de redondear el resultado al más cercano, hacia abajo y hacia arriba para ver cómo cambian las cifras finalmente tomaré la lista completa de edades y utilizaré un programa de Python con matplotlib para crear un gráfico de pastel lo que me ayudará a ver los datos en lugar de solo ver números en una tabla

---

Primero comienzo entrando a la base de datos clientes
```
USE clientes;
```

Ahora voy a calcular el promedio redondeado al entero más cercano
```
SELECT ROUND(AVG(edad)) FROM clientes;
```
Y el resultado es:
```
+------------------+
| ROUND(AVG(edad)) |
+------------------+
|               34 |
+------------------+
1 row in set (0.006 sec)
```

Ahora voy a calcular el promedio redondeado hacia abajo al entero más cercano
```
SELECT FLOOR(AVG(edad)) FROM clientes;
```
Y el resultado es:
```
+------------------+
| FLOOR(AVG(edad)) |
+------------------+
|               34 |
+------------------+
1 row in set (0.006 sec)
```

Ahora voy a calcular la promedio redondeado hacia arriba al entero más cercano
```
SELECT CEIL(AVG(edad)) FROM clientes;
```
Y el resultado es:
```
+-----------------+
| CEIL(AVG(edad)) |
+-----------------+
|              35 |
+-----------------+
1 row in set (0.000 sec)
```

Ahora voy a mostrar todos los clientes
```
SELECT * FROM clientes;
```
Y el resultado es:
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
10 rows in set (0.006 sec)
```

Ahora voy a mostrar un grafico de torta de la edad de los clientes
```
import matplotlib.pyplot as pt

data = [28, 34, 45, 22, 56, 31, 40, 29, 37, 19]

pt.pie(data)
pt.show()
```

---

En conclusión este ejercicio integra el procesamiento numérico en base de datos con la visualización gráfica en programación en la fase de SQL he comprobado la importancia de las funciones escalares ROUND, FLOOR, CEIL para normalizar los resultados de funciones de agregación como AVG permitiendome controlar exactamente cómo se manejan los decimales finalmente la implementación de matplotlib en Python demuestra cómo los datos brutos pueden transformarse en información visual facilitando la interpretación rápida de la distribución en un grafico de los clientes