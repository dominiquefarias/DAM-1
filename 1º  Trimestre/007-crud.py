import sqlite3

conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

print("Programa agenda SQLite Dominique Farias")
while True:
    print("Escoge una opción:\n1.-Crear cliente\n2.-Listar clientes")
    opcion = int(input("Seleccina una opcion: "))
    if opcion == 1:
        nombre = input("Introduce el nombre del cliente:")
        apellidos = input("introduce los apellidos del cliente:")
        email = input("Introduce el email del cliente: ")
        cursor.execute("""
            INSERT INTO clientes VALUES(
                NULL,'"""+nombre+"""','"""+apellidos+"""','"""+email+"""'
            );""")
        conexion.commit()
        
    elif opcion == 2:
        cursor.execute('''
            SELECT * FROM clientes;
        ''')
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)

