
En este ejercicio voy a definir un esquema xsd para validar la estructura de un documento XML de una persona el objetivo es identificar los elementos clave y sus tipos de datos para asegurar que la información intercambiada cumpla con una normativa estricta utilizando tipos complejos y secuencias

---

Primero comienzo definiendo el esquema y especificando el espacio de nombres porque es un esquema XML

```

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

```
Ahora defino el elemento raíz persona especificando que tiene una estructura compleja y que sus elementos deben aparecer en orden dado que es un tipo secuencial

```

<xs:element name="persona">
[xs:complexType](https://www.google.com/search?q=xs:complexType)
[xs:sequence](https://www.google.com/search?q=xs:sequence)

```
Ahora defino los elementos hijos simples nombre y apellidos ambos de tipo string dado que son datos simples

```

```
    <xs:element name="nombre" type="xs:string"/>
    <xs:element name="apellidos" type="xs:string"/>

```

```
Ahora defino el elemento telefonos que a su vez es un tipo complejo que contiene una secuencia de elementos telefono permitiendo un número ilimitado de ocurrencias

```

```
    <xs:element name="telefonos">
      <xs:complexType>
        <xs:sequence>
          <xs:element name="telefono" type="xs:string" maxOccurs="unbounded"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>

```

```
Finalmente cierro todas las etiquetas abiertas

```

```
  </xs:sequence>
</xs:complexType>

```

</xs:element>

</xs:schema>

```

---

En conclusión he aprfendido a crear unas descripción formal de un documento utilizando xsd lo más udctil ha sido entender dcómo anidar tipos complejos dentro de otros para cresar estructuras jerárquicas como la lista de teléfonos y cómo el uso de maxOccurs me permite flexibilizar la cantidad de datos que recibo sin perder el control sobre el tivpo de dato
