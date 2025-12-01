-- Create

INSERT INTO clientes VALUES(
	'12345678A',
	'Dominique',
	'Farias Osorio',
	'info@domi.com'
);

Query OK, 1 row affected (0,01 sec)

-- Read

SELECT * FROM clientes;

+-----------+-----------+---------------+---------------+
| dni       | nombre    | apellidos     | email         |
+-----------+-----------+---------------+---------------+
| 12345678A | Dominique | Farias Osorio | info@domi.com |
+-----------+-----------+---------------+---------------+
1 row in set (0,00 sec)

-- Update

UPDATE clientes
SET dni = '1111111A'
WHERE nombre = 'Dominique';

SELECT * FROM clientes;

UPDATE clientes
SET apellidos = 'Osorio Farias'
WHERE nombre = 'Dominique';

-- Delete

DELETE FROM clientes
WHERE dni = '1111111A';

