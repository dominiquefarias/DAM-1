import sqlite3

# Nos conectamos a la base de datos
conexion = sqlite3.connect("empresa.db")

# Creamos un cursor
cursor = conexion.cursor()

# Creamos la tabla con la sintaxis correcta
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellidos TEXT,
        email TEXT
    );
''')

# Insertamos un registro (es mejor especificar columnas)
cursor.execute('''
    INSERT INTO clientes (nombre, apellidos, email) VALUES (
        'Jorge', 'Garcia Lopez', 'jorge@Domasa.com'
    );
''')

conexion.commit()
conexion.close()


