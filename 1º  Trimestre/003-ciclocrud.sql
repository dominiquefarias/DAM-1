INSERT INTO clientes VALUES(
	NULL:
	"Dominique",
	"Farias Osorio",
	"Info@jocarsa.com"
);

SELECT * FROM clientes;

UPDATE clientes
SET email = 'info@jocarsacarratala.com'
WHERE identificador
