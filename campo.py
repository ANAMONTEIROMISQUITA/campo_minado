import random

SIZE = 5        
BOMBS = 5       

def create_bombs(size, bombs):
    all_cells = [(r, c) for r in range(size) for c in range(size)]
    return set(random.sample(all_cells, bombs))
