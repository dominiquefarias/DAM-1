<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Moderno</title>
    <style>
        /* 1. Estilos Generales */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 40px;
            color: #333;
        }

        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 40px;
        }

        /* 2. Contenedor Grid (Rejilla) */
        .blog-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsivo automático */
            gap: 25px;
            max-width: 1200px;
            margin: 0 auto;
        }

        /* 3. Diseño de la Tarjeta (Card) */
        .article-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            padding: 25px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            border-left: 5px solid #3498db; /* Un toque de color */
        }

        /* Efecto Hover */
        .article-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.12);
        }

        /* 4. Tipografía interna */
        .article-card h3 {
            margin-top: 0;
            color: #2c3e50;
            font-size: 1.5rem;
            margin-bottom: 10px;
        }

        .meta-info {
            font-size: 0.85rem;
            color: #7f8c8d;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }

        .content {
            line-height: 1.6;
            color: #555;
        }
    </style>
</head>
<body>

    <h1>Últimas Entradas</h1>

    <div class="blog-container">
        <?php
        // Configuración de la base de datos
        $host = "localhost";
        $user = "blogphp";
        $pass = "Blogphp123$";
        $db   = "blogphp";

        // Crear conexión con control de errores básico
        $conexion = new mysqli($host, $user, $pass, $db);

        // Verificar si hay error en la conexión
        if ($conexion->connect_error) {
            die("<p style='color:red; text-align:center'>Error de conexión: " . $conexion->connect_error . "</p>");
        }

        // Establecer charset a UTF-8 para evitar problemas con tildes/ñ
        $conexion->set_charset("utf8");

        $sql = "SELECT * FROM blog ORDER BY fecha DESC"; // Ordenado por fecha
        $resultado = $conexion->query($sql);

        if ($resultado->num_rows > 0) {
            while ($fila = $resultado->fetch_assoc()) {
                // IMPORTANTE: Usamos htmlspecialchars para seguridad (evitar XSS)
                $titulo = htmlspecialchars($fila['titulo']);
                $fecha = date("d/m/Y", strtotime($fila['fecha'])); // Formatear fecha
                $autor = htmlspecialchars($fila['autor']);
                $contenido = htmlspecialchars($fila['contenido']);

                // Si el contenido es muy largo, lo cortamos
                $resumen = (strlen($contenido) > 150) ? substr($contenido, 0, 150) . '...' : $contenido;

                echo '
                <article class="article-card">
                    <h3>' . $titulo . '</h3>
                    <div class="meta-info">
                        <time>📅 ' . $fecha . '</time>
                        <span>✍️ ' . $autor . '</span>
                    </div>
                    <p class="content">' . $resumen . '</p>
                </article>
                ';
            }
        } else {
            echo "<p style='text-align:center; width:100%'>No hay entradas en el blog aún.</p>";
        }

        $conexion->close();
        ?>
    </div>

</body>
</html>
