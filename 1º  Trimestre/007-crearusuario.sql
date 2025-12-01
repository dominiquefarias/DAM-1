-- crea usuario nuevo con contraseña
CREATE USER 
'empresadam'@'localhost' 
IDENTIFIED  BY 'Empresadam123$';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'empresadam'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'empresadam'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `empresadam`.* 
TO 'empresadam'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;

-- crea usuario nuevo con contraseña
CREATE USER 
'dominique3'@'localhost' 
IDENTIFIED  BY 'Domy123$';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'dominique3'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'dominique3'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `portafolioexamen`.* 
TO 'dominique3'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
