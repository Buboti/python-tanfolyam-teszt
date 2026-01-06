import string
import unicodedata


def is_pangram(text):
    text=text.lower()
    letters= set(c for c in text if c.isalpha())
    return len(letters) == 26
user_input = input ('adj meg egy szoveget: ')
if is_pangram(user_input):
    print('Ez pangram')
else:
    print('Nem pangram')

#róbert:

def is_pangram(text: str) -> bool:
    alphabet = string.ascii_lowercase + 'öüóőúéáűí'
    normalized = unicodedata.normalize('NFC', text).lower()
    letters_in_text = {ch for ch in normalized if ch in alphabet}
    return letters_in_text.issuperset(alphabet)

print(is_pangram('Egy hűtlen vejét fülöncsípő, dühös mexikói úr Wesselényinél mázol Quitóban'))