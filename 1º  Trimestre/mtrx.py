import curses
import random
import time

# Inicializa la pantalla de curses
stdscr = curses.initscr()
curses.curs_set(0)  # Oculta el cursor
sh, sw = stdscr.getmaxyx()  # Tamaño de la ventana (alto, ancho)
stdscr.nodelay(1)  # No bloqueará la ejecución mientras esperamos entrada del teclado
stdscr.timeout(100)  # Tiempo de espera para actualizar la pantalla

# Crea las columnas para la "lluvia"
columns = int(sw / 2)  # Determina cuántas columnas caben en la pantalla
matrix_chars = ['0', '1', '@', '#', '%', '&', '$']

# Variables para las posiciones de las gotas
positions = [random.randint(0, sh) for _ in range(columns)]

try:
    while True:
        for i in range(columns):
            # Dibuja el carácter en la posición aleatoria
            char = random.choice(matrix_chars)
            stdscr.addstr(positions[i], i * 2, char, curses.color_pair(1))
            
            # Movimiento de las gotas
            positions[i] += 1
            if positions[i] >= sh:  # Cuando llega al final, reinicia la posición
                positions[i] = 0
        
        stdscr.refresh()
        time.sleep(0.05)  # Velocidad de la lluvia
except KeyboardInterrupt:
    curses.endwin()  # Salir de curses al presionar Ctrl+C

