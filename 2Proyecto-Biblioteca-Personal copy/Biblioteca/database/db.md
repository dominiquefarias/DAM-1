
---

Primero Comienzo creando la base de datos para el proyecto y llamo la base de datos biblioteca_personal
```sql
CREATE DATABASE IF NOT EXISTS biblioteca_personal;
```
Luego utilizo USE para seleccionar la base de datos
```sql
USE biblioteca_personal;
```

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
Luego creo la tabla de categorias que es por categoria donde utilizo el id_categoria como primary key y auto incremento, que es para distinguir a cada categoria que entre por su id ya que puede haber categorias que tengan mas de un libro. 
y que mientras vaya subiendo mas categorias suba el numero de id que le corresponde y utilizo el INT para que sea solo numerico.
Luego creo la otra de nombre que es para el nombre de la categoria donde NOT_NULL que es para que no pueda quedar vacio.
```sql
CREATE TABLE Categorias (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(50) NOT NULL
);
```
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
Ahora creo un usuario para poder conectar la base de datos con algun proyecto de php o html o python etc y puedan acceder a esta
Primero creo un usuario nuevo con contraseña en este caso e puesto % dado que es para conectarse a la base de datos desde cualquier direccion ip
luego le doy permisos para que pueda conectarse a la base de datos y pueda hacer todo lo que quiera y tambien le doy permisos para que pueda eliminar la base de datos
despues le doy permisos para que pueda conectarse a la base de datos y pueda hacer todo lo que quiera y tambien le doy permisos para que pueda eliminar la base de datos

```sql
CREATE USER 
'ruthydomi'@'%' 
IDENTIFIED  BY 'BibliotecaPersonal123$';
GRANT USAGE ON *.* TO 'ruthydomi'@'%';
ALTER USER 'ruthydomi'@'%' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `biblioteca_personal`.* 
TO 'ruthydomi'@'%';
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