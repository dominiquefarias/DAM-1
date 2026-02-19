# Ejercicio Final: Agrupamientos y Visualización

Este documento contiene la solución para los ejercicios de agrupación y visualización de productos.

## 1. Configuración de la Base de Datos
Para ejecutar estos ejercicios, primero necesitamos una tabla de `productos` con datos. He creado el archivo `setup_database.sql` con el siguiente contenido:

```sql
-- setup_database.sql
DROP TABLE IF EXISTS productos;
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    color VARCHAR(30),
    stock INT
);

INSERT INTO productos (nombre, categoria, color, stock) VALUES
('Camiseta Básica', 'Ropa', 'Blanco', 100),
('Pantalón Vaquero', 'Ropa', 'Azul', 50),
('Zapatillas Running', 'Calzado', 'Negro', 30),
('Camisa Formal', 'Ropa', 'Blanco', 40),
('Calcetines Deportivos', 'Ropa', 'Blanco', 200),
('Chaqueta Cuero', 'Ropa', 'Negro', 15),
('Zapatos Vestir', 'Calzado', 'Marrón', 25),
('Gorra', 'Accesorios', 'Rojo', 60),
('Bufanda', 'Accesorios', 'Azul', 45),
('Cinturón', 'Accesorios', 'Negro', 80),
('Vestido Verano', 'Ropa', 'Rojo', 35),
('Sandalias', 'Calzado', 'Marrón', 40),
('Botas Invierno', 'Calzado', 'Negro', 20),
('Bolso Mano', 'Accesorios', 'Rojo', 25),
('Reloj Deportivo', 'Accesorios', 'Negro', 10);
```

**Instrucción:** Ejecuta este script el tu cliente de MySQL (Workbench, terminal, etc.) para crear la tabla y los datos.

## 2. Categorías de Productos (Gráfico de Pastel)
Script: `01_categorias.py`
Consulta SQL utilizada:
```sql
SELECT categoria, COUNT(categoria) as numero 
FROM productos 
GROUP BY categoria 
ORDER BY numero DESC;
```
Este script conecta a la base de datos, obtiene el conteo por categoría y genera un gráfico de pastel.

## 3. Colores de Productos (Gráfico de Pastel con Colores Reales)
Script: `02_colores.py`
Consulta SQL utilizada:
```sql
SELECT color, COUNT(color) as numero 
FROM productos 
GROUP BY color 
ORDER BY numero DESC;
```
Este script mapea los nombres de colores en la base de datos (ej. 'Rojo') a colores visuales en el gráfico (ej. 'red').

## 4. Stock de Productos (Gráfico de Barras)
Script: `03_stock.py`
Consulta SQL utilizada:
```sql
SELECT stock, COUNT(*) as numero 
FROM productos 
GROUP BY stock 
ORDER BY numero DESC;
```
Este script muestra cuántos productos tienen el mismo nivel de stock.

---
**Nota:** Asegúrate de actualizar las credenciales (`user`, `password`, `database`) en cada archivo `.py` antes de ejecutarlos.
