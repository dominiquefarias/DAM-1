En este ejercicio combino html con javascript sobre todo me centro en las fechas asi como tambien en las funciones parametrizadas el objetivo es crear un programa que procese datos estos datos son la fecha actual y un saludo personalizado y muestre los resultados directamente en la consola del navegador mediante console.log, en lugar de imprimirlo en el cuerpo de la página

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

En conclusión he aprendido a conectar html con javascript de forma en la que he podido comprobar que puedo guardar la fecha de hoy en una variable y usarla cuando quiera lo más útil ha sido entender cómo funciona el return mi función prepara el saludo mezclando el nombre y la edad y luego entrega ese texto listo para que el console.log lo muestre es como tener una pequeña fábrica de saludos dentro de mi código