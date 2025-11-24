-- Crear base de datos
CREATE DATABASE IF NOT EXISTS tienda1;
USE tienda1;

-- Tabla clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(255)
);

-- Tabla productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Datos de prueba: clientes
INSERT INTO clientes (nombre, email, telefono)
VALUES
    ('Ana López', 'ana@example.com', '600123456'),
    ('Carlos Ruiz', 'carlos@example.com', '611987654'),
    ('María Gómez', 'maria@example.com', '622111222');

-- Datos de prueba: productos
INSERT INTO productos (nombre, descripcion, precio, stock)
VALUES
    ('Portátil 15"', 'Portátil de 15 pulgadas con 16GB RAM', 899.99, 10),
    ('Ratón inalámbrico', 'Ratón óptico inalámbrico', 19.90, 50),
    ('Teclado mecánico', 'Teclado con switches azules', 59.95, 30);
    
-- Creamos usuario

-- crea usuario nuevo con contraseña
CREATE USER 
'tiendaclase1'@'localhost' 
IDENTIFIED  BY 'Tiendaclase123$';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'tiendaclase1'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'tiendaclase1'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos portafolio1
GRANT ALL PRIVILEGES ON `tienda1`.* 
TO 'tiendaclase1'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
