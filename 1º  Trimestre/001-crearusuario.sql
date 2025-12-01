-- crea usuario nuevo con contraseña
CREATE USER 
'dominique1'@'localhost' 
IDENTIFIED  BY 'Domi.virt3';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'dominique1'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'dominique1'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `empresadam`.* 
TO 'dominique1'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;


-- crea usuario nuevo con contraseña
CREATE USER 
'dominique1'@'localhost' 
IDENTIFIED  BY 'Domi.virt3';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'dominique1'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'dominique1'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos portafolio1
GRANT ALL PRIVILEGES ON `portafolio1`.* 
TO 'dominique1'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
