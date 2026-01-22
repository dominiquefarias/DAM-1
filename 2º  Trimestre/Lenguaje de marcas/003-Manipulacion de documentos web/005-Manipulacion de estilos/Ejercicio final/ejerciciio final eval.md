
En este ejercicio voy a mejorar la interactividad de los formularios web. Primero modificaré el archivo de estilo condicional para que reaccione no solo a la longitud exacta sino también al exceso de caracteres cambiando el color del texto y luego pondre algo similar pero para el archivo de cálculo css

---

Primero comienzo editando el archivo que se me a dado el cual es 004-estilo condicional.html añadiendo una nueva clase en el css para el color del texto

```
<style>
  .rosa{background:rgba(226, 69, 176, 1);}
  .morado{background: rgba(225, 1, 255, 1);}
  .azul{color: blue;}
</style>

```

Ahora modifico el programa para añadir la nueva condición que detecta si la longitud supera los 15 caracteres

```
<script>
  let entrada = document.querySelector("input")
  entrada.onkeyup = function(){
    let valor = this.value;
    let longitud = valor.length
    
    if(longitud == 9){
        this.classList.add("morado")
        this.classList.remove("rosa")
    }else{
        this.classList.remove("morado")
        this.classList.add("rosa")
    }

    if(longitud > 15){
        this.classList.add("azul")
    }else{
        this.classList.remove("azul")
    }
  }
</script>

```



A continuación paso al archivo el siguiente archivo 006-funcion de calculo en css.html y defino dos clases con diferentes cálculos de ancho en css



```
<style>
  .normal{width:calc(100% - 50px);background:#e782f0;}
  .grande{width:calc(100% - 10px);background:#82f0e7;}
</style>

```

Y finalmente añado un programa que permite alternar entre estos cálculos al hacer click en el elemento div

```
<script>
    let caja = document.querySelector("div")
    caja.onclick = function(){
        if(this.classList.contains("normal")){
            this.classList.remove("normal")
            this.classList.add("grande")
        }else{
            this.classList.remove("grande")
            this.classList.add("normal")
        }
    }
</script>

```
---

En conclusión he aprendido a manipular múltiples estilos CSS desde JavaScript utilizando classList lo que me permite crear interfaces que responden de forma inmediata a las acciones que se realicen tanto al escribir en un input como al interactuar con elementos de bloque