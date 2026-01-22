
En este ejercicio voy a profundizar en el agrupamiento de registros y su visualización mediante python y sql el objetivo es analizar la tabla de productos desde tres perspectivas diferentes por categoría por color y por nivel de stock para esto conectaré Python con la base de datos ejecutaré consultas de agrupación y finalmente representaré los datos visualmente usando la librería matplotlib

---

Primero comienzo agrupando los productos por categoría para ver cuántos hay de cada tipo

```

SELECT
COUNT(categoria) AS numero,
categoria
FROM productos
GROUP BY categoria
ORDER BY numero DESC;

```
Y el resultado es:

```

+--------+-------------+
| numero | categoria   |
+--------+-------------+
|     10 | Ropa        |
|      8 | Tecnología  |
|      5 | Hogar       |
|      5 | Deportes    |
|      5 | Decoración  |
|      5 | Dormitorio  |
|      5 | Herramientas|
+--------+-------------+
7 rows in set (0.005 sec)

```
Ahora utilizo el siguiente código donde conecto python con la base de datos y ejecuto la consulta de agrupación para generar un gráfico de las categorías

```

import mysql.connector
import matplotlib.pyplot as pt

conexion = mysql.connector.connect(
host="localhost",

user="dominique3",

password="Domi123$",

database="portafolioexamen"

)

cursor = conexion.cursor()
cursor.execute('''
SELECT
COUNT(categoria) AS numero,
categoria
FROM productos
GROUP BY categoria
ORDER BY numero DESC;
''');

filas = cursor.fetchall()
cantidades = []
etiquetas = []
for fila in filas:
cantidades.append(fila[0])
etiquetas.append(fila[1])

pt.pie(cantidades, labels=etiquetas)
pt.show()

```

Ahora voy a agrupar los productos por color para analizar la distribución del inventario

```

SELECT
COUNT(color) AS numero,
color
FROM productos
GROUP BY color
ORDER BY numero DESC;

```
Y el resultado es:

```

+--------+---------+
| numero | color   |
+--------+---------+
|     12 | Negro   |
|      9 | Blanco  |
|      5 | Rojo    |
|      4 | Azul    |
|      4 | Gris    |
|      2 | Verde   |
|      2 | Marrón  |
|      1 | Plateado|
|      1 | Dorado  |
|      1 | Amarillo|
+--------+---------+
10 rows in set (0.004 sec)

```
Ahora utilizo Python para conectar con la base de datos y ejecutar la consulta de agrupación para visualizar estos colores en un gráfico

```

import mysql.connector
import matplotlib.pyplot as pt

conexion = mysql.connector.connect(
host="localhost",

user="dominique3",

password="Domi123$",

database="portafolioexamen"

)

cursor = conexion.cursor()
cursor.execute('''
SELECT
COUNT(color) AS numero,
color
FROM productos
GROUP BY color
ORDER BY numero DESC;
''');

filas = cursor.fetchall()
cantidades = []
etiquetas = []
for fila in filas:
cantidades.append(fila[0])
etiquetas.append(fila[1])

pt.pie(cantidades, labels=etiquetas)
pt.show()

```

Finalmente agrupo los productos por su nivel de stock para ver cuántos productos tienen la misma disponibilidad

```

SELECT
COUNT(stock) AS numero,
stock
FROM productos
GROUP BY stock
ORDER BY numero DESC;

```
Y el resultado en MySQL es:

```

+--------+-------+
| numero | stock |
+--------+-------+
|      3 |    20 |
|      3 |    25 |
|      3 |    15 |
|      2 |    10 |
|      2 |    30 |
|      2 |    40 |
|      2 |    60 |
|      1 |   100 |
|      1 |    50 |
+--------+-------+
15 rows in set (0.005 sec)

```
Ahora utilizo Python para conectar con la base de datos y ejecutar la consulta de agrupación para crear un gráfico de barras que represente esta distribución

```

import mysql.connector
import matplotlib.pyplot as pt

conexion = mysql.connector.connect(
host="localhost",

user="dominique3",

password="Domi123$",

database="portafolioexamen"

)

cursor = conexion.cursor()
cursor.execute('''
SELECT
COUNT(stock) AS numero,
stock
FROM productos
GROUP BY stock
ORDER BY numero DESC;
''');

filas = cursor.fetchall()
cantidades = []
etiquetas = []
for fila in filas:
cantidades.append(fila[0])
etiquetas.append(str(fila[1])) # Convierto a string para la etiqueta

pt.bar(etiquetas, cantidades)
pt.show()

```

---

En conclusión este ejercicio me ha permitido entender cómo el agrupamiento de registros mediante sql combinado con la visualización de datos en python es una herramienta fundamental para las empresas sobre todo dado que esta muestra graficos en base a los datos que estn en la base de datos y en el stock 

