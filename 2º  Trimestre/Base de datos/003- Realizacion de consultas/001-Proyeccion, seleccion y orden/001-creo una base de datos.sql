-- sudo mysql -u root -p

CREATE DATABASE clientes;

USE clientes;

CREATE TABLE clientes(
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	edad INT
);

INSERT INTO clientes VALUES ("Juan", "Lopez", 45);
INSERT INTO clientes VALUES ("Javier", "Martines", 46);

-- Podemos añadir mas clientes con ia
