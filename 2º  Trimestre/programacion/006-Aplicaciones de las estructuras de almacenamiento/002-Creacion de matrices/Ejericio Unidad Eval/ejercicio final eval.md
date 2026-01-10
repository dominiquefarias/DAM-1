'''
Enunciado paso a paso
Introducir nueva comida en el menú:

Añade una nueva comida al menú.
Listar comidas en el menú:

Muestra todas las comidas que has añadido hasta ahora.
Guardar en archivo:

Guarda la lista de comidas en un archivo binario llamado datos.bin.
Restricciones
No uses funciones ni métodos que no hayas visto en clase.
Solo puedes usar el módulo pickle para guardar y cargar los datos.
'''
En este ejercicio se me pide crear un programa que permita gestionar una lista de comidas este programa permite al usuario añadir platos y ver su lista actual mediante un menú además implemento una la capacidad de exportar y guardar el menú creado en un archivo externo llamado datos.bin utilizando la librería pickle logrando así almacenar la información

---

Primero importo el modulo pickle para poder guardar los datos en un archivo binario

```
import pickle
```

Luego creo una lista vacia para guardar los datos

```
menu = []
```

Ahora creo un bucle while para que el programa se ejecute hasta que el usuario decida salir

```
while True:
```

Ahora creo un menu con 3 opciones y creo una variable opcion para guardar la opcion que el usuario elija y pasarla a entero

```
    print("Opciones:")
    print("1. Introducir nueva comida en el menu")
    print("2. Listar las comidas del menu")
    print("3. Guardar en archivo")
    opcion = int(input("Selecciona una opcion: "))
```

Ahora creo una condicion para que si el usuario elige la opcion 1 le pida que introduzca el nombre de la comida y la añada a la lista

```
    if opcion == 1:
        comida = input("Introduce el nombre de la comida: ")
        menu.append(comida)
```

Ahora creo una condicion para que si el usuario elige la opcion 2 liste todas las comidas que ha introducido hasta el momento

```
    elif opcion == 2:
        print("Tus comidas hasta el momento son: ")
        for elemento in menu:
            print (elemento)
```

Ahora creo una condicion para que si el usuario elige la opcion 3 guarde la lista de comidas en un archivo binario llamado datos.bin

```
    elif opcion == 3:
        archivo = open("datos.bin","wb")
        pickle.dump(menu, archivo)
        archivo.close()
```

---

Como conclusion he construido un programa funcional que integra la interacción con el usuario y la gestión de archivos a través de un bucle while y condicionales creando un menu dinámico que permite al usuario introducir comidas y listarlas además de guardarlas en un archivo binario utilizando la librería pickle lo que asegura que la información perdure este programa sirve para aprender a crear una base de para la mayoria de programas utilizando CRUD