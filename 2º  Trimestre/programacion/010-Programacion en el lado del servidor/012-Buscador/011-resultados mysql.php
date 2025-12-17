<!doctype html>
<html lang="es">

<head>
    <title>Satori</title>
    <meta charset="utf-8">
    <link rel="icon" href="satorilogo.png">
    <style>
        body,
        html {
            padding: 0px;
            margin: 0px;
            font-family: sans-serif;
        }

        header {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            padding: 20px;
        }

        main {
            margin: auto;
            width: 800px;
        }

        article {
            border-bottom: 1px solid lightgray;
            margin: 20px;
            padding: 20px;
        }

        h1,
        h2,
        h3 {
            padding: 0px;
            margin: 0px;
        }

        a {
            font-size: 10px;
        }

        input {
            border: 1px solid lightgrey;
            padding: 10px;
            s border-radius: 20px;
        }

        h1 {
            font-size: 40px;
            display: inline-block;
            vertical-align: middle;
        }

        header img {
            height: 50px;
            width: auto;
            vertical-align: top;
        }
    </style>
</head>

<body>

    <header>
        <nav>
            <a href="011-resultados mysql.php" class="nav-brand">
                <img src="satorilogo.png" alt="Logo" class="nav-logo">
            </a>
        </nav>
        <h1>Satori</h1>
        <form method="POST" action="?">
            <input type="text" name="criterio" placeholder="Introduce algo para buscar...">
        </form>
    </header>

    <main>
        <?php
        // 1. Abrimos el IF. Todo lo que pase aquí dentro solo ocurrirá si se ha pulsado buscar.
        if (isset($_POST['criterio'])) {

            echo "<p>Resultados para: <strong>" . $_POST['criterio'] . "</strong></p>";

            $host = "localhost";
            $user = "satori";
            $pass = "Satori123$";
            $db = "satori";

            // Usamos @ para ocultar errores de conexión feos si fallan las credenciales
            $conexion = new mysqli($host, $user, $pass, $db);

            if ($conexion->connect_error) {
                die("Error de conexión: " . $conexion->connect_error);
            }

            // IMPORTANTE: Evitar inyección SQL básica (seguridad mínima)
            $busqueda = $conexion->real_escape_string($_POST['criterio']);

            $resultado = $conexion->query("
              SELECT * FROM paginas WHERE titulo LIKE '%$busqueda%';
            ");

            // Si hay resultados, los mostramos
            if ($resultado->num_rows > 0) {
                while ($fila = $resultado->fetch_assoc()) { ?>
                    <article>
                        <h2><?= $fila['titulo'] ?></h2>
                        <a href="<?= $fila['url'] ?>"><?= $fila['url'] ?></a>
                        <p><?= $fila['descripcion'] ?? '' // Añade descripción si la tienes en la BD ?></p>
                    </article>
                <?php }
            } else {
                echo "<p>No se encontraron resultados para tu búsqueda.</p>";
            }

        } // <--- 2. AQUÍ es donde debes cerrar el IF principal
        ?>
    </main>
</body>

</html>