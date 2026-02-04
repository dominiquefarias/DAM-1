<!doctype html>
<html lang="es">

<head>
    <title>Camaron viviendas</title>
    <meta charset="utf-8">
</head>

<body>
    <header>
        <h1>Viviendas</h1>
    </header>
    <style>
        /* Configuración General */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            margin: 0;
            padding: 0;
        }

        /* Encabezado */
        header {
            background-color: #633d63ff;
            /* Azul elegante */
            color: white;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        header h1 {
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        /* Navegación y Formulario */
        nav {
            background: white;
            padding: 1.5rem;
            display: flex;
            justify-content: center;
            border-bottom: 3px solid #d4af37;
            /* Dorado */
        }

        nav form {
            display: flex;
            gap: 10px;
            align-items: center;
        }

        select,
        input[type="submit"] {
            padding: 10px 15px;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 1rem;
        }

        input[type="submit"] {
            background-color: #1a3a5d;
            color: white;
            border: none;
            cursor: pointer;
            transition: background 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #d4af37;
        }

        /* Contenedor de Viviendas */
        main section {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 25px;
            padding: 40px;
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Tarjeta de Vivienda (Article) */
        article {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            padding: 20px;
            border-top: 5px solid #1a3a5d;
        }

        article:hover {
            transform: translateY(-5px);
        }

        article h3 {
            margin-top: 0;
            color: #1a3a5d;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }

        /* Estilo para los datos de la vivienda */
        article p {
            margin: 8px 0;
            font-size: 0.95rem;
            line-height: 1.4;
        }

        /* Destacar el precio */
        article p:nth-child(2) {
            font-size: 1.4rem;
            font-weight: bold;
            color: #2c7a7b;
            margin-bottom: 15px;
        }

        article p:nth-child(2)::after {
            content: " €";
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 2rem;
            background: #333;
            color: #ccc;
            margin-top: 40px;
            font-size: 0.8rem;
        }
    </style>
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
            SELECT * FROM viviendas WHERE localidad = '" . $_POST['localidad'] . "';
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
    <footer>(c) 2026 Dominique Farías</footer>
</body>

</html>