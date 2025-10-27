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