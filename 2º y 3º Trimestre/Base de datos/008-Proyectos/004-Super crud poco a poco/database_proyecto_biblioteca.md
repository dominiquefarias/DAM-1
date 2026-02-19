En mi proyecto el cual se basa en una biblioteca personal la cual es para mantener un registro personal de libros y que tu puedas añadir tus propios libros y tratar de ser detallado teniendo en cuenta su categoria un poco de que trata y su portada y todo en general. En la base de datos como tal cree varias tablas y estas conectandolas con PHP puede almacenar toda la informacion sobre el libro y sobre la cuenta del usuario y que esta visualice solo los libros que el usuario ha añadido por ejemplo haciendo pruebas al principo pensabamos que se iba a guardar todo en lo mismo y no iba a haber una distincion por la cual creamos un pequeño pedazo de codigo que finalmente pueda identificar al usuario y que muestre solo los libros añadidos por este. 

---

Primero Comienzo creando la base de datos para el proyecto y llamo la base de datos biblioteca_personal
```sql
CREATE DATABASE IF NOT EXISTS biblioteca_personal;
```
Luego utilizo USE para seleccionar la base de datos
```sql
USE biblioteca_personal;
```
Esta tabla de usuario sirve para poder identificar al usuario e identificandose con su usuario, email, contrasena y nombre completo asi como tambien la fecha en la que fue creado el usuario

Luego creo la tabla de usuarios que es por usuario donde utilizo el id_usuario como primary key y auto incremento, que es para distinguir a cada usuario que entre por su id
esto es para que cada usuario tenga su propia colección de libros y que mientras haya subiendo mas usuarios suba el numero de id que le corresponde y utilizo el INT para que sea solo numerico.
Luego creo la otro de usuarios que es por usuario donde NOT_NULL que es para que no quede vacio y UNIQUE que es para que no se repita.
Despues creo el de email el cual es para el correo electronico este tambien utiliza NOT_NULL que es para que no quede vacio y UNIQUE que es para que no se repita.
Despues creo el de contrasena el cual es para la contraseña este tambien utiliza NOT_NULL que es para que no quede vacio.
Despues creo el de nombre_completo el cual es para el nombre completo del usuario.
Despues creo el de created_at el cual es para la fecha de creacion del usuario.
```sql
CREATE TABLE IF NOT EXISTS Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    nombre_completo VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
Luego creo la tabla de autores esta tabla fue creada para recopilar el nombre del autor y nacionalidad cuando sea introducido por el usuario para lograr que el usuario pueda buscar el autor que desea depues de que sea añadido por este

Ahora creo la tabla de autores que es por autor donde utilizo el id_autor como primary key y auto incremento, que es para distinguir a cada autor que entre por su id ya que puede haber autores que tengan mas de un libro. 
y que mientras haya subiendo mas autores suba el numero de id que le corresponde y utilizo el INT para que sea solo numerico.
Luego creo la otro de nombre que es para el nombre del autor donde NOT_NULL que es para que no quede vacio.
Despues creo el de nacionalidad el cual es para la nacionalidad del autor
```sql
CREATE TABLE Autores (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50)
);
```
Tambien creo la tabla de categorias esta tabla fue creada para recopilar el nombre de la categoria dependiendo de que es la cual despues se le dara al usuario unas cuantas categorias para que seleccione y pueda poner que el libro que ha añadido sea de esa categoria

Luego creo la tabla de categorias que es por categoria donde utilizo el id_categoria como primary key y auto incremento, que es para distinguir a cada categoria que entre por su id ya que puede haber categorias que tengan mas de un libro. 
y que mientras vaya subiendo mas categorias suba el numero de id que le corresponde y utilizo el INT para que sea solo numerico.
Luego creo la otra de nombre que es para el nombre de la categoria donde NOT_NULL que es para que no pueda quedar vacio.
```sql
CREATE TABLE Categorias (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(50) NOT NULL
);
```
Luego utilizo la tabla de editoriales para poder almacenar la editorial del libro que el usuario añadiria esta tabla contine pais y nombre_editorial la creo con id_editorial la cual es para luego poder hacer un "JOIN" con la tabla de libros

Luego creo la tabla de editoriales que es por editorial donde utilizo el id_editorial como primary key y auto incremento, que es para distinguir a cada editorial que entre por su id ya que puede haber editoriales que tengan mas de un libro. 
y que mientras vaya subiendo mas editoriales suba el numero de id que le corresponde y utilizo el INT para que sea solo numerico.
Luego creo la otro de nombre que es para el nombre de la editorial donde NOT_NULL que es para que no pueda quedar vacio.
Luego creo el de pais el cual es para el pais de la editorial
```sql
CREATE TABLE Editoriales (
    id_editorial INT PRIMARY KEY AUTO_INCREMENT,
    nombre_editorial VARCHAR(100) NOT NULL,
    pais VARCHAR(50)
);
```
Luego creo la tabla de libros mediante esta recopilara todos los datos del libro que el usuario añadiria asi como tambien esta tabla tiene una relacion entre las tablas de libros con id_autor con la tabla de Autores, Luego tiene una relacion de la tabla de libros con id_categoria con la tabla de Categoria, asi como tambien tengo una relacion en la tabla de libros con id_editorial con la tabla de Editoriales

Luego creo la tabla de libros que es por libro donde utilizo el id_libro como primary key y auto incremento, que es para distinguir a cada libro que entre por su id ya que puede haber libros que tengan mas de un autor, editorial y categoria. 
y que mientras vaya subiendo mas libros suba el numero de id que le corresponde y utilizo el INT para que sea solo numerico.
Luego creo el otro de titulo que es para el titulo del libro donde NOT_NULL que es para que no pueda quedar vacio.
Luego creo el de isbn el cual es para el isbn del libro el cual tambien es UNIQUE que es para que sea unico y NOT_NULL que es para que no pueda quedar vacio.
Luego creo el de num_paginas el cual es para el numero de paginas del libro el cual es INT que es para que sea solo numerico.
Luego creo el de idioma el cual es para el idioma del libro 
Luego creo el de edicion el cual es para la edicion del libro si es especial, tapa dura, tapa blanda, etc.
Luego creo el de año_publicacion el cual es para el año de publicacion del libro el cual tambien es INT que es para que sea solo numerico.
Luego creo el de descripcion el cual es para la descripcion del libro el cual tambien es TEXT que es para que sea solo texto.
Luego creo el de id_autor el cual es para el id del autor del libro
Luego creo el de id_editorial el cual es para el id de la editorial del libro
Luego creo el de id_categoria el cual es para el id de la categoria del libro

Luego creo una FOREIGN KEY que es para la relacion de la tabla de libros con la tabla de autores, editoriales y categorias
Por ejemplo el id_autor es para la relacion de la tabla de libros con la tabla de autores
Donde el id_editorial de la tabla de libros es igual al id_editorial de la tabla de editoriales
Donde el id_categoria de la tabla de libros es igual al id_categoria de la tabla de categorias
```sql
CREATE TABLE Libros (
    id_libro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    num_paginas INT,
    idioma VARCHAR(30),
    edicion VARCHAR(50),
    año_publicacion INT,
    descripcion TEXT,
    id_autor INT,
    id_editorial INT,
    id_categoria INT,
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor),
    FOREIGN KEY (id_editorial) REFERENCES Editoriales(id_editorial),
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);
```
Tambien luego creo la tabla Coleccion qu esta tabla la utilizo para las colecciones que creamos que tenemos que son deseado, leyendo y leido donde creo distintos campos que se diferenciaran mas adelante para mostrarse dependiendo del estado que quiera poner el usuario. En este caso cree una FK con la tabla de usuarios y el id usuario de la coleccion para que no haya repeticion. Asi como tambien cree una FK con la tabla de libros y el id libro de la coleccion para que no haya repeticion

Luego creo la tabla coleccion para poder divoidir lo que el usuario tiene deseado, leyendo y leido
donde el id_colecciones es INT que es para que sea solo numerico asi como tambien es PRIMARY KEY AUTO_INCREMENT que es para que sea auto incremento y que mientras vaya subiendo mas libros suba el numero de id que le corresponde
Donde el id_usuario es INT que es para que sea solo numerico asi como tambien es NOT NULL que es para que no pueda quedar vacio
Donde el id_libro es INT que es para que sea solo numerico asi como tambien es NOT NULL que es para que no pueda quedar vacio
Donde el estado es ENUM que es para que sea solo texto y que pueda tener los valores de "Deseado", "Leyendo", "Leido"
Donde el fecha_agregado es TIMESTAMP que es para que recuerde la fecha en que se agrego el libro
Donde el precio es DECIMAL que es para que sea numero y este solo aparecera cuando el estado sea "Deseado"
Donde el capitulo_actual es INT que es para que sea solo numerico y este solo aparecera cuando el estado sea "Leyendo"
Donde el resena es TEXT que es para que sea solo texto y este solo aparecera cuando el estado sea "Leido"
Donde el valoracion es INT que es para que sea solo numerico y este solo aparecera cuando el estado sea "Leido" y tambien esta el CHECK que es para que sea solo numerico y este solo aparecera cuando el estado sea "Leido" y que pueda tener los valores de 0 a 5
Donde el FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE que es para que cuando se elimine un usuario se elimine tambien su coleccion
Donde el FOREIGN KEY (id_libro) REFERENCES Libros(id_libro) ON DELETE CASCADE que es para que cuando se elimine un libro se elimine tambien su coleccion
Donde el UNIQUE KEY (id_usuario, id_libro) que es para que no pueda haber dos libros iguales para un usuario

```sql
CREATE TABLE Coleccion (
    id_coleccion INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_libro INT NOT NULL,
    estado ENUM('Deseado', 'Leyendo', 'Leido') NOT NULL,
    fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    precio DECIMAL(10, 2),       
    capitulo_actual INT,         
    resena TEXT,                    
    valoracion INT CHECK (valoracion BETWEEN 0 AND 5), 
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_libro) REFERENCES Libros(id_libro) ON DELETE CASCADE,
    UNIQUE KEY (id_usuario, id_libro)
);
```
Por ultimo creo el usuario que es para luego crear un archo ya sea en PHP o en lo que sea y lograr conectarlo con la base de datos y poder utilizarlo

Ahora creo un usuario para poder conectar la base de datos con algun proyecto de php o html o python etc y puedan acceder a esta
Primero creo un usuario nuevo con contraseña en este caso e puesto % dado que es para conectarse a la base de datos desde cualquier direccion ip
luego le doy permisos para que pueda conectarse a la base de datos y pueda hacer todo lo que quiera y tambien le doy permisos para que pueda eliminar la base de datos
despues le doy permisos para que pueda conectarse a la base de datos y pueda hacer todo lo que quiera y tambien le doy permisos para que pueda eliminar la base de datos

```sql
CREATE USER 
'ruthydomi'@'root' 
IDENTIFIED  BY 'BibliotecaPersonal123$';
GRANT USAGE ON *.* TO 'ruthydomi'@'root';
ALTER USER 'ruthydomi'@'root' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `biblioteca_personal`.* 
TO 'ruthydomi'@'root';
FLUSH PRIVILEGES;
```
Despues hice un alter table para poder agregar la portada y el precio al libro
```sql
ALTER TABLE Libros ADD COLUMN portada VARCHAR(255) DEFAULT NULL;
ALTER TABLE Libros ADD COLUMN precio DECIMAL(6, 2) DEFAULT NULL;
```
Finalmente creo un usuario de prueba para poder iniciar sesion y poder probar el sistema de base de datos
-- Usuario de prueba (contraseña: Admin123$)
-- Nota: En producción, la contraseña debe estar hasheada. 

```sql
INSERT INTO Usuarios (usuario, email, contrasena, nombre_completo) VALUES 
('admin', 'admin@example.com', '$2y$10$YourHashedPasswordHere...', 'Administrador');
```
Tambien le añadi un select para poder ver todos los libros que hay en la base de datos el cual tambien se vera en las foto adjuntas
```sql
SELECT * FROM Libros;
```

---

Como finalidad la base de datos de nuestro proyecto esta creaada para poder tener ese registrop ersonal de los libros que a uno le gustaria leer, esta leyendo y que ya ha leido. La pagina como tal tiene varias "vistas" las cuales con las FK y las referncias que hicimos logramos que todo funcione correctamente ya que logramos la relacion necesaria para que todo se logre ver como se mostraran en las imagenes adjuntas