<?php

$cliente = [
    "nombre" => "Dominique",
    "apellidos" => "Farías Osorio",
    "email" => "domi@mail.com"
];

foreach ($cliente as $clave => $valor) {
    echo "<label>" . $clave . "</label>";
    echo "<input type='text' value='" . $valor . "'>";
}


?>