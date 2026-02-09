En este ejercicio primero crearé una barra de menú con enlaces para poder navegar a otras páginas como Juegos o Contacto después me centraré en crear una tabla ordenada para mostrar la lista de personas registradas, incluyendo mis propios datos, asegurándome de que cada columna tenga su encabezado correcto para que se entienda bien la información

---

Primero comienzo abriendo la parte principal del html
```
<!doctype html>
<html lang="es">

<head>
    <meta charset="utf-8">
    <title>Panel de Usuarios</title>
</head>
```

Luego abro el body y añado enlaces a la página principal que permitan navegar entre diferentes partes del sitio
```
<body>
    <nav>
       <ul>
            <li>
                <a href="Inicio.php">Inicio</a>
            </li>
            <li>
                <a href="Acerca de.php">Acerca de</a>
            </li>
            <li>
                <a href="Contacto.php">Contacto</a>
            </li>
            <li>
                <a href="Juegos.php">Juegos</a>
            </li>
       </ul> 
    </nav>
```

Luego abro el main y añado la tabla con los datos de los usuarios
```
    <main>
       <h1>Listado de Usuarios</h1>
       
       <table border="1">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Apellidos</th>
                    <th>Email</th>
                    <th>Dirección</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Juan</td>
                    <td>Pérez García</td>
                    <td>juan.perez@email.com</td>
                    <td>Calle Falsa 12</td>
                </tr>
                <tr>
                    <td>Ana</td>
                    <td>López Martín</td>
                    <td>ana.lopez@email.com</td>
                    <td>calle falsa 45</td>
                </tr>
                <tr>
                    <td>Carlos</td>
                    <td>Ruiz Díaz</td>
                    <td>carlos.ruiz@email.com</td>
                    <td>calle falsa 1</td>
                </tr>
                <tr>
                    <td>Dominique</td>
                    <td>Farías Osorio</td>
                    <td>dominique@email.com</td>
                    <td>calle falsa 10</td>
                </tr>
            </tbody>
        </table>
    </main>
</body>

</html>
```

---

En conclusion he construido mi panel de administración y he aprendido a organizar los enlaces en una lista de navegación limpia y a presentar los datos de los usuarios como el nombre y el email en una cuadrícula ordenada aunque ahora mismo los datos están escritos a mano son estático esta estructura HTML es exactamente la que necesitaré para en el futuro rellenar las filas automáticamente usando PHP