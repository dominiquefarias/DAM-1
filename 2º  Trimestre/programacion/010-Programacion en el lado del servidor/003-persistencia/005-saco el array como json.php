<?php
  $cliente = [];
  $cliente['nombre'] = "Dominique";
  $cliente['apellidos'] = "Farias Osorio";
  $cliente['email'] = "domi@mail.com";
  
  $json = json_encode($cliente);
  echo $json;  
?>
