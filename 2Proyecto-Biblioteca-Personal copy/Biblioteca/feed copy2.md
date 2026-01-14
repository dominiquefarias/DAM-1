Aquí tienes el código de tu archivo `feed.php` (tu biblioteca principal) dividido en secciones lógicas, con la explicación redactada en primera persona para que puedas presentarla con seguridad.

### 1. Inicio de sesión y Verificación de Seguridad

```php
<?php
// 1. INICIAR SESIÓN
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// 2. VERIFICAR LOGIN (Seguridad)
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header("Location: index.php");
    exit;
}

include "includes/config.php";

```

> "Lo primero que hago es asegurar el entorno. Inicio la sesión de PHP si no ha arrancado aún y verifico inmediatamente si el usuario está logueado. Si alguien intenta entrar aquí directamente sin haber pasado por el login, lo expulso redirigiéndolo al `index.php`. Una vez seguro, incluyo mi archivo de configuración para conectar a la base de datos."

---

### 2. Identificación del Usuario

```php
// 3. OBTENER ID DEL USUARIO ACTUAL
// Ya no hay redirección. Seas quien seas (ID 1, 2 o 50), verás tus libros.
if (isset($_SESSION['id'])) {
    $usuario_id = $_SESSION['id'];
} else {
    // Fallback por seguridad si la sesión 'id' no está definida
    $usuario_id = 1; 
}

```

> "Aquí determino quién es el dueño de la biblioteca que vamos a mostrar. Tomo el ID del usuario guardado en la sesión. Puse un pequeño respaldo (fallback) que asigna el ID 1 en caso de emergencia, para evitar que el código falle si por alguna razón extraña la sesión pierde el ID, aunque en un flujo normal siempre debería existir."

---

### 3. Lógica para Eliminar un Libro

```php
// --- LOGICA DE ELIMINAR ---
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['delete_id'])) {
    $id_libro_eliminar = intval($_POST['delete_id']);
    
    // PASO A: Eliminar imagen física (Opcional)
    $stmt_img = $conexion->prepare("SELECT portada FROM Libros WHERE id_libro = ?");
    $stmt_img->bind_param("i", $id_libro_eliminar);
    $stmt_img->execute();
    $res_img = $stmt_img->get_result();
    if ($fila = $res_img->fetch_assoc()) {
        $ruta_imagen = $fila['portada'];
        if (!empty($ruta_imagen) && file_exists($ruta_imagen)) {
            unlink($ruta_imagen);
        }
    }
    $stmt_img->close();

    // PASO B: Eliminar de Coleccion
    $stmt_col = $conexion->prepare("DELETE FROM Coleccion WHERE id_libro = ?");
    $stmt_col->bind_param("i", $id_libro_eliminar);
    $stmt_col->execute();
    $stmt_col->close();

    // PASO C: Eliminar de Libros
    $stmt_libro = $conexion->prepare("DELETE FROM Libros WHERE id_libro = ?");
    $stmt_libro->bind_param("i", $id_libro_eliminar);
    
    if ($stmt_libro->execute()) {
        header("Location: feed.php");
        exit;
    }
    $stmt_libro->close();
}

```

> "Esta sección maneja la limpieza cuando decido borrar un libro. Es un proceso en tres pasos para no dejar 'basura' en el sistema: primero busco si el libro tiene una imagen de portada guardada y la borro del servidor. Luego, elimino el registro de mi 'Colección' personal y, finalmente, borro el libro de la base de datos general. Si todo sale bien, recargo la página para ver los cambios."

---

### 4. Consulta a la Base de Datos (Recuperar Libros)

```php
// --- CONSULTA DE LIBROS ---
$sql = "SELECT L.id_libro, L.titulo, L.portada, L.descripcion, 
               A.nombre AS autor, 
               C.estado, C.capitulo_actual, C.valoracion
        FROM Coleccion C
        JOIN Libros L ON C.id_libro = L.id_libro
        LEFT JOIN Autores A ON L.id_autor = A.id_autor
        WHERE C.id_usuario = ?
        ORDER BY C.fecha_agregado DESC";

$stmt = $conexion->prepare($sql);
$stmt->bind_param("i", $usuario_id);
$stmt->execute();
$result = $stmt->get_result();
$libros = [];
while ($row = $result->fetch_assoc()) {
    $libros[] = $row;
}
$stmt->close();
?>

```

> "Aquí preparo los datos para mostrarlos. Hago una consulta SQL compleja usando `JOIN` para unir tres tablas: la Colección (mis datos personales), los Libros (datos generales) y los Autores. Filtro solo por mi ID de usuario y los ordeno para ver primero los que agregué más recientemente. Guardo todo en un array `$libros` para usarlo más tarde en el HTML."

---

