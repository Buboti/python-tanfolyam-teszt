import random

# Magyar allatok szavak (100 db, ekezet nelkul)
word_list = [
    "kutya", "macska", "lo", "tehen", "juh", "kecske", "sertes", "csirke", "pulyka", "lud",
    "kacsa", "liba", "hattyu", "roka", "medve", "farkas", "oz", "szarvas", "nyul", "mokus",
    "eger", "patkany", "horcsog", "tengerimalac", "nyest", "borz", "hiuz", "sakal", "medve", "varju",
    "galamb", "vereb", "fecske", "bagoly", "sas", "heja", "kakas", "tyuk", "pocok", "denver",
    "facan", "farkas", "medve", "roka", "meduza", "polip", "rak", "hal", "angolna", "ponty",
    "harcsa", "karasz", "csuka", "beka", "varangy", "gyik", "kigyo", "teknos", "sakal", "hiuz",
    "oszibarack", "pava", "galamb", "pocok", "nyul", "szarvas", "oz", "lo", "kutya", "macska",
    "cickany", "hod", "vidra", "foka", "delfin", "cet", "balna", "pingvin", "strucc", "kenguru",
    "koala", "zsiraf", "elefant", "tigris", "oroszlan", "leopard", "parduc", "antilop", "zebra", "antilop",
    "medve", "farkas", "roka", "nyul", "eger", "patkany", "mokus", "horcsog", "tengerimalac", "kecske"
]

# Titkos szó kiválasztása
secret_word = random.choice(word_list)

guessed_letters = []  # Ide kerülnek a helyes tippek
wrong_letters = []    # Ide kerülnek a hibás tippek
max_attempts = 6      # Maximum hibás tipp

def display_word():
    displayed = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()


print(display_word())  # kezdetben minden betű "_"

hangman_stages = [
    """
       +---+
           |
           |
           |
          ===
    """,
    """
       +---+
       O   |
           |
           |
          ===
    """,
    """
       +---+
       O   |
       |   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\  |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\  |
      /    |
          ===
    """,
    """
       +---+
       O   |
      /|\  |
      / \  |
          ===
    """
]

while True:
    print(hangman_stages[len(wrong_letters)])
    print(display_word())
    print(f"Hibas tippek: {', '.join(wrong_letters)}")
    print(f"Hatralvo probalkozasok: {max_attempts - len(wrong_letters)}")

    guess = input("Tippelj egy betut: ").lower()

    # Ellenőrzés: csak egy betűt lehessen beírni
    if len(guess) != 1 or not guess.isalpha():
        print("Csak egy betut irj be!")
        continue

    # Ha már tippelte korábban
    if guess in guessed_letters or guess in wrong_letters:
        print("Ezt a betut mar tippelted.")
        continue

    # Ha a tipp helyes
    if guess in secret_word:
        guessed_letters.append(guess)
        print("Talalat! 🎯")
    else:
        wrong_letters.append(guess)
        print("Nem talaltad el. ❌")

    # Ha minden betű megvan → nyert
    if all(letter in guessed_letters for letter in secret_word):
        print(f"Nyertel! A szo ez volt: {secret_word}")
        break

    # Ha elfogytak a próbák → veszít
    if len(wrong_letters) >= max_attempts:
        print(f"Vesztettel! A szo ez volt: {secret_word}")
        break







