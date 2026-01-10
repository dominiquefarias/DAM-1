#sudo mysql -u rooot -p

USE clientes;
 
SELECT
	FLOOR(AVG(edad))
FROM clientes;

SELECT	
	CEIL(AVG(edad))
FROM clientes;


