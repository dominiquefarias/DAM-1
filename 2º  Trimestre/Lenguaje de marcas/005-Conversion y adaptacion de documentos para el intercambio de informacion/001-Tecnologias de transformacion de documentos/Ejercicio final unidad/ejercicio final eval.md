En este ejercicio voy a conectar una base de datos con php para mostrar los datos en una pagina web. Este proceso aunque se puede hacer con html y css, es un proceso que se puede hacer con php y mysql.

---

Primero creo una base de datos y ha esta tabla le añado datos sobre el blog

```sql
CREATE DATABASE proyecto;
USE proyecto;

CREATE TABLE blog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    fecha DATE,
    autor VARCHAR(255),
    contenido TEXT
);

INSERT INTO blog (titulo, fecha, autor, contenido) VALUES 
('Mi primer post', '2023-01-01', 'Juan', 'Este es el contenido del primer post'),
('Aprendiendo PHP', '2023-01-02', 'Maria', 'PHP es un lenguaje muy interesante para backend'),
('Conexión a MySQL', '2023-01-03', 'Pedro', 'Hoy aprendimos a conectar PHP con MySQL');

```

Luego a esta base de datos le creo un usuario para masa adelante conectarlo con alguna pagina web

```sql
CREATE USER 'proyecto'@'localhost' IDENTIFIED BY 'proyecto';
GRANT ALL PRIVILEGES ON proyecto.* TO 'proyecto'@'localhost';
FLUSH PRIVILEGES;

```

Ahora conectamos a php con la base de datos donde hara una consulta y mostrara los datos en una pagina web

```php
<?php
    // Defino las credenciales de conexión
    $host = "localhost";
    $user = "proyecto";
    $pass = "proyecto";
    $db = "proyecto";

    $sql = "SELECT * FROM blog";
    $resultado = $conexion->query($sql);
    while($fila = $resultado->fetch_assoc()){
        echo '<article>';
        echo '<h3>'.$fila['titulo'].'</h3>';
        echo '<time>'.$fila['fecha'].'</time>';
        echo '<p>'.$fila['autor'].'</p>';
        echo '<p>'.$fila['contenido'].'</p>';
        echo '</article>';
    }
    $conexion->close();
?>

```

---

En conclusion he logrado conectarme desde php a una base de datos y mostrar los datos en una pagina web aparte he aprendido que es fundamental crear un usuario específico para proteger la base de datos