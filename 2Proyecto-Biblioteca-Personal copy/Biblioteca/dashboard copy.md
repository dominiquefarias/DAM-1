Lo primero es verificar si la variable de sesión loggedin existe y es verdadera si esta no lo es significaria que alguien intenta entrar sin iniciar sesion y los redirijo automáticamente al index.php. Si todo está bien se guarda el nombre del usuario en una variable 
```php
<?php
session_start();

// por seguridad se verifica que la variable de sesión loggedin existe y es verdadera
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header("Location: index.php");
    exit;
}
// se guarda el nombre del usuario en una variable
$nombre_usuario = htmlspecialchars($_SESSION['nombre']);
?>
```
En esta parte vuelvo a importar la fuente Quicksand y mi hoja de estilos general estilo.css para mantener la linea visual con la página de login
```html
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Mi Biblioteca Personal</title>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/estilo.css">
```
Dentro de la sección de estilos defino la apariencia de los dos enlaces principales que son "Ir a mi biblioteca" y "Cerrar Sesión" al enlace para 'Ir a mi biblioteca' le doy un color violeta oscuro para resaltar la acción positiva mientras que al enlace de 'Cerrar Sesión' le asigno un color rojo para indicar que es una acción de salida o precaución
```html
    <style>
        .welcome-container {
            font-family: 'Quicksand', sans-serif;
            /* Aplicamos la letra del estilo */
            text-align: center;
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: 50px auto;
        }

        .welcome-container h1 {
            color: #333;
            font-weight: 700;
        }

        .welcome-container p {
            color: #666;
            font-weight: 400;
        }

        .logout-link {
            color: #ff4d4d;
            text-decoration: none;
            font-weight: 700;
            display: inline-block;
            margin-top: 20px;
        }
         .login-biblioteca {
            color: #4d0955ff;
            text-decoration: none;
            font-weight: 700;
            display: inline-block;
            margin-top: 20px;
        }
    </style>
</head>
```
En esta parte de la pagina utilizo PHP echo $nombre_usuario para insertar el nombre de la persona que inició sesión esto crea una experiencia personalizada ya que como la base de datos puede reconocer al usuario por el numero de idconfirmándole al usuario que el sistema lo ha reconocido.
Con esto el usuario puede hacer clic en Ir a mi biblioteca para dirigirse a feed.php que es donde se encuentra el contenido principal o puede elegir cerrar su sesión a través de php/logout.php
```html
<body>
    <div class="main-container">
        <div class="logo-container">
            <img src="assets/img/logo.png" alt="Logo" class="logo">
        </div>

        <div class="welcome-container">
            <h1>¡Hola, <?php echo $nombre_usuario; ?>!</h1>
            <p>Tu contraseña es correcta. Bienvenido a tu biblioteca.</p>
            <a href="feed.php" class="login-biblioteca">Ir a mi biblioteca</a>
            <p>o</p>
            <a href="php/logout.php" class="logout-link">Cerrar Sesión</a>
        </div>
    </div>
</body>

</html>
```