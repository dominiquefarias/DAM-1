import os
import random
import time
import sys

# Secuencias ANSI para diferentes tonos de verde (de más brillante a más oscuro)
GREEN_COLORS = [
    '\033[38;5;82m',   # verde brillante
    '\033[38;5;40m',   # verde medio
    '\033[38;5;28m',   # verde oscuro
    '\033[38;5;22m',   # verde muy oscuro
]

RESET = '\033[0m'

def get_terminal_size():
    try:
        size = os.get_terminal_size()
        return size.lines, size.columns
    except OSError:
        # Por si falla, tamaño por defecto
        return 24, 80

def matrix_rain():
    rows, cols = get_terminal_size()

    # Cada columna tendrá su "posición" de gota y longitud de la cola
    drops = [random.randint(0, rows) for _ in range(cols)]
    tails = [random.randint(5, rows // 2) for _ in range(cols)]

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*()-_=+[]{}|;:',.<>/?"

    try:
        while True:
            # Limpiar pantalla al inicio de cada frame
            print('\033[H', end='')  # mover cursor a la esquina superior izquierda
            
            for row in range(rows):
                line = ''
                for col in range(cols):
                    drop_pos = drops[col]
                    tail_len = tails[col]
                    char = ' '

                    # Si la fila está dentro del rango de la gota para esa columna
                    if drop_pos - tail_len <= row <= drop_pos:
                        distance = drop_pos - row
                        if distance == 0:
                            # Cabeza de la gota (más brillante)
                            color = GREEN_COLORS[0]
                        elif distance < len(GREEN_COLORS):
                            # Cola con degradado
                            color = GREEN_COLORS[distance]
                        else:
                            # Cola más oscura
                            color = GREEN_COLORS[-1]
                        char = color + random.choice(chars) + RESET
                    else:
                        char = ' '

                    line += char
                print(line)
            
            # Actualizar posición de las gotas, que caen
            for i in range(cols):
                if drops[i] < rows + tails[i]:
                    drops[i] += 1
                else:
                    # Reiniciar gota con nueva cola y posición inicial aleatoria (arriba)
                    drops[i] = 0
                    tails[i] = random.randint(5, rows // 2)

            time.sleep(0.05)
    except KeyboardInterrupt:
        print(RESET)
        sys.exit()

if __name__ == "__main__":
    # Limpiar pantalla antes de empezar
    os.system('cls' if os.name == 'nt' else 'clear')
    matrix_rain()