### 5. Estilos y Estructura Visual (CSS)

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Biblioteca Personal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #fffbef; /* Tono crema suave */
            /* ... otros estilos generales ... */
        }
        /* ... Estilos de tarjetas, grid y botones ... */
        .card-deseado { background-color: #fff59d !important; }
        .card-leyendo { background-color: #ffbbf1 !important; }
        .card-leido   { background-color: #e1bee7 !important; }
    </style>
</head>

```

> "En la cabecera, importo Tailwind CSS para utilidades rápidas y la fuente 'Inter'. En mis estilos personalizados, definí un color de fondo crema (`#fffbef`) para dar esa sensación cálida. También creé clases específicas (`.card-deseado`, `.card-leyendo`, etc.) para que cada libro tenga un color de fondo distinto según su estado, facilitando identificar visualmente qué estoy leyendo."

---

### 6. Encabezado y Barra de Navegación

```html
<body>

    <div class="custom-header">
        <div class="logo-area">
            <img src="assets/img/logo.png" alt="Logo" class="logo">
            <h1 class="text-xl md:text-2xl font-bold tracking-tight m-0">Mi Biblioteca</h1>
        </div>
        
        <div class="flex items-center gap-4">
            <a href="php/logout.php" class="text-red-500 font-semibold hover:text-red-700 text-sm md:text-base no-underline">
                Cerrar sesión
            </a>
        </div>
    </div>

```

> "Diseñé un encabezado limpio y redondeado que contiene mi logo y el título de la aplicación. A la derecha, coloqué un enlace visible en rojo para cerrar sesión, asegurándome de que sea accesible pero diferenciado del resto del contenido."

---

### 7. Botón de "Añadir" y Rejilla de Contenido

```html
    <div style="max-width: 1000px; margin: 0 auto;">
        
        <div class="flex justify-end pr-4">
            <a href="nuevo_libro.php" class="btn-add shadow-md">
                + Añadir libro
            </a>
        </div>

        <div class="library-grid">
            
            <?php if (empty($libros)): ?>
                <div class="col-span-full text-center py-10 text-gray-500 w-full" style="grid-column: 1 / -1;">
                    <p class="text-xl">Aún no tienes libros en tu colección.</p>
                </div>

```

> "Antes de mostrar los libros, coloco un botón flotante verde para 'Añadir libro' que lleva al formulario de creación. Luego abro el contenedor `library-grid`. Si mi array de libros está vacío (porque soy nuevo o borré todo), muestro un mensaje amigable indicando que no hay libros, en lugar de dejar la pantalla en blanco."

---

### 8. El Bucle Principal y Lógica de Colores

```html
            <?php else: ?>
                <?php foreach ($libros as $libro): 
                    $bgClass = 'card-deseado'; 
                    if (strtolower($libro['estado']) === 'leyendo') $bgClass = 'card-leyendo';
                    if (strtolower($libro['estado']) === 'leido')   $bgClass = 'card-leido';
                    
                    $portada = !empty($libro['portada']) ? $libro['portada'] : 'https://via.placeholder.com/120x180?text=No+Cover';
                ?>

                <div class="card-wrapper">
                    <div class="book-card <?php echo $bgClass; ?>">
                        <img src="<?php echo htmlspecialchars($portada); ?>" alt="Portada" class="book-cover">

```

> "Aquí ocurre la magia visual. Itero sobre cada libro encontrado. Uso una lógica condicional en PHP para asignar una clase CSS específica (`$bgClass`) dependiendo de si el estado es 'leyendo', 'leído' o 'deseado'. Esto hace que las tarjetas se pinten automáticamente del color correcto. También verifico si hay portada; si no, pongo una imagen genérica por defecto."

---

### 9. Información del Libro y Estado

```html
                        <div class="book-info">
                            <div class="book-title"><?php echo htmlspecialchars($libro['titulo']); ?></div>
                            <div class="book-author"><?php echo htmlspecialchars($libro['autor']); ?></div>
                            
                            <div class="book-desc">
                                <?php echo htmlspecialchars($libro['descripcion']); ?>
                            </div>

                            <div class="status-badge">
                                <span><?php echo ucfirst(htmlspecialchars($libro['estado'])); ?></span>
                                
                                <?php if (strtolower($libro['estado']) === 'leyendo' && $libro['capitulo_actual']): ?>
                                    <span class="text-xs bg-black/10 px-2 py-1 rounded">Cap: <?php echo $libro['capitulo_actual']; ?></span>
                                <?php endif; ?>

```

> "Dentro de cada tarjeta, imprimo el título, el autor y la descripción, asegurándome de usar `htmlspecialchars` para evitar problemas de seguridad con texto extraño. Además, muestro una pequeña insignia con el estado del libro. Si estoy 'leyendo' el libro actualmente, añado dinámicamente el número de capítulo en el que voy."

---

### 10. Valoración y Botones de Acción

```html
                                <?php if (strtolower($libro['estado']) === 'leido'): ?>
                                    <div class="stars">
                                        <?php 
                                        $val = $libro['valoracion'] ? $libro['valoracion'] : 0;
                                        for($i=0; $i<5; $i++) {
                                            echo ($i < $val) ? '★' : '☆';
                                        }
                                        ?>
                                    </div>
                                <?php endif; ?>
                            </div>

                            <div class="action-buttons">
                                <a href="nuevo_libro.php?edit=<?php echo $libro['id_libro']; ?>" class="icon-btn" title="Editar">
                                    </a>
                                
                                <form method="POST" onsubmit="return confirm('¿Estás seguro...?');" style="margin:0;">
                                    <input type="hidden" name="delete_id" value="<?php echo $libro['id_libro']; ?>">
                                    <button type="submit" class="icon-btn" title="Eliminar">
                                        </button>
                                </form>
                            </div> 
                        </div> 
                    </div> 
                </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
    </div>
</body>
</html>

```

> "Para terminar la tarjeta, si el libro ya fue leído, genero un sistema de estrellas visual basado en mi valoración numérica (de 1 a 5). Finalmente, añado los botones de acción ocultos que aparecen al pasar el mouse: uno para editar (que recicla el formulario de `nuevo_libro.php`) y otro formulario pequeño para eliminar el libro, el cual pide confirmación antes de enviarse."