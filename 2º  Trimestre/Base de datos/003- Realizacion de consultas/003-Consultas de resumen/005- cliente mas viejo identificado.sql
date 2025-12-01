-- sudo mysql -u rooot -p

USE clientes;
 
SELECT
	nombre,
	apellidos,
	MIN (edad)
FROM clientes
ORDER BY edad DESC
LIMIT 1;

