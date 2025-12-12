INSERT INTO clientes VALUES(
	NULL,
	"Dominique",
	"Farias Osorio",
	"Info@Domasa.com"
);

SELECT * FROM clientes;

UPDATE clientes
SET email = 'info@Domasacarratala.com'
WHERE identificador