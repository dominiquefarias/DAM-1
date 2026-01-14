Para comenzar ddefino con lo de siempre que voy a utilizar html asi como tambien indico que el idioma sera español también "configuro" el como se vera el contenido en dispositivos moviles y asigno el título que aparecerá en la pestaña del navegador identificando claramente mi aplicación
```html
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Biblioteca Personal</title>
```
En esta parte utilizo recursos externos los cuales son para la fuente de la pagina y el css que se encuentra en la carpeta assets/css/estilo.css
```html
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/estilo.css">
```
En esta parte incluimos un pequeño css ya que el css externo que tenemos en estilo.css no tiene el css para el error y se comparte con otra pagina que es register.html que tiene una funcion parecida a esta
```html
    <style>
        
        .error-message {
            color: #ff4d4d;
            font-family: 'Quicksand', sans-serif;
            font-weight: 600;
            font-size: 0.9em;
            margin-bottom: 15px;
            text-align: center;
        }
    </style>
</head>
```
Dentro del cuerpo de la página creé un contenedor principa que agrupa todos los elementos que estaran dentro de el en la parte de arriba de la pagina con el logo y sobre todo es para mantener el diseño centrado y organizado asi que inserté la imagen de Mi Biblioteca Personal 

```html
<body>
    <div class="main-container">
        <div class="logo-container">
            <img src="assets/img/logo.png" alt="Logo" class="logo">
        </div>
        <div class="title-container">
            <h1>Mi Biblioteca Personal</h1>
        </div>
```
Aquí creo el formulario funcional en este caso configuramos la etiqueta de formulario para que envíe los datos al archivo php/login.php usando el método POST lo cual es muy importante para proteger la contraseña ya que esta es la forma en que se envia los datos del formulario tambien incluyo los campos de entrada para el correo y la contraseña marcándolos como obligatorios con required para evitar que se envíe el formulario vacío
```html
        <form action="php/login.php" method="POST" class="login-form">
            <input type="email" name="email" placeholder="Correo..." required>
            <input type="password" name="contrasena" placeholder="Contraseña..." required>
```
Luego añadimos este bloque de código para comunicarnos con el usuario di el proceso de login falla devuelve un error aquí lo atrapamos y mostramos el mensaje específico correspondiente ya sea que la contraseña esté mal o que el correo no exista
```php
            <?php if (isset($_GET['error']) && $_GET['error'] == '1'): ?>
                <p class="error-message">Contraseña incorrecta, vuelve a intentarlo</p>
            <?php elseif (isset($_GET['error']) && $_GET['error'] == '2'): ?>
                <p class="error-message">El correo no existe o faltan datos</p>
            <?php endif; ?>
```
Finalmente colocamos el botón de envío para procesar el formulario y debajo de este, añadimos un enlace que lleva a la página de registro que seria register.html pensado para los usuarios nuevos que aún no tienen nada creado Con esto
```html
            <button type="submit">Iniciar sesión</button>
        </form>

        <div class="footer-link">
            <a href="register.html">Crear cuenta</a>
        </div>
    </div>

</body>

</html>
```