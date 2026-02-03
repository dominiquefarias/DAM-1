<?php
if (isset($_POST['localidad'])) {
    $host = "localhost";
    $user = "camaron";
    $pass = "Camaron123$";
    $db = "camaron";

    $conexion = new mysqli($host, $user, $pass, $db);
    $resultado = $conexion->query('
  	INSERT INTO viviendas 
    VALUES(
    	NULL,
      "' . @$_POST['localidad'] . '",
      ' . @$_POST['precio'] . ',
      ' . @$_POST['metroscuadrados'] . ',
      ' . @$_POST['aniodeconstruccion'] . ',
      "' . @$_POST['direccion'] . '",
      ' . @$_POST['altura'] . ',
      "' . @$_POST['tipodevivienda'] . '",
      "' . @$_POST['descripcion'] . '",
      "' . @$_POST['estado'] . '",
      ' . @$_POST['banios'] . ',
      ' . @$_POST['habitaciones'] . ',
      "' . @$_POST['teniente'] . '"
    )
  ;
  ');
}
?>
<!doctype html>
<html>

<head>
    <link rel="stylesheet" href="css/style2.css">
</head>

<body>
    <nav>
        <a>Viviendas</a>
        <a>Imagenes</a>
        <a>Usuarios</a>
        <a>Propietarios</a>
        <a>Alquileres</a>
        <a>a</a>
        <a>b</a>
        <a>c</a>
        <a>d</a>
        <a>e</a>
    </nav>
    <main>
        <table>
            <thead>
                <tr>
                    <th>localidad</th>
                    <th>precio</th>
                    <th>metroscuadrados</th>
                    <th>aniodeconstruccion</th>
                    <!--
            <th>direccion</th>
            <th>altura</th>
            <th>tipodevivienda</th>
            <th>descripcion</th>
            <th>estado</th>
            <th>banios</th>
            <th>habitaciones</th>
            <th>teniente</th>
            -->
                </tr>
            </thead>
            <tbody>
                <?php
                $host = "localhost";
                $user = "camaron";
                $pass = "Camaron123$";
                $db = "camaron";

                $conexion = new mysqli($host, $user, $pass, $db);
                $resultado = $conexion->query("
              SELECT * FROM viviendas 
              ;
            ");
                while ($fila = $resultado->fetch_assoc()) {
                    echo '<tr>
              	<td>' . $fila['localidad'] . '</td>
                <td>' . $fila['precio'] . '</td>
                <td>' . $fila['metroscuadrados'] . '</td>
                <td>' . $fila['aniodeconstruccion'] . '</td>
                
              </tr>';
                    /*<td>'.$fila['direccion'].'</td>
                      <td>'.$fila['altura'].'</td>
                      <td>'.$fila['tipodevivienda'].'</td>
                      <td>'.$fila['descripcion'].'</td>
                      <td>'.$fila['estado'].'</td>
                      <td>'.$fila['banios'].'</td>
                      <td>'.$fila['habitaciones'].'</td>
                      <td>'.$fila['teniente'].'</td> */
                }
                ?>
            </tbody>
        </table>
        <form>
            <input name="localidad" placeholder="localidad">
            <input name="precio" placeholder="precio">
            <input name="metroscuadrados" placeholder="metroscuadrados">
            <input name="aniodeconstruccion" placeholder="año de construccion">
            <input name="direccion" placeholder="direccion">
            <input name="altura" placeholder="altura">
            <input name="tipodevivienda" placeholder="tipodevivienda">
            <input name="descripcion" placeholder="descripcion">
            <input name="estado" placeholder="estado">
            <input name="banios" placeholder="baños">
            <input name="habitaciones" placeholder="habitaciones">
            <input name="teniente" placeholder="teniente">
            <input type="submit">
        </form>
    </main>
</body>

</html>