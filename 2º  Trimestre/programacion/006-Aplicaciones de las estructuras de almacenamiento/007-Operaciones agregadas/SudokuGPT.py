"""
Sudoku bonito - Generador y visor

Ejecución (GUI): python3 sudoku_bonito.py
Ejecución (sin GUI / entorno sin tkinter): python3 sudoku_bonito.py --nogui

Qué hace este archivo:
- Genera un tablero completo por backtracking.
- Crea un puzzle eliminando cifras (3 niveles de dificultad).
- Intenta arrancar una interfaz "bonita" con Tkinter cuando esté disponible.
- Si Tkinter NO está disponible (ej. en servidores o sandboxes), cae a un modo consola automático.
- Incluye pruebas sencillas que se ejecutan con `--test`.

Notas sobre el error común:
Si ves `ModuleNotFoundError: No module named 'tkinter'` significa que tu entorno de ejecución no tiene Tkinter instalado (muy común en contenedores/sandboxes). Usa `--nogui` o ejecuta en una máquina local con Tk instalado.
"""

import random
import sys
import argparse
from copy import deepcopy

# Intentar importar tkinter, si falla, seguir en modo consola
HAS_TK = True
try:
    import tkinter as tk
    from tkinter import font
    try:
        import tkinter.messagebox as messagebox
    except Exception:
        messagebox = None
except Exception:
    HAS_TK = False
    tk = None
    font = None
    messagebox = None

# ---------- Generador de Sudoku (Backtracking) ----------

def valid(board, r, c, val):
    """Comprueba si `val` puede ir en board[r][c] según reglas Sudoku."""
    for i in range(9):
        if board[r][i] == val or board[i][c] == val:
            return False
    br, bc = (r // 3) * 3, (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == val:
                return False
    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve_board(board):
    """Resuelve el tablero in-place. Devuelve True si se resuelve."""
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty
    for n in range(1, 10):
        if valid(board, r, c, n):
            board[r][c] = n
            if solve_board(board):
                return True
            board[r][c] = 0
    return False


def generate_full_board(seed_shuffle=True):
    board = [[0] * 9 for _ in range(9)]
    # rellenar diagonal de 3x3 aleatoriamente para acelerar
    for block in range(3):
        nums = list(range(1, 10))
        if seed_shuffle:
            random.shuffle(nums)
        br = block * 3
        for i in range(3):
            for j in range(3):
                board[br + i][br + j] = nums.pop()
    # solucionar el resto
    solve_board(board)
    return board


def make_puzzle(full_board, clues=36):
    """Toma un tablero completo `full_board` y elimina (81-clues) celdas al azar."""
    puzzle = [row[:] for row in full_board]
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    to_remove = 81 - clues
    for i in range(to_remove):
        r, c = cells[i]
        puzzle[r][c] = 0
    return puzzle

# ---------- Interfaz Tkinter (si está disponible) ----------

if HAS_TK:
    class SudokuApp:
        def __init__(self, master):
            self.master = master
            master.title("Sudoku Bonito")
            master.resizable(False, False)

            self.frame = tk.Frame(master, padx=12, pady=12, bg="#f4f6f8")
            self.frame.pack()

            title = tk.Label(self.frame, text="Sudoku Bonito", font=("Helvetica", 20, "bold"), bg="#f4f6f8")
            title.grid(row=0, column=0, columnspan=9, pady=(0, 8))

            self.level = tk.StringVar(value="medio")
            level_frame = tk.Frame(self.frame, bg="#f4f6f8")
            level_frame.grid(row=1, column=0, columnspan=9, pady=(0, 6))
            tk.Radiobutton(level_frame, text="Fácil", variable=self.level, value="facil", bg="#f4f6f8").pack(side="left", padx=6)
            tk.Radiobutton(level_frame, text="Medio", variable=self.level, value="medio", bg="#f4f6f8").pack(side="left", padx=6)
            tk.Radiobutton(level_frame, text="Difícil", variable=self.level, value="dificil", bg="#f4f6f8").pack(side="left", padx=6)

            # fuente para números (si falla, usar por defecto)
            try:
                self.num_font = font.Font(family="Helvetica", size=16, weight="bold")
            except Exception:
                self.num_font = None

            # canvas con bordes y celdas
            self.grid_frame = tk.Frame(self.frame, bd=2, relief="flat", bg="#e8edf2")
            self.grid_frame.grid(row=2, column=0, columnspan=9, padx=4, pady=4)

            self.cells = [[None] * 9 for _ in range(9)]
            for r in range(9):
                for c in range(9):
                    cell = tk.Label(self.grid_frame, text='', width=3, height=1, font=self.num_font,
                                    bg='white', bd=1, relief='solid')
                    cell.grid(row=r, column=c, sticky='nsew')
                    cell.config(borderwidth=1, relief='solid')
                    self.cells[r][c] = cell

            for i in range(9):
                self.grid_frame.grid_rowconfigure(i, minsize=36)
                self.grid_frame.grid_columnconfigure(i, minsize=36)

            # botones
            btn_new = tk.Button(self.frame, text="Nuevo", command=self.new_puzzle, width=10)
            btn_new.grid(row=3, column=1, columnspan=2, pady=(10, 0))

            btn_solve = tk.Button(self.frame, text="Resolver", command=self.show_solution, width=10)
            btn_solve.grid(row=3, column=4, columnspan=2, pady=(10, 0))

            btn_copy = tk.Button(self.frame, text="Copiar solución al portapapeles", command=self.copy_solution, width=22)
            btn_copy.grid(row=3, column=6, columnspan=3, pady=(10, 0))

            # inicializar
            self.full = generate_full_board()
            self.puzzle = make_puzzle(self.full, clues=self._clues_from_level())
            self.draw()

        def _clues_from_level(self):
            lvl = self.level.get()
            if lvl == 'facil':
                return 42
            if lvl == 'medio':
                return 36
            return 28

        def new_puzzle(self):
            self.full = generate_full_board()
            self.puzzle = make_puzzle(self.full, clues=self._clues_from_level())
            self.draw()

        def draw(self, show_solution=False):
            board = self.full if show_solution else self.puzzle
            for r in range(9):
                for c in range(9):
                    val = board[r][c]
                    label = self.cells[r][c]
                    if val == 0:
                        label.config(text='', fg='#333', bg='#ffffff')
                    else:
                        if show_solution:
                            label.config(text=str(val), fg='#2b2b2b', bg='#f2f6f9')
                        else:
                            label.config(text=str(val), fg='#1b66d1', bg='#ffffff')
                    if self.puzzle[r][c] == 0 and not show_solution:
                        label.config(font=self.num_font, fg='#555')
                    elif self.puzzle[r][c] != 0 and not show_solution:
                        label.config(font=self.num_font, fg='#0b3b86')
            self.master.update_idletasks()

        def show_solution(self):
            self.draw(show_solution=True)

        def copy_solution(self):
            s = ''
            for r in range(9):
                s += ' '.join(str(n) for n in self.full[r]) + '\n'
            try:
                self.master.clipboard_clear()
                self.master.clipboard_append(s)
                self.master.update()
                if messagebox:
                    messagebox.showinfo("Copiado", "Solución copiada al portapapeles")
                else:
                    print("Solución copiada al portapapeles (no se pudo mostrar diálogo).")
            except Exception:
                print(s)

# ---------- Modo consola (para entornos sin GUI o --nogui) ----------

def pretty_print(board):
    line = '+-------+-------+-------+'
    for i, row in enumerate(board):
        if i % 3 == 0:
            print(line)
        print('|', end=' ')
        for j, num in enumerate(row):
            ch = str(num) if num != 0 else '.'
            print(ch, end=' ')
            if (j + 1) % 3 == 0:
                print('|', end=' ')
        print()
    print(line)

# ---------- Tests simples ----------

def _is_complete(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return False
    return True


def validate_full_board(board):
    # Verifica que cada fila, columna y bloque contienen 1..9
    for i in range(9):
        row = sorted(board[i])
        if row != list(range(1, 10)):
            return False
        col = sorted(board[r][i] for r in range(9))
        if col != list(range(1, 10)):
            return False
    # bloques 3x3
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            nums = []
            for r in range(br, br + 3):
                for c in range(bc, bc + 3):
                    nums.append(board[r][c])
            if sorted(nums) != list(range(1, 10)):
                return False
    return True


def run_tests():
    print('Ejecutando pruebas básicas...')
    full = generate_full_board()
    assert _is_complete(full), 'Full board no está completo'
    assert validate_full_board(full), 'Full board no es válido'

    # probar el solver sobre un tablero con huecos (debe resolverse)
    puzzle = make_puzzle(full, clues=36)
    copy_for_solve = deepcopy(puzzle)
    solvable = solve_board(copy_for_solve)
    assert solvable, 'El puzzle generado no es resolvible (esto no debería ocurrir)'

    # comprobar cantidad de pistas
    clues = sum(1 for r in puzzle for v in r if v != 0)
    assert 1 <= clues <= 81, 'Número de pistas fuera de rango'

    print('Todas las pruebas pasaron correctamente.')

# ---------- Ejecutable ----------

def main(argv=None):
    parser = argparse.ArgumentParser(description='Sudoku Bonito - GUI opcional')
    parser.add_argument('--nogui', action='store_true', help='Forzar modo consola (no tkinter)')
    parser.add_argument('--test', action='store_true', help='Ejecutar pruebas internas')
    parser.add_argument('--clues', type=int, default=None, help='Cantidad de pistas si se imprime puzzle en consola')
    args = parser.parse_args(argv)

    if args.test:
        run_tests()
        return 0

    if args.nogui or not HAS_TK:
        # modo consola
        if not HAS_TK and not args.nogui:
            print('Atención: Tkinter no está disponible en este entorno. Ejecutando en modo consola.')
        full = generate_full_board()
        clues = args.clues if args.clues is not None else 36
        puzzle = make_puzzle(full, clues=clues)
        pretty_print(puzzle)
        return 0

    # Si aquí, tenemos tkinter y no se forzó nogui
    root = tk.Tk()
    try:
        app = SudokuApp(root)
        root.mainloop()
    except Exception as e:
        print('Error con la interfaz gráfica — mostrando puzzle en consola. Detalle:', e)
        full = generate_full_board()
        puzzle = make_puzzle(full, clues=36)
        pretty_print(puzzle)
    return 0


if __name__ == '__main__':
    sys.exit(main())

