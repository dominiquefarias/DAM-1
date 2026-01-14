Para comenzar establecí la estructura básica del documento en html y configuré el idioma a español despues en la sección del head me aseguré de inclui lo de meta charset que es para que todos los datos se cargen bien, le añadi un titulo y le puse un viewport para que la pagina sea responsive para los distintos dispositivos por los que se ingresa asi como tambien utilice apis de google para las fuentes de la pagina además conecte una hoja de estilos css que esta en otra carpeta 
```html
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro - Mi Biblioteca Personal</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/estilo.css">
</head>
```
Dentro del cuerpo de la página creé un contenedor principa que agrupa todos los elementos que estaran dentro de el en la parte de arriba de la pagina con el logo y sobre todo es para mantener el diseño centrado y organizado asi que inserté la imagen de Mi Biblioteca Personal 
```html
<body>
    <div class="main-container">
        <div class="logo-container">
            <img src="assets/img/logo.png" alt="Mi Biblioteca Personal Logo" class="logo">
        </div>
```
Justo debajo del logo añadí una sección con el título "Crear Cuenta" nuestra intención aquí es que el usuario sepa inmediatamente en qué parte del sistema se encuentra en este caso, le estamos indicando que esta es la pantalla para registrarse y crear una nueva cuenta.
```html
        <div class="title-container">
            <h1>Crear Cuenta</h1>
        </div>
```
Dentro del contenedor principal, añadí un formulario de registro con campos para el nombre completo, el nombre de usuario, el correo electrónico y la contraseña. Cada campo tiene un atributo "required" para asegurar que el usuario complete todos los campos antes de enviar el formulario.
```html
        <form action="php/register.php" method="POST" class="login-form">
            <input type="text" name="nombre_completo" placeholder="Nombre Completo..." required>
            <input type="text" name="usuario" placeholder="Usuario..." required>
            <input type="email" name="email" placeholder="Correo..." required>
            <input type="password" name="contrasena" placeholder="Contraseña..." required>

            <button type="submit">Registrarse</button>
        </form>
```
Justo debajo del formulario añadimos un enlace que redirige al usuario a la página de inicio de sesión este enlace se encuentra dentro de un contenedor de pie de página para mantener la consistencia visual y la organización del diseño
```html
        <div class="footer-link">
            <a href="index.php">¿Ya tienes cuenta? Inicia sesión</a>
        </div>
    </div>
</body>

</html>
```

En general esta pagina es para que el usuario pueda registrarse en el sistema y crear una cuenta nuevatola pagina se conecta con unos archivos que estan en php que son para poder crea su cuenta iniciar sesion 