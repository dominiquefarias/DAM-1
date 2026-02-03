<!doctype html>
<html lang="es">

<head>
    <title>Camaron viviendas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/style1.css">
</head>

<body>
    <header>
        <h1>Camarón viviendas</h1>
    </header>
    <nav>
        <form action="?" method="POST">
            <select name="localidad">
                <option>Selecciona una localidad...</option>
                <option value="Valencia">Valencia</option>
                <option value="Alboraya">Alboraya</option>
                <option value="Torrent">Torrent</option>
                <option value="Gandía">Gandía</option>
                <option value="Sagunto">Sagunto</option>
                <option value="Paterna">Paterna</option>
                <option value="Burjassot">Burjassot</option>
                <option value="Xàtiva">Xàtiva</option>
                <option value="Cullera">Cullera</option>
            </select>
            <input type="number" name="precio_minimo" value=0 min=0>
            <input type="number" name="precio_maximo" value=1000000000 min=0>
            <input type="submit">
        </form>
    </nav>
    <main>
        <section>
            <?php
            $host = "localhost";
            $user = "camaron";
            $pass = "Camaron123$";
            $db = "camaron";

            $conexion = new mysqli($host, $user, $pass, $db);
            $resultado = $conexion->query("
            SELECT * FROM viviendas 
            WHERE 
            localidad LIKE '%" . $_POST['localidad'] . "%'
            AND precio > " . $_POST['precio_minimo'] . "
            AND precio < " . $_POST['precio_maximo'] . "
            ;
          ");
            while ($fila = $resultado->fetch_assoc()) {
                echo '
            	<article>
              	<h3>' . $fila['localidad'] . '</h3>
                <p>' . $fila['precio'] . '</p>
                <p>' . $fila['metroscuadrados'] . '</p>
                <p>' . $fila['aniodeconstruccion'] . '</p>
                <p>' . $fila['direccion'] . '</p>
                <p>' . $fila['altura'] . '</p>
                <p>' . $fila['tipodevivienda'] . '</p>
                <p>' . $fila['descripcion'] . '</p>
                <p>' . $fila['estado'] . '</p>
                <p>' . $fila['banios'] . '</p>
                <p>' . $fila['habitaciones'] . '</p>
                <p>' . $fila['teniente'] . '</p>
              </article>
            ';
            }
            ?>
        </section>
    </main>
    <footer>(c) Dominique Farías</footer>
</body>

</html>