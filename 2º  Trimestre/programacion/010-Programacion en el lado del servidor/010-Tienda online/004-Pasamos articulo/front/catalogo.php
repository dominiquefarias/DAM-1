<?php include "inc/cabecera.php"; ?>

<section id="catalogo">

    <?php
    $host = "localhost";
    $user = "tiendaonlinedamdaw";
    $pass = "Tiendaonlinedamdaw123$";
    $db = "tiendaonlinedamdaw";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM producto;";

    $resultado = $conexion->query($sql);
    while ($fila = $resultado->fetch_assoc()) {
        ?>
        <article>
            <div class="imagen"></div>
            <h3><?= $fila['nombre_producto'] ?></h3>
            <p><?= $fila['precio'] ?></p>
            <p><?= $fila['descripcion'] ?></p>
            <a href="comprar.php">Comprar</a>
        </article>
        <?php
    }

    $conexion->close();
    ?>

</section>

<style>
    #catalogo {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }

    #catalogo article {
        text-align: center;
    }

    #catalogo article .imagen {
        background: darkorchid;
        height: 200px;
        border-radius: 5px 5px 0px 0px;
    }
</style>

<?php include "inc/piedepagina.php"; ?>