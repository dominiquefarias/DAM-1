En este ejercicio voy a realizar un ejercicio de exportación de datos, primero, organizaré los datos personales de un usuario nombre, apellidos, email dentro de un array en PHP usando claves para identificar cada dato. Una vez que la información esté estructurada, usaré la herramienta json_encode para traducirla a un formato de texto universal El objetivo final es generar un archivo .json en la carpeta data, simulando cómo una aplicación guardaría la información de un usuario para usarla después

---

Primero abro el archivo 004-array nombrado en php.php en el cual tengo el siguiente codigo el cual se me pide rellenar con los datos del cliente el cual relleno con lo siguiente:
```
<?php
  $cliente = [];
  $cliente['nombre'] = "Dominique";
  $cliente['apellidos'] = "Farias Osorio";
  $cliente['email'] = "domi@mail.com";
  
  var_dump($cliente);
?>
```
Despues se me pide utilizar la funcion ```json_encode()``` para convertir el array en un json el cual se veria de la siguiente manera:
```
{"nombre":"Dominique","apellidos":"Farias Osorio","email":"domi@mail.com"}
```
El contenido anterior lo guardo en un archivo llamado cliente.json el cual se encuentra en la carpeta data

---

Como conclusion he aprendido a estructurar y exportar información a diferencia de guardar datos en un archivo de texto plano donde se perdería el significado de qué es el nombre y qué es el email uso el de JSON mantiene la jerarquía de 'clave-valor' intacta esto significa que hemos guardado los datos personales del "usuario" de una forma organizada que garantiza que al leer el archivo en el futuro el ordenador sabrá distinguir perfectamente cada campo