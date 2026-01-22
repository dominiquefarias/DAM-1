
En este ejercicio comienzo con la creación de copias de seguridad para garantizar la integridad de la información seguido de la eliminación precisa de registros obsoletos y la corrección de errores en los datos existentes mediante de actualización comprendiendo así completo del mantenimiento de la información

---

Primero voy hasta el directorio Escritorio y creo el directorio para la copia de seguridad


```

cd ~/Escritorio
mkdir micopiadeseguridad
cd micopiadeseguridad

```

Ahora realizo la copia de seguridad de la base de datos empresarial


```

mysqldump -u root -p empresarial > copia_de_seguridad_empresarial.sql

```

Ahora accedo a la base de datos para realizar las operaciones de mantenimiento


```

USE empresarial;

```

Ahora elimino el registro del cliente Jose Vicente utilizando su número de teléfono como identificador único


```

DELETE FROM clientes WHERE telefono = '620891718';

```

Lo cual me da el siguiente resultado


```

Query OK, 1 row affected (0.01 sec)

```

Ahora corrijo el nombre del cliente que se ha escrito mal en la base de datos utilizando nuevamente su teléfono como referencia


```

UPDATE clientes SET nombre = 'Jose Vicente' WHERE telefono = '620891718';

```

Lo cual me da el siguiente resultado


```

Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

```

---

En conclusión este ejercicio me ha permitido verificar la importancia de las operaciones de mantenimiento en una base de datos con `DELETE` y `UPDATE` combinadas con la gestión de archivos del sistema se ve que es muy importante la información depurada y actualizada así como asegurar su persistencia mediante copias de seguridad esto transforma una base de datos mas confiable para la empresa
