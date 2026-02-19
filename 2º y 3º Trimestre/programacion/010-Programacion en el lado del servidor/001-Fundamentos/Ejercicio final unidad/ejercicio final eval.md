En este ejercicio voy a desarrollar un pequeño programa en PHP para automatizar una clasificación sencilla el objetivo es crear una herramienta que reciba la edad de una persona y determine automáticamente su categoría joven o no joven para ello defino la función clasificarEdad y probar su funcionamiento enviándole un valor concreto en este caso 19 para ver el resultado inmediato en pantalla

---

Primero comienzo abriendo con la etiqueta de apertura de PHP
```
<?php
```
Luego declaro la función clasificarEdad que recibe un parámetro $edad y clasifica si es un joven o no
```
function clasificarEdad($edad) {
      
      if($edad < 30){
        echo "Eres un joven";
      }else{
        echo "Ya no eres un joven";
      }
  }
```
Luego llamo a la función clasificarEdad con el parámetro 19
```
  clasificarEdad(19); 
```
cierro con la etiqueta de cierre de PHP
```
?>
```

---

En conclusión he comprobado cómo PHP gestiona el flujo de información a través de parámetros. He visto que la función actúa como una caja negra que recibe un dato de entrada el numero 19lo procesa internamente mediante una comparación matemática y produce una salida específica este ejemplo valida que nuestra lógica condicional funciona correctamente