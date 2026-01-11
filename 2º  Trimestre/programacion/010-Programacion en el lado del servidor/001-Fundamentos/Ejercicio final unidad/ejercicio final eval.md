
---

Primero comienzo abriendo con la etiqueta de apertura de PHP
```
<?php
```

Luego declaro la función clasificarEdad que recibe un parámetro $edad
```
function clasificarEdad($edad) {
      
      if($edad < 30){
        echo "Eres un joven";
      }else{
        echo "Ya no eres un joven";
      }
  }

  clasificarEdad(19); 

?>