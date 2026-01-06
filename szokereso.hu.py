import random
import string

DIRECTIONS = [
    (0, 1),   # jobbra
    (1, 0),   # lefelé
    (1, 1),   # átlósan jobbra-le
    (-1, 1),  # átlósan jobbra-fel
    (0, -1),  # balra
    (-1, 0),  # felfelé
    (-1, -1), # átlósan balra-fel
    (1, -1)   # átlósan balra-le
]

def print_grid(grid):
    """"
    Nicely print the grid : each row on its own line, letters separated by spaces.
    """
    for row in grid:
        print(' '.join(row))

def create_empty_grid(size=10):
    """Creates an empty grid filled with dots."""
    return [['.' for _ in range(size)] for _ in range(size)]

def place_word (grid, word):
    size = len(grid)
    word = word.upper()
    placed = False

    while not placed:
        row = random.randint( 0, size-1 )
        col = random.randint( 0, size-1 )
        dr, dc = random.choice(DIRECTIONS)

        #ellenorizzuk hogy a szo befer e
        can_place = True
        for i in range(len(word)):
            r = row + dr*i
            c = col + dc*i
            if not ( 0 <= r < size and 0 <= c < size ):
                can_place = False
                break
        #ellenorizzuk az utkozest
            if grid[r][c] != '.' and grid[r][c] != word[i]:
                can_place = False
                break
        if can_place:
            for i in range(len(word)):
                r = row + dr*i
                c = col + dc*i
                grid[r][c] = word[i]
            placed = True

def fill_empty(grid):
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if grid[row][col] == '.':
                grid[row][col] = random.choice(string.ascii_uppercase)

def search_word(grid, word):
    """
    Searches for word in the grid in all 8 directions.
    Returns (True, start_position, direction) if found, otherwise (False, None, None).
    """
    word = word.upper()
    size = len(grid)

    # minden racsban
    for row in range(size):
        for col in range(size):
            for dr, dc in DIRECTIONS:
                found = True
                for i in range(len(word)):
                    r = row + dr * i
                    c = col + dc * i
                    if not (0 <= r < size and 0 <= c < size ):
                        found = False
                        break
                    if grid[r][c] != word[i]:
                        found = False
                        break
                if found:
                    return True, (row, col), (dr, dc)
    # ha nem talatuk
    return False, None, None

# manual test when you run the file

if __name__ == "__main__":
    words = ["BOTOND", "LACKO", "BENCE", "BRUNO"]  # szavak a játékhoz
    grid = create_empty_grid(10)

    # Szavak elhelyezése
    for word in words:
        place_word(grid, word)

    # Maradék cellák feltöltése
    fill_empty(grid)

    # Rács kiírása
    print_grid(grid)

    # Szó keresése
    word_to_search = input("\nAdj meg egy keresett szót: ")
    found, start, direction = search_word(grid, word_to_search)

    if found:
        print(f"\nA(z) '{word_to_search}' szó megtalálható a rácsban!")
        print(f"Kiindulási pont: {start}, irány: {direction}")
    else:
        print(f"\nA(z) '{word_to_search}' szó NINCS a rácsban.")
