En este ejercicio voy a repasar los conceptos de selección y manipulación del DOM comenzando por la lectura de elementos y pasando por la modificación de contenido estático y dinámico el objetivo es alterar el texto de varios elementos html y ampliar un array de datos para ver cómo se refleja en la vista del navegador utilizando javascript

---

Primero comienzo con el archivo 001- lectura.html donde selecciono el párrafo para leer su contenido

```

<script>
// Selecciono el elemento que tenga la etiqueta p
const elemento = document.querySelector("p");
document.write(elemento);
document.write(elemento.textContent);
</script>

```

Ahora modifico el archivo 003-escribir html.html para cambiar el contenido de la etiqueta div reemplazando el saludo original por otro texto diferente

```

<script>
document.querySelector("div").innerHTML = "<h1>Hola modificado desde JS</h1>"
</script>

```

Ahora abro el archivo 004-microblog.html y agrego más elementos al array de articulos para que el bucle los pinte en el contenedor main

```

<script>
const articulos = [
"Primer articulo", "segundo articulo", "tercer articulo", "cuarto articulo extra", "quinto articulo extra"
];
const contenedor = document.querySelector("main");
for (let i = 0; i < articulos.length; i++) {
contenedor.innerHTML += "<h3>" + articulos[i] + "</h3>";
}
</script>

```

Finalmente edito el archivo 002-escribir.html para cambiar los textos de los elementos div seleccionándolos por su id específico

```

<script>
document.querySelector("#rojo").textContent = "nuevo texto rojo modificado"
document.querySelector("#verde").textContent = "nuevo texto verde modificado"
document.querySelector("#azul").textContent = "nuevo texto azul modificado"
</script>

```

---

En conclusión he aprendido a acceder y modificar el árbol DOM de diferentes maneras tanto leyendo propiedades como escribiendo nuevos valores en textContent e innerHTML lo más interesante ha sido ver cómo al ampliar el array en el microblog el bucle for se encarga automáticamente de generar el html necesario para los nuevos artículos sin tener que escribir las etiquetas a mano una por una

