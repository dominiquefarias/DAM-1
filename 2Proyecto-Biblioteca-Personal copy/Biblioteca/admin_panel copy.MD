
Primeo comienzo la "sesion" utilizando la funcion "session_start()" para poder leer todo lo que se guardo en la sesion.
luego utilizo un if para comprobar si el usuario que ha accedido es el administrador en este caso el administrador tiene el id=2 y si no es el administrador lo redirijo a otra vista que es index.php
En este caso el if tambien comprueba 3 cosas si existe la variable de sesión "loggedin" si el usuario está logueado y si el ID del usuario es 2 (ya que este es el id del administrador), si estas condiciones falla como dicho anteriormente este lo redirige a index.php

```PHP
session_start();

if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true || $_SESSION['id'] != 2) {
    header("Location: index.php");
    exit;
}

require_once 'includes/config.php';
```
Ahora utilizo $lista_tablas para guardar las tablas de la base de datos y con $sql_tablas guardo la consulta para mostrar las tablas ya que dice "SHOW TABLES" y con $result_tablas guardo la consulta para mostrar las tablas
```PHP
$lista_tablas = [];
$sql_tablas = "SHOW TABLES";
$result_tablas = $conexion->query($sql_tablas);

if ($result_tablas) {
    while ($row = $result_tablas->fetch_array()) {
        $lista_tablas[] = $row[0];
    }
}
```