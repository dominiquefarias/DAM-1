ALTER TABLE clientes
ADD COLUMN identificador INT AUTO_INCREMENT
PRIMARY KEY FIRST;

ALTER = Altera
TABLE = Tabla
clientes = la tabla que quiero alterar
ADD = la operacion que quiero realizar
COLUMN  = quiero añadir una columna
identificador = es el nombre de la columna que quiero añadir
INT = el tipo de dato de la columna
AUTO_INCREMENT = el numero que va a crecer 
PRIMARY_KEY = clave primaria
FIRST = si hay varias, esta tiene la preferencia

DESCRIBE clientes;

INSERT INTO clientes
VALUES(
	NULL,
	'12345678A',
	'Jose vicente',
	'sanchez',
	'info@mail.com'
);

INSERT INTO clientes
VALUES(
	NULL,
	'12345678A',
	'Jose vicente',
	'sanchez',
	'info@mail.com'
);
	
