USE ejemplosclaves;
CREATE TABLE personas (
	nombre VARCHAR(50),
	apellidos VARCHAR(255)
);

CREATE TABLE emails (
	direccion VARCHAR(50),
	persona VARCHAR(255)
);

--paso 1 cambiar el tipo de columna
ALTER TABLE emails
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

-- paso 2 crear la foreign key
ALTER TABLE emails
MODIFY COLUMN personas INT;

ALTER TABLE emails
ADD CONSTRAINT fk_emails_personas
FOREIGN KEY (persona) REFERENCES personas(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

CREATE DATABASE ejemplosclaves;

