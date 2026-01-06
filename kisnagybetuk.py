import unicodedata

text = input('Adj meg egy szoveget: ')
def letter_number(text):
    small = 0
    large = 0
    for c in text:
        if c.isupper():
            large += 1
        elif c.islower():
            small += 1
    print(f"Nagybetuk szama: {large}")
    print(f"Kisbetuk szama: {small}")
letter_number(text)

# róbert megoldasa:
def count_small_and_upper_case(s:str) -> None:
    d= {'upper':0,'lower' :0}

    for c in s:
        if c.isupper():
            d['upper'] += 1
        elif c.islower():
            d['lower'] += 1

    print('az eredeti szoveg: ' +s)
    print(' A nagybetuk szama:', d['upper'])
    print('a kisbetuk szama:', d['lower'])

count_small_and_upper_case('AlMaFa')
count_small_and_upper_case('ÓlAjtó')
count_small_and_upper_case('ÍaÁéŐüÚű')

def count_small_and_lower_case2(s:str) -> dict:
    s_norm = unicodedata.normalize('NFC', s)
    upper = sum(1 for c in s_norm if c.isupper())
    lower = sum(1 for c in s_norm if c.islower())
    return {
        'original': s,
        'normalized': s_norm,
        'upper_case': upper,
        'lower_case': lower,
    }
print(count_small_and_lower_case2('AáÁlÓmHAjó'))