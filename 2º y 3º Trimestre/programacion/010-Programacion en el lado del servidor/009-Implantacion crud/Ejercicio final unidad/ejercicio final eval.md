En este ejercicio desarrollare una pequeña aplicación web dinámica llamada 'Domasa' la cual es para la gestión de noticias tecnológicas la estructura del sitio se basa en la modularidad: utilizare un archivo principal  de nombre index.php que actúa como contenedor y carga los diferentes componentes mediante la sentencia include el proyecto integra funcionalidades clave de un pequeño CRUD de lectura de datos con filtros de búsqueda SQL para las noticias, listado de registros únicos para los autores y un formulario HTML para la inserción de nueva información en la base de datos MySQL

---

Primero creo un archivo que se llama index.php que es para que se vea toda la informacion mediante ese archivo donde pongo un cuerpo basico que seria el siguiente:

```
<!doctype html>
<html lang="es">

<head>
    <title>Domasa - Noticias tecnológicas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/estilo.css">
</head>

<body>
    <header>
        <h1>Domasa</h1>
        <h2>Noticias tecnológicas</h2>
    </header>
    <main>
        <?php include "inc/listar_articulos.php"; ?>
    </main>
    <footer>
    </footer>
</body>

</html>
```

Luego creo un archivo que se llama noticias.php que es para que se vea la informacion a lista de noticias con opciones de filtrado donde podre utilizar tecnologías como PHP y MySQL para interactuar con la base de datos y mostrar los datos solicitados que se veria de esta manera:

```
<?php
include "inc/conexion.php";

// Lógica de filtrado
$filtro = "";
$whereSQL = "";

if (isset($_POST['buscar'])) {
    $filtro = $_POST['busqueda'];
    // Filtramos por título o contenido
    $whereSQL = "WHERE titulo LIKE '%$filtro%' OR contenido LIKE '%$filtro%'";
}

$sql = "SELECT * FROM noticias $whereSQL ORDER BY fecha_publicacion DESC";
$resultado = $conexion->query($sql);
?>

<div class="seccion-noticias">
    <h3>Listado de Noticias</h3>
    
    <form method="POST" action="index.php?seccion=noticias" class="filtro">
        <input type="text" name="busqueda" placeholder="Buscar noticia..." value="<?php echo $filtro; ?>">
        <input type="submit" name="buscar" value="Filtrar">
    </form>

    <div class="lista-articulos">
        <?php
        if ($resultado->num_rows > 0) {
            while ($fila = $resultado->fetch_assoc()) {
                echo '
                <article>
                    <h4>' . $fila['titulo'] . '</h4>
                    <time>' . $fila['fecha_publicacion'] . '</time>
                    <p>' . substr($fila['contenido'], 0, 100) . '...</p>
                </article>
                <hr>';
            }
        } else {
            echo "<p>No se encontraron noticias.</p>";
        }
        ?>
    </div>
</div>
```

Luego en otro archivo llamado autores.php muestro una lista de autores y sus novelas donde creo un programa que interactua con la base de datos y php

```
<?php
include "inc/conexion.php";

$sql = "SELECT DISTINCT autor_id FROM noticias"; 


$resultado = $conexion->query($sql);
?>

<div class="seccion-autores">
    <h3>Nuestros Autores</h3>
    <ul>
    <?php
    while ($fila = $resultado->fetch_assoc()) {
        echo '<li>Autor: <strong>' . $fila['autor_id'] . '</strong></li>';
    }
    ?>
    </ul>
</div>
```
Luego creo otro archivo llamado formulario.php que es para que se vea la informacion a lista de noticias con opciones de filtrado donde podre utilizar tecnologías como PHP y MySQL para interactuar con la base de datos y mostrar los datos solicitados que se veria de esta manera:

```
<form action="inc/create/procesaformulario.php" method="POST">
    <div class="controlformulario">
        <label for="titulo">Título de la nueva noticia</label>
        <input type="text" name="titulo" id="titulo">
    </div>

    <div class="controlformulario">
        <label for="contenido">Contenido de la nueva noticia</label>
        <textarea id="contenido" name="contenido"></textarea>
    </div>

    <div class="controlformulario">
        <label for="fecha_publicacion">Fecha de la nueva noticia</label>
        <input type="text" name="fecha_publicacion" id="fecha_publicacion">
    </div>

    <div class="controlformulario">
        <label for="autor_id">Autor de la nueva noticia</label>
        <input type="text" name="autor_id" id="autor_id">
    </div>

    <input type="submit">

</form>
```

---

En conclusión en este ejercicio al utilizar la sentencia include en el archivo index.php, he logrado separar la estructura común de cabecera y pie de página del contenido variable esto es muy importante para el mantenimiento de la web si en el futuro necesito cambiar el diseño del menú solo tendré que modificar un archivo y el cambio se reflejará automáticamente en todas las secciones las cuales son Noticias, Autores, Formulario ahorrando tiempo y evitando errores
