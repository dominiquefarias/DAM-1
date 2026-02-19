<?php

  function clasificarEdad($edad) {
      
      if($edad < 30){
        echo "Eres un joven";
      }else{
        echo "Ya no eres un joven";
      }
  }

  clasificarEdad(19); 

?>