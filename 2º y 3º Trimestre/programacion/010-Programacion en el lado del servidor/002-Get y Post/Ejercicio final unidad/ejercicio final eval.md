En esta ejercicio primero haré un formulario que manda mi nombre usando GET para ver cómo aparece escrito en la dirección web del navegador luego cambiaré al método POST para que la misma página procese el dato sin mostrarlo en la URL entendiendo así cómo se maneja la información de forma más limpia

---

Primero creare un formulario en html con un input de texto y un boton de submit y que envíe datos al servidor usando el método GET
````
<!DOCTYPE html>
<html>

<head>
    <title>Formulario</title>
</head>

<body>
    <form action="004-dos parametros get.php" method="GET">
        <p>Introduce tu nombre</p>
        <input type="text" name="nombre">
        <input type="submit">
    </form>
</body>

</html>
```
Ahora creare un archivo php que reciba los datos del formulario y los muestre en la pantalla
```
<?php
  echo $_GET['nombre'];
?>
```
Luego creare un formulario html que reciba dos parámetros y los muestre en la pantalla que envíe datos al servidor usando el método POST
```
<!DOCTYPE html>
<html>

<head>
    <title>Formulario</title>
</head>

<body>
    <form action="?" method="POST">
        <p>Introduce tu nombre</p>
        <input type="text" name="nombre">
        <input type="submit">
    </form>
</body>

</html>
```
Ahora creare un archivo php que reciba los datos del formulario y los muestre en la pantalla
```
<?php
  echo $_POST['nombre'];
?>
```

---

En conclusión he aprendido a manipular las variables superglobales de PHP este ejercicio demuestra que PHP clasifica automáticamente la información entrante: si el formulario usa el metodo GET  llena el array asociativo, y si usa el metodo POST llena entender esta distinción es fundamental para el desarrollo backend ya que nos obliga a saber de antemano cómo va a enviar los datos el cliente para poder capturarlos correctamente en el servidor