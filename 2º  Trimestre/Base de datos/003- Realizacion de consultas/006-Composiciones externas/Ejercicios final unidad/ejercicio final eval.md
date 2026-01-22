
En este ejercicio voy a integrar una base de datos con una aplicación web en python utilizando flask y la plantilla jinja el objetivo es recuperar datos de una vista en la base de datos y presentarlos de manera estructurada en el navegador 

---

Primero comienzo configurando la base de datos y creando las tablas de alumno para alumnos, asignatura para asignaturas y matriculas para matriculas que son las necesarias para que el ejercicio funcione correctamente

```

CREATE DATABASE composiciones;

USE composiciones;

CREATE TABLE alumnos(
Identificador INT PRIMARY KEY,
nombre VARCHAR(100),
apellidos VARCHAR(100)
);

CREATE TABLE asignaturas(
Identificador INT PRIMARY KEY,
nombre VARCHAR(100),
id_profesor INT
);

CREATE TABLE matriculas(
Identificador INT PRIMARY KEY,
id_asignatura INT,
id_alumno INT
);

```

Ahora inserto datos de muestra para poder utilizarlos con información real

```

INSERT INTO alumnos (Identificador, nombre, apellidos) VALUES
(1,'Ana','García López'),
(2,'Luis','Martínez Pérez'),
(3,'María','Sánchez Ruiz');

INSERT INTO asignaturas (Identificador, nombre, id_profesor) VALUES
(1,'Matemáticas',1),
(2,'Lengua Española',2);

INSERT INTO matriculas (Identificador, id_asignatura, id_alumno) VALUES
(1,1,1),
(2,1,2),
(3,1,3);

```

Ahora creo una vista llamada matriculas_join para que cuente con una vista que me permita simplificar las consultas desde la aplicación es decir que estas consultas me permitan obtener los datos de la base de datos de manera más eficiente
```

CREATE VIEW matriculas_join AS
SELECT
asignaturas.nombre AS "Nombre de la asignatura",
alumnos.nombre AS "Nombre del alumno",
alumnos.apellidos AS "Apellidos del alumno"
FROM matriculas
LEFT JOIN asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;

```

Ahora hago la aplicacion en python donde me conecto a la base de datos utilizando sql y recupero los datos de la vista para mostrarlos en el navegador

```

import mysql.connector
from flask import Flask,render_template

conexion = mysql.connector.connect(
host="localhost",
user="composiciones",
password="Compo123$Segura",
database="composiciones"
)

app = Flask(**name**)
@app.route("/")
def inicio():
cursor = conexion.cursor(dictionary=True)
cursor.execute("SELECT * FROM matriculas_join;")

filas = cursor.fetchall()
return render_template("index.html",datos=filas)

```

Finalmente utilizo la plantilla html utilizando un bucle for para recorrer los datos y mostrarlos en tarjetas


```
<main>
  <section>
    {% for linea in datos:%}
    	<article>
        <div class="imagen">
        	<img src="static/josevicente.jpg">
        </div>
        <div class="texto">
          <p>Asignatura: {{linea['Nombre de la asignatura']}}</p>
          <p>Nombre: {{linea['Nombre del alumno']}}</p>
          <p>Apellidos: {{linea['Apellidos del alumno']}}</p>
        </div>
      </article>
    {% endfor %}
  </section>    
</main>

```

---

En conclusión este ejercicio me permite mostrar contenido proveniente de una base de datos relacional manteniendo el código organizado la vista en sql hace mas facil la consulta desde python facilita la visualización de los datos sobre los resultados obtenidos

