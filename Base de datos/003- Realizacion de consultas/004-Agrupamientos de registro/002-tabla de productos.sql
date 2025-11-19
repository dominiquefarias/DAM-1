CREATE TABLE productos(
	nombre VARCHAR(255),
	precio DECIMAL(10,2)
	categoria VARCHAR(255),
	peso DECIMAL(10,2)
	stock INT,
	color VARCHAR(100)
);

INSERT INTO productos (nombre, precio, categoria, peso, stock, color) VALUES
('Laptop Pro 15"', 1299.99, 'Tecnología', 2.50, 15, 'Gris'),
('Auriculares Bluetooth X2', 89.99, 'Tecnología', 0.20, 40, 'Negro'),
('Ratón Gamer RGB', 49.90, 'Tecnología', 0.15, 60, 'Negro'),
('Teclado Mecánico MK500', 119.50, 'Tecnología', 0.90, 25, 'Blanco'),
('Monitor UltraWide 34"', 499.99, 'Tecnología', 5.80, 10, 'Negro'),

('Camiseta Deportiva', 19.99, 'Ropa', 0.25, 100, 'Azul'),
('Pantalones Chándal Premium', 35.50, 'Ropa', 0.60, 50, 'Gris'),
('Zapatillas Running AirFlex', 79.95, 'Ropa', 0.80, 35, 'Negro'),
('Chaqueta Impermeable', 59.99, 'Ropa', 1.10, 20, 'Rojo'),
('Calcetines Antideslizantes', 5.99, 'Ropa', 0.05, 200, 'Blanco'),

('Mesa de Madera Roble', 149.90, 'Hogar', 12.00, 8, 'Marrón'),
('Silla Ergonómica Pro', 129.50, 'Hogar', 6.50, 12, 'Negro'),
('Lámpara LED Minimalista', 29.99, 'Hogar', 0.90, 45, 'Blanco'),
('Cojín Decorativo 45x45', 12.50, 'Hogar', 0.40, 70, 'Verde'),
('Alfombra Suave 160x230', 89.99, 'Hogar', 4.50, 15, 'Beige'),

('Botella Deportiva 1L', 14.99, 'Deportes', 0.30, 90, 'Azul'),
('Balón de Fútbol Pro', 24.99, 'Deportes', 0.45, 60, 'Blanco'),
('Guantes de Entrenamiento', 17.50, 'Deportes', 0.20, 40, 'Negro'),
('Cuerda de Saltar Fitness', 9.99, 'Deportes', 0.10, 120, 'Rojo'),
('Mochila Outdoor 50L', 59.99, 'Deportes', 1.20, 25, 'Verde'),

('Jarrón Cerámico', 22.90, 'Decoración', 1.10, 30, 'Blanco'),
('Marco de Fotos 20x30', 8.99, 'Decoración', 0.25, 80, 'Negro'),
('Espejo Redondo 60cm', 49.90, 'Decoración', 3.00, 10, 'Dorado'),
('Portavelas Vintage', 6.50, 'Decoración', 0.15, 55, 'Plateado'),
('Figura Decorativa Elefante', 19.50, 'Decoración', 0.75, 20, 'Gris'),

('Juego de Sábanas 150cm', 39.99, 'Dormitorio', 2.00, 25, 'Blanco'),
('Edredón Nórdico', 79.99, 'Dormitorio', 3.50, 15, 'Gris'),
('Cortinas Blackout', 29.99, 'Dormitorio', 1.80, 35, 'Negro'),
('Almohada Viscoelástica', 24.90, 'Dormitorio', 0.90, 40, 'Blanco'),
('Manta Polar Suave', 14.99, 'Dormitorio', 0.70, 60, 'Azul'),

('Taladro Inalámbrico', 89.90, 'Herramientas', 1.80, 20, 'Amarillo'),
('Caja de Herramientas 75pcs', 59.99, 'Herramientas', 4.50, 12, 'Negro'),
('Martillo Profesional', 12.99, 'Herramientas', 0.80, 50, 'Plateado'),
('Destornillador Eléctrico', 29.99, 'Herramientas', 1.20, 30, 'Rojo'),
('Nivel Láser ProLine', 45.99, 'Herramientas', 0.70, 18, 'Verde'),

('Polera Básica Unisex', 12.90, 'Ropa', 0.20, 180, 'Negro'),
('Sudadera Oversize', 32.50, 'Ropa', 0.55, 75, 'Beige'),
('Gorro Invierno Lana', 8.99, 'Ropa', 0.10, 95, 'Gris'),
('Bufanda Larga', 11.50, 'Ropa', 0.25, 65, 'Rojo'),
('Botas Montaña GripMax', 99.99, 'Ropa', 1.50, 20, 'Marrón'),

('Cámara Fotográfica X100', 699.00, 'Tecnología', 1.20, 10, 'Negro'),
('Smartwatch Serie 5', 199.99, 'Tecnología', 0.30, 35, 'Negro'),
('Tablet 10" Slim', 159.99, 'Tecnología', 0.50, 25, 'Gris'),
('Powerbank 20000mAh', 24.90, 'Tecnología', 0.40, 60, 'Blanco'),
('Altavoz Portátil Bass+ ', 34.99, 'Tecnología', 0.70, 30, 'Rojo');



