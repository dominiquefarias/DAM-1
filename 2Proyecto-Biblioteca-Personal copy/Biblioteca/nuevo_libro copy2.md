Aquí tienes el desglose del código. He separado la lógica de PHP (backend), la estructura visual (HTML) y la interactividad (JavaScript), redactando cada explicación en primera persona para que puedas usarlo directamente en tu documentación o presentación.

---

### 1. Configuración y manejo de errores

```php
include "includes/config.php";

// Reportar errores para depuración
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

$usuario_actual_id = 1; 
$libro_editar = null;
$es_edicion = false;

```

**Explicación:**
Para comenzar, incluyo mi archivo de configuración para conectar con la base de datos. También activé el reporte estricto de errores de MySQL, lo cual es vital para detectar fallos durante el desarrollo. Además, inicializo variables clave: defino el ID del usuario (actualmente estático en 1 para pruebas) y preparo las variables `$libro_editar` y `$es_edicion` para controlar más adelante si estoy creando un libro nuevo o modificando uno existente.

---

### 2. Detección del modo edición

```php
// --- A. MODO EDICIÓN: CARGAR DATOS SI HAY ?edit=ID ---
if (isset($_GET['edit'])) {
    $id_edit = intval($_GET['edit']);
    
    // Consulta para rellenar el formulario
    $sql_edit = "SELECT L.*, ... WHERE L.id_libro = ? AND Col.id_usuario = ?";
    
    // ... (ejecución y obtención de datos)
    if ($fila = $res->fetch_assoc()) {
        $libro_editar = $fila;
        $es_edicion = true;
    }
    $stmt->close();
}

```

**Explicación:**
Aquí implementé la lógica para rellenar el formulario automáticamente. Verifico si la URL trae un parámetro `?edit=ID`. Si es así, hago una consulta compleja (usando `JOIN`) para traer toda la información del libro, incluyendo su autor, editorial y mi valoración personal. Si encuentro el libro, cambio la bandera `$es_edicion` a `true`, lo que modificará el comportamiento del formulario más adelante.

---

### 3. Procesamiento de datos (POST) y validación

```php
// --- B. GUARDAR DATOS (CUANDO PULSAS EL BOTÓN) ---
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $conexion->begin_transaction();

        // 1. Recoger datos
        $titulo = $_POST['titulo'];
        $autor_nombre = trim($_POST['autor']);
        // ... (resto de variables)
        
        // CORRECCIÓN DE ESTADO
        $estado_raw = $_POST['estado']; 
        $estado_db = 'Deseado'; // Default
        if ($estado_raw === 'leyendo') $estado_db = 'Leyendo';
        if ($estado_raw === 'leido')   $estado_db = 'Leido';

```

**Explicación:**
Esta es la sección que se activa cuando presiono "Guardar". Inicio una transacción de base de datos para asegurar que todas las operaciones se guarden correctamente o ninguna lo haga (evitando datos corruptos). Recojo y limpio todos los datos enviados por el usuario. También incluí un pequeño bloque lógico para normalizar el "estado" del libro, asegurándome de que lo que viene del formulario coincida exactamente con los valores permitidos en mi base de datos (`ENUM`).

---

### 4. Manejo de subida de imágenes

```php
        // 2. Imagen
        $ruta_portada = ($modo_edicion && isset($_POST['portada_actual'])) ? $_POST['portada_actual'] : null;
        if (isset($_FILES['portada']) && $_FILES['portada']['error'] === UPLOAD_ERR_OK) {
            $nombre_archivo = time() . "_" . basename($_FILES['portada']['name']);
            $directorio_destino = "uploads/";
            if (!is_dir($directorio_destino)) { mkdir($directorio_destino, 0777, true); }
            if (move_uploaded_file($_FILES['portada']['tmp_name'], $directorio_destino . $nombre_archivo)) {
                $ruta_portada = $directorio_destino . $nombre_archivo;
            }
        }

```

**Explicación:**
Para la portada del libro, he creado un sistema que verifica si el usuario subió una nueva imagen. Si es así, genero un nombre único usando la fecha actual (para evitar duplicados), creo la carpeta `uploads/` si no existe, y muevo el archivo allí. Si no se sube nada pero estoy editando, mantengo la ruta de la portada antigua para no perderla.

---

### 5. Normalización de datos (Autores y Editoriales)

```php
        // 3. Relaciones (Autor/Editorial/Categoria)
        function getIdByName($con, $table, $col_id, $col_name, $val) {
            // ... (Lógica de buscar o insertar)
            return $con->insert_id;
        }

        $id_autor = getIdByName($conexion, 'Autores', 'id_autor', 'nombre', $autor_nombre);
        // ... (llamadas para editorial y categoría)

```

**Explicación:**
Para mantener la base de datos optimizada y sin textos repetidos, escribí la función auxiliar `getIdByName`. Lo que hace es inteligente: primero busca si el autor (o editorial) ya existe. Si existe, me devuelve su ID. Si no existe, lo crea automáticamente y me devuelve el ID del nuevo registro. Esto me permite escribir nombres libremente en el formulario sin preocuparme por gestionar IDs manualmente.

---

### 6. Guardado en Base de Datos (SQL)

```php
        // 4. Guardar (Update o Insert)
        if ($modo_edicion) {
            // UPDATE: Actualizar tablas Libros y Coleccion
            $sql = "UPDATE Libros SET ... WHERE id_libro=?";
            // ...
        } else {
            // INSERT: Crear nuevo libro y entrada en Coleccion
            // ...
        }

        $conexion->commit();
        echo "<script>alert('$msg'); window.location.href='feed.php';</script>";

```

**Explicación:**
Aquí tomo la decisión final. Si estoy en modo edición, ejecuto sentencias `UPDATE` para modificar los datos existentes. Si es un libro nuevo, ejecuto `INSERT`. Es importante notar que actualizo dos tablas: `Libros` (datos generales) y `Coleccion` (mis datos personales como estado y valoración). Finalmente, hago `commit` para confirmar los cambios y redirijo al usuario al *feed* principal con un mensaje de éxito.

---

### 7. Interfaz Gráfica: Estructura y Estilos

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Estilos CSS personalizados para la tarjeta, inputs, animaciones, etc. */
        .book-card { ... }
        .image-preview-container { ... }
        /* ... */
    </style>
</head>

```

**Explicación:**
En la parte visual, estoy utilizando Tailwind CSS para utilidades rápidas, pero he añadido un bloque grande de CSS personalizado (`<style>`). Hice esto para darle una identidad única "tipo tarjeta" al formulario, con bordes redondeados, sombras suaves y una tipografía limpia (Inter). Definí estilos específicos para que la tarjeta se vea bien tanto en ordenadores como en móviles.

---

### 8. Formulario y Previsualización de Portada

```html
<body>
    <form action="nuevo_libro.php" method="POST" enctype="multipart/form-data" id="mainForm">
        <div class="book-card">
            <div class="book-image-section">
                <div class="image-preview-container" onclick="document.getElementById('portada').click()">
                    </div>
                </div>

```

**Explicación:**
Diseñé esta sección para que la subida de imágenes sea intuitiva. En lugar del típico botón gris de "Examinar archivo", creé un recuadro visual. Si haces clic en él, se dispara el `input` oculto de tipo archivo. Además, incluí lógica PHP aquí para mostrar la portada actual si estamos editando, o un signo "+" si es un libro nuevo.

---

### 9. Paso 1: Datos Principales y Estado

```html
            <div class="book-details-section">
                <div id="step1" class="step-container">
                    <div class="custom-dropdown" id="statusDropdown">...</div>

                    <div id="dynamic-fields-container">...</div>

                    <input type="text" name="titulo" ... >
                    
                    <button type="button" onclick="goToStep2()">SIGUIENTE &rarr;</button>
                </div>

```

**Explicación:**
Para no abrumar al usuario, dividí el formulario en pasos. En este primer paso, solicito lo más importante: el estado (Deseado, Leyendo, Leído) y los datos básicos. He creado un sistema de "campos dinámicos": si selecciono "Leyendo", aparece el campo de capítulo actual; si selecciono "Leído", aparecen las estrellas de valoración. Esto mantiene la interfaz limpia y relevante.

---

### 10. Paso 2: Metadatos y Categorías

```html
                <div id="step2" class="step-container hidden-step">
                    <div class="category-grid">
                        <div class="cat-btn" onclick="selectCat(this, 'Ficción')">Ficción</div>
                        </div>

                    <div class="grid grid-cols-2 gap-4">...</div>

                    <button type="submit" class="btn btn-save">GUARDAR TODO</button>
                </div>

```

**Explicación:**
En el segundo paso, agrupo la información técnica. Implementé una cuadrícula de botones para las categorías en lugar de una lista aburrida, lo que hace la selección más rápida. Aquí también recojo datos como la editorial, el año y el número de páginas. Es donde coloco el botón final de "Submit" para enviar todo el formulario al servidor.

---

### 11. Interactividad (JavaScript)

```javascript
    <script>
        // Lógica de navegación entre pasos (Step 1 -> Step 2)
        function goToStep2() { ... }

        // Lógica visual del Dropdown y actualización de campos
        items.forEach(item => { ... updateDynamicFields(val); });

        // Lógica de estrellas de valoración
        function setRating(val) { ... }

        // Previsualización instantánea de la imagen subida
        document.getElementById('portada').addEventListener('change', ...);
        
        // Inicialización de datos al cargar (para modo edición)
        window.addEventListener('DOMContentLoaded', () => { ... });
    </script>

```

**Explicación:**
Finalmente, añadí todo el comportamiento dinámico con JavaScript. Escribí funciones para cambiar entre el paso 1 y 2 sin recargar la página, y para que la previsualización de la imagen se actualice en cuanto el usuario selecciona un archivo. También incluí un bloque de inicialización que, si estoy en modo edición, "enciende" automáticamente las estrellas correctas, selecciona la categoría guardada y colorea el estado correspondiente para que el usuario vea sus datos tal cual los dejó.