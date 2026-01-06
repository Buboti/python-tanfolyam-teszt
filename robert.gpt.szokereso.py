# 1. szokeszlet letrehozasa
# 2. szoracs letrehozasa
# 3. szavak elhelyezese a szoracsban
# 4. ures cellak feltoltese veletlenszeru betukkel
# 5. szamozott racs megjelenitese
# 6. felhasznaloi input(koordinatak)
# 7. ha megtalalta akkor "szavak kiemelese", megtalalt betuk szinezese
from colorama import init, Fore, Style
import random

init(autoreset=True)

def get_word_list() -> list[str]:
    """
    The game word list
    :return: A list of words
    """
    return ['PYTHON','PROGRAM','LOGIKA','WEB','LAPTOP','SZINTAXIS','ALMAFA']

def create_empty_grid(size=10):
    """
    Create empty grid

    Args:
        size (int): The size of the grid
    Returns:
         The empty grid
    """
    return [[' ' for _ in range(size)] for _ in range(size)]

def place_word_in_grid(grid, word):
    """
    Place the given word into the given grid

    Args:
        grid(list): The word grid
        word(str): The given word
    """
    size = len(grid)
    directions = ['horizontal', 'vertical', 'diagonal']
    placed = False
    while not placed:
        good_position = True
        direction = random.choice(directions)
        start_row, start_col = random.randint(0, size-1), random.randint(0, size-1)

        # vízszintes
        if direction == 'horizontal' and start_col + len(word) <= size:
            for i in range(len(word)):
                if grid[start_row][start_col+i] != ' ':
                    good_position = False
                    break
            if not good_position:
                continue
            for i in range(len(word)):
                grid[start_row][start_col + i] = word[i]
            placed = True

        # függőleges
        elif direction == 'vertical' and start_row + len(word) <= size:
            for i in range(len(word)):
                if grid[start_row + i][start_col] != ' ':
                    good_position = False
                    break
            if not good_position:
                continue
            for i in range(len(word)):
                grid[start_row + i][start_col] = word[i]
            placed = True

        # átlós
        elif direction == 'diagonal' and start_col + len(word) <= size and start_row + len(word) <= size:
            for i in range(len(word)):
                if grid[start_row + i][start_col + i] != ' ':
                    good_position = False
                    break
            if not good_position:
                continue
            for i in range(len(word)):
                grid[start_row + i][start_col + i] = word[i]
            placed = True

def fill_empty_cells(grid):
    """
    Fill empty cells with random values

    Args:
        grid(list): The grid
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ' ':
                grid[row][col] = chr(random.randint(65,90))

def display_grid(grid):
    """
    Display the grid with coordinates

    Args:
        grid(list): The grid
    """
    print('\nJatekracs (sor es oszlopszamokkal)')
    header = '   ' + ' '.join(f'{i}' for i in range(len(grid)))
    print(header)
    print('   ' + '--' * len(grid))
    for idx, row in enumerate(grid):
        print(f'{idx} | ' + ' '.join(f'{Fore.GREEN}{cell}{Style.RESET_ALL}'
                                     if cell.islower() else cell for cell in row))

def get_number_input(user_str, size):
    """
    Handle user input and validate

    Args:
        user_str(str): The user input string
        size(int): The size of the grid

    Returns:
        The choosed coordinate
    """
    while True:
        input_str = input(user_str)
        if input_str.isdigit() and 0 <= int(input_str) < size:
            return int(input_str)

def get_word_selection(grid):
    """
    Get word selection

    Args:
        grid(list): The grid
    Returns:
        Coordinates
    """
    print('\nSegitseg a koordinatak megadasahoz: ')
    print(' - Sor es oszlopszamot adjon meg (pl: kezdo sor: 2 oszlop: 3)')
    print(' - Vegpontonkent adja meg a koordinatakat (pl.: veg sor: 2 oszlop: 7)')
    print('Pelda a -SZINTAXIS- szohoz: kezdo (1,1) veg (1,8) ')
    size = len(grid)
    start_row = get_number_input(f'Adja meg a szo kezdosoranak szamat (0-{size-1}): ', size)
    start_col = get_number_input(f'Adja meg a szo kezdooszlopanak szamat (0-{size-1}): ', size)
    end_row = get_number_input(f'Adja meg a szo vegsoranak szamat (0-{size-1}): ', size)
    end_col = get_number_input(f'Adja meg a szo vegoszlopanak szamat (0-{size-1}): ', size)
    return start_row, start_col, end_row, end_col

def check_and_mark_word_in_grid(grid, word, start_row, start_col, end_row, end_col):
    """
    Check and mark a given word in grid

    Args:
        grid(list): The grid
        word(str): The given word
        start_row(int): The starting row coordinate
        start_col(int): The starting column coordinate
        end_row(int): The ending row coordinate
        end_col(int): The ending column coordinate
    Returns:
        (boolean): Found
    """
    word_length = len(word)

    # vizszintes
    if start_row == end_row:
        if abs(start_col - end_col) + 1 == word_length:
            for i in range(word_length):
                if grid[start_row][min(start_col,end_col) + i] != word[i]:
                    return False
            for i in range(word_length):
                grid[start_row][min(start_col,end_col) + i] = grid[start_row][min(start_col,end_col) + i].lower()
            return True

    # fuggoleges
    elif start_col == end_col:
        if abs(start_row - end_row) + 1 == word_length:
            for i in range(word_length):
                if grid[min(start_row,end_row) + i][start_col] != word[i]:
                    return False
            for i in range(word_length):
                grid[min(start_row,end_row) + i][start_col] = grid[min(start_row,end_row) + i][start_col].lower()
            return True

    # atlos
    elif abs(start_row - end_row) + 1 == word_length and abs(start_col - end_col) + 1 == word_length:
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        for i in range(word_length):
            r = start_row + i*row_step
            c = start_col + i*col_step
            if grid[r][c] != word[i]:
                return False
        for i in range(word_length):
            r = start_row + i*row_step
            c = start_col + i*col_step
            grid[r][c] = grid[r][c].lower()
        return True

    return False

def main():
    grid = create_empty_grid()
    word_list = get_word_list()

    for word in word_list:
        place_word_in_grid(grid, word)

    fill_empty_cells(grid)
    display_grid(grid)

    print('\nRejtett szavak:', ', '.join(word_list))
    found_words = []

    while len(found_words) < len(word_list):
        print('\nTalalt szavak:', ', '.join(found_words))
        start_row, start_col, end_row, end_col = get_word_selection(grid)

        found = False
        for word in word_list:
            if word not in found_words and check_and_mark_word_in_grid(grid, word, start_row, start_col, end_row, end_col):
                print(f'Megtalaltad a szot: {word}')
                found_words.append(word)
                found = True
                break

        if not found:
            print('Nincs a megadott szavak egyike sem a megadott helyen')

        display_grid(grid)

    print('Gratulalunk, megtalaltad az osszes szot!')

if __name__ == '__main__':
    main()
