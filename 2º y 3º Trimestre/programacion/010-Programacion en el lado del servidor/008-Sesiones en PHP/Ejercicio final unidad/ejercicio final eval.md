En este ejercicio he creado una pequeña aplicación web que utiliza sesiones para mantener datos entre páginas web la persistencia de datos entre páginas por defecto en el protocolo HTTP no tiene como una memoria lo que significa que las variables creadas en un archivo desaparecen al navegar a otro y para solucionar eso utilizare las sesiones de PHP y comparare qué ocurre al intentar pasar una variable normal frente al uso de session_start() y la superglobal $_SESSION, lo que nos permitirá mantener la información del usuario accesible mientras navegamos por el sitio.

---
Primero abro el archivo 003-origen.php en el cual tengo el siguiente codigo:
```
<?php
$nombre = "Dominique";
?>
<a href="004-destino.php">Vamos a otra página</a>
```
Despues abro el archivo 004-destino.php en el cual tengo el siguiente codigo:
```
<?php
echo $nombre;
?>
```
Luego se me pide abrir el archivo 005-destino con sesiones.php en el cual tengo el siguiente codigo:
```
<?php
session_start();
$nombre = $_SESSION['nombre'];
echo $nombre
?>
<a href="006-origen.php">Vamos a otra página</a>
```
Luego abro el archivo 006-origen.php en el cual tengo el siguiente codigo:
```
<?php
session_start();
$nombre = $_SESSION['nombre'];
echo $nombre;
?>
<a href="005-destino con sesiones.php">Vamos a otra página</a>
```
En lo que cambio de las paginas puedo ver el nombre que he puesto y puedo ir cambiando de pagina 

---

Como conclusión he aprendido cómo las aplicaciones web consiguen recordar al usuario mientras que en el primer ejemplo la conexión entre páginas estaba "rota" ya que el dato desaparecía en el segundo ejemplo logré crear una navegación fluida gracias a las sesiones he podido moverme de un archivo a otro manteniendo mi nombre visible lo cual es el principio básico que utilizan las webs para mantenernos logueados mientras navegamos por su contenido