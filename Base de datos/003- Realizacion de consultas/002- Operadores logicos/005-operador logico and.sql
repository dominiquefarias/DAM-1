-- sudo mysql -u root -u

SELECT
nombre,
apellidos,
edad < 30 AS "¿Es menor de 30 años?",
edad >=30 && edad < 40 AS "Entre 30 y 40 años"
edad > 40 AS "Mayor de 40"
FROM clientes;

