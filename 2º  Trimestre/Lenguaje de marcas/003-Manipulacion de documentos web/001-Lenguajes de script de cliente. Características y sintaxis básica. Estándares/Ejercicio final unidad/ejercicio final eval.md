
---

Primero comienzo abriendo el archivo html 
```
<!doctype html>
<html lang="es">

<head>
    <meta charset="UTF-8">
</head>
```
Ahora abro el body y comienzo a escribir el script
```
<body>
```
Ahora escribo el script el cual contiene una variable que almacena la fecha actual y una funcion que recibe dos parametros y retorna una cadena de texto la cual se muestra en la consola con el console.log
```
    <script>
        let hoy = new Date();
        function diHola(nombre, edad) {
            return "Hola, " + nombre + " tienes " + edad + " años, ¿cómo estás?";
        }
        console.log("Hoy es: " + hoy.toLocaleDateString());
        console.log(diHola("Dominique", 19));
    </script>
</body>
```
Ahora cierro el body y el html
```
</html>
```

---