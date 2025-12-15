import sqlite3
from colorama import init, Fore, Style


# Inicializa colorama (para colores en Windows y otros sistemas)
init(autoreset=True)

# Conexión a la base de datos
conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

# Crear tabla 'clientes' si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        identificador INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        email TEXT NOT NULL
    );
''')
conexion.commit()

# Título del programa
print(Fore.CYAN + Style.BRIGHT + "\n📅 AGENDA DE CLIENTES - Dominique Farias 📅\n")

# Menú principal
while True:
    print(Fore.YELLOW + "📌 Selecciona una opción:")
    print(Fore.GREEN + "  1️⃣  - Crear cliente")
    print(Fore.GREEN + "  2️⃣  - Listar clientes")
    print(Fore.GREEN + "  3️⃣  - Actualizar cliente")
    print(Fore.GREEN + "  4️⃣  - Eliminar cliente")
    print(Fore.GREEN + "  5️⃣  - Salir\n")

    try:
        opcion = int(input(Fore.MAGENTA + "👉 Opción: "))
    except ValueError:
        print(Fore.RED + "❌ Por favor, introduce un número válido.\n")
        continue

    try:
        # OPCIÓN 1: CREAR CLIENTE
        if opcion == 1:
            print(Fore.CYAN + "\n📝 Crear nuevo cliente")
            nombre = input("   ➤ Nombre: ")
            apellidos = input("   ➤ Apellidos: ")
            email = input("   ➤ Email: ")
            cursor.execute("""
                INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?);
            """, (nombre, apellidos, email))
            conexion.commit()
            print(Fore.GREEN + "\n✅ Cliente registrado con éxito.\n")

        # OPCIÓN 2: LISTAR CLIENTES
        elif opcion == 2:
            print(Fore.CYAN + "\n📋 Lista de clientes:")
            cursor.execute('SELECT * FROM clientes;')
            filas = cursor.fetchall()
            if filas:
                headers = ["🆔 ID", "👤 Nombre", "👥 Apellidos", "📧 Email"]
                print("\n" + tabulate(filas, headers=headers, tablefmt="fancy_grid") + "\n")
            else:
                print(Fore.YELLOW + "⚠️ No hay clientes registrados.\n")

        # OPCIÓN 3: ACTUALIZAR CLIENTE
        elif opcion == 3:
            print(Fore.CYAN + "\n✏️ Actualizar cliente")
            identificador = input("   ➤ ID del cliente: ")
            nombre = input("   ➤ Nuevo nombre: ")
            apellidos = input("   ➤ Nuevos apellidos: ")
            email = input("   ➤ Nuevo email: ")
            cursor.execute("""
                UPDATE clientes SET nombre = ?, apellidos = ?, email = ?
                WHERE identificador = ?;
            """, (nombre, apellidos, email, identificador))
            conexion.commit()

            if cursor.rowcount == 0:
                print(Fore.RED + "\n⚠️ No se encontró ningún cliente con ese ID.\n")
            else:
                print(Fore.GREEN + "\n✅ Cliente actualizado correctamente.\n")

        # OPCIÓN 4: ELIMINAR CLIENTE
        elif opcion == 4:
            print(Fore.CYAN + "\n🗑️ Eliminar cliente")
            identificador = input("   ➤ ID del cliente: ")
            cursor.execute("""
                DELETE FROM clientes WHERE identificador = ?;
            """, (identificador,))
            conexion.commit()

            if cursor.rowcount == 0:
                print(Fore.RED + "\n⚠️ No se encontró ningún cliente con ese ID.\n")
            else:
                print(Fore.GREEN + "\n✅ Cliente eliminado correctamente.\n")

        # OPCIÓN 5: SALIR
        elif opcion == 5:
            print(Fore.MAGENTA + "\n👋 ¡Gracias por usar la agenda de clientes! Hasta luego.\n")
            break

        # OPCIÓN NO VÁLIDA
        else:
            print(Fore.RED + "❌ Opción no válida. Intenta de nuevo.\n")

    except sqlite3.Error as e:
        print(Fore.RED + f"❌ Error en la base de datos: {e}\n")

# Cierre de conexión
conexion.close()

