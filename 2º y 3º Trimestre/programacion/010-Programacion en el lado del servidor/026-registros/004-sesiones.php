<?php
session_start();

$_SESSION['nombre'] = "Dominique";
$_SESSION['apellidos'] = "Farias Osorio";

foreach ($_SESSION as $clave => $valor) {
    echo $clave . ": " . $valor . "<br>";
}
?>