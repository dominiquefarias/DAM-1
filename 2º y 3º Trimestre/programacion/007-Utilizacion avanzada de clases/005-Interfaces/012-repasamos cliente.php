<?php

$campos_cliente = [
    "nombre",
    "apellidos",
    "email",
    "telefono"
];

foreach ($campos_cliente as $campo) {
    echo $campo . "<br>";
}
// Ventajas del foreach: Es mas limpio
// Desventajas del foreach: En principio no está el índice
?>