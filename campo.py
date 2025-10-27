import random

SIZE = 5        
BOMBS = 5       

def create_bombs(size, bombs):
    all_cells = [(r, c) for r in range(size) for c in range(size)]
    return set(random.sample(all_cells, bombs))

def neighbors(r, c, size):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size:
                yield nr, nc

def count_adjacent_bombs(r, c, bombs):
    return sum((nr, nc) in bombs for nr, nc in neighbors(r, c, SIZE))

def print_board(revealed, bombs, size, show_bombs=False):
    print("   " + " ".join(f"{c+1}" for c in range(size)))
    for r in range(size):
        row_cells = []
        for c in range(size):
            if (r, c) in revealed:
                if (r, c) in bombs:
                    cell = "B"
                else:
                    cell = str(count_adjacent_bombs(r, c, bombs))
            else:
                if show_bombs and (r, c) in bombs:
                    cell = "B"
                else:
                    cell = "."
            row_cells.append(cell)
        print(f"{r+1:2} " + " ".join(row_cells))
    print()

def get_player_move(size):
    while True:
        move = input(f"Escolha linha e coluna (1-{size}) separados por espaço, ex: '3 2': ").strip()
        parts = move.split()
        if len(parts) != 2:
            print("Entrada inválida digite dois números separados por espaço.")
            continue
        if not (parts[0].isdigit() and parts[1].isdigit()):
            print("Use apenas números.")
            continue
        r, c = int(parts[0]) - 1, int(parts[1]) - 1
        if not (0 <= r < size and 0 <= c < size):
            print(f"Números fora do intervalo. Use valores entre 1 e {size}.")
            continue
        return r, c

def main():
    bombs = create_bombs(SIZE, BOMBS)
    revealed = set()
    safe_cells_total = SIZE * SIZE - BOMBS

    print("=== Campo Minado (5x5) Simplificado ===")
    print("Revele todas as casas sem explodir uma bomba para vencer.")
    print("Marcas: '.' = não revelado, número = bombas adjacentes, B = bomba")
    print()

    while True:
        print_board(revealed, bombs, SIZE, show_bombs=False)
        r, c = get_player_move(SIZE)

        if (r, c) in revealed:
            print("Casa já revelada — escolha outra.")
            continue

        revealed.add((r, c))

        if (r, c) in bombs:
            print_board(revealed, bombs, SIZE, show_bombs=True)
            print("BOOM! Você acertou uma bomba. Fim de jogo.")
            break

        if count_adjacent_bombs(r, c, bombs) == 0:
            to_check = [(r, c)]
            while to_check:
                cr, cc = to_check.pop()
                for nr, nc in neighbors(cr, cc, SIZE):
                    if (nr, nc) not in revealed and (nr, nc) not in bombs:
                        revealed.add((nr, nc))
                        if count_adjacent_bombs(nr, nc, bombs) == 0:
                            to_check.append((nr, nc))

        if len([cell for cell in revealed if cell not in bombs]) >= safe_cells_total:
            print_board(revealed, bombs, SIZE, show_bombs=True)
            print("Parabéns! Você venceu!")
            break

if __name__ == "__main__":
    main()
