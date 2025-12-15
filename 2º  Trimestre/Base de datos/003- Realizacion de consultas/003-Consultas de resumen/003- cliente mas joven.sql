-- sudo mysql -u rooot -p

USE clientes;
 
SELCET
nombre,
apellidos,
MIN (edad)
FROM clientes;
