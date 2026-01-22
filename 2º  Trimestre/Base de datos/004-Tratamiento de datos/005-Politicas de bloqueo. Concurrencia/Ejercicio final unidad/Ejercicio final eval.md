
En este ejercicio aprendo a proteger las páginas web hechas con php básicamente probamos dos cosas cómo esconder información y despues recuperarla cómo bloquearla para siempre o sea como las contraseñas también utilizamols la fuerza bruta e intentando adivinar claves simples para ver lo fácil que es romperlas, y tocamos el código básico de las letras para entender cómo las lee el ordenador

---

Primero creo un programa para comprobar la integridad de datos al codificar y descodificar en un archivo php


```

$contrasena = "Seguridad2025";
$codificado = base64_encode($contrasena);
$descodificado = base64_decode($codificado);

```

Lo cual me da los siguientes resultados:


```

Original: Seguridad2025
Codificado: U2VndXJpZGFkMjAyNQ==
Descodificado: Seguridad2025
Las cadenas son identicas

```

Ahora creo funciones para crear tipo una capa de oscurecimiento de datos en un archivo php


```

function codificar($cadena){
for($i = 0;$i<9;$i++){
$cadena = base64_encode($cadena);
}
return $cadena;
}

```

Que se veria asi:


```

Contraseña: AccesoPermitido
Oculto 9 veces: Vm0wd2QyUXlVWGxWV0d4WFlUSm9WMVl3Wkc5V01WbDNXa2M1VjAxV2JETlhhMUpUVmpBeFYySkVUbGhoTVVwVVZtcEJlRll5U2tWVWJGl
Recuperado: AccesoPermitido

```

Ahora realizo una prueba de conversión a nivel de byte utilizando la tabla ascii en un archivo php


```

$caracter = "Z";
$valor_ascii = ord($caracter);
$recuperado = chr($valor_ascii);

```

Que se veria asi:


```

Carácter original: Z
Valor ASCII: 90
Recuperado: Z
La conversión es correcta

```

Ahora hago una prueba de fuerza bruta para recuperar una contraseña original probando combinaciones y comparando su versión codificada en un archivo php


```

$intento = $caracteres[$i] . $caracteres[$j] . $caracteres[$k];
if(codificar($intento) == $objetivo){ ... }

```

Lo cual me da los siguientes resultados


```

¡Contraseña encontrada!: abc

```

Ahora verifico una contraseña comparando su huella digital md5 con un hash almacenado en un archivo php


```

if (md5($entrada_usuario) == $hash_guardado) { ... }

```

Que se veria asi:


```

El usuario introduce: 1234
Hash generado: 81dc9bdb52d04dc20036dbd8313ed055
Acceso concedido. Las contraseñas coinciden.

```

---

En conclusión vi que con el método base64 cualquiera puede recuperar el mensaje original si se pone a probar combinaciones con la fuerza bruta en cambio, el md5 sirve para comprobar que la información es correcta sin tener que enseñarl al final es que para que algo sea seguro de verdad no basta con una seguridad tan básica