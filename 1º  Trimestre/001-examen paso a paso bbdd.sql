# Iniciamos sesion en MySQL --> sudo mysql -u root -p

# Creamos la base de datos --> CREATE DABASES blog-simulacro;

# Nos aseguramos de que exista la base de datos --> SHOW DATABASES;

# Ingresamos a la base de datos --> USE blog-simulacro;

# Ahora creamos una tabla: Opcion 1:
	CREATE TABLE autores(
		nombre VARCHAR(100),
		apellidos VARCHAR(100),
		email VARCHAR(100)
	);
		
# Miramos que la hemos creado bien --> SHOW TABLES;

# Ahora quiero crear la columna identificador
	ALTER TABLE autores ADD COLUMN Identificador INT auto_increment PRIMARY KEY FIRST;
	
# O bien lo creamos con identificador desde el principio y con primary key first: Opcion 2:
	CREATE TABLE autores(
		Identificador INT AUTO_INCREMENT PRIMARY KEY,
		nombre VARCHAR(100),
		apellidos VARCHAR(100),
		email VARCHAR(100)
	);
	
# Vamos a ver que se ha hecho --> DESCRIBE autores;

# Ahora quiero insertar un autor de prueba:
	INSERT INTO autores VALUES(
		NULL,
		'Dominique',
		'Farias Osorio',
		'domi@mail.com'
	);

# Me aseguro que se haya creado --> SELECT * FROM autores;

# Creo la tabla de entradas:
	CREATE TABLE entradas (
		Identificador INT(100) AUTO_INCREMENT,
		titulo VARCHAR(100),
		fecha VARCHAR(100),
		imagen VARCHAR(100),
		id_autor VARCHAR(100),
		contenido TEXT,
		PRIMARY KEY (Identificador)
	);
		
# Pimero comprobamos la existencia de la tabla --> SHOW TABLES;

# Describimos --> DESCRIBE entradas;

# Creamos una foreign key
	ALTER TABLE entradas
	ADD CONSTRAINT autores_a_entradas
	FOREIGN KEY (id_autor)
	REFERENCES autores(Identificador)
	ON DELETE CASCADE
	ON UPDATE CASCADE;
	
# Cambiamos tipo de datos:
	ALTER TABLE entradas
	MODIFY COLUMN id_autor INT;
	
# Insertamos una entrada:
	INSERT INTO entradas VALUES(
		NULL,
		'Titulo de la primera entrada',
		'2025-11-03',
		'imagen.jpg',
		1,
		'Este es el contenido de la primera entrada'
	);
	
# Peticion cruzada:
	SELECT 
	FROM entradas.titulo,entradas.fecha,entradas.imagen,entradas.entradas.contenido,entradas.nombre,autores.apellidos
	LEFT JOIN autores
	ON entradas.id_autor = autores.Identificador;
	
# Por ultimo creamos una vista
