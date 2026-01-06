import re
import unicodedata

var = 'Elemezzuk ki ezt a mondatot Pythonban'

m = re.match(r'(.*) ezt (.*)',var)

if m:
    print(m.group())
    print(m.group(1))
    print(m.group(2))

s = re.search(r'(pythonban)', var, re.I)

if s:
    print(s.group())
else:
    print('Nincs talalat')

email = 'info@t_rossz_est.com'
m = re.search(r'_rossz_', email)

if m:
    print('Megvan')
    print(m.start())
    print(m.end())
    print('Email cim: ', email[:m.start()] + email[m.end():])
else:
    print('Nincs meg')

telefon = 'Kerem hivja ezt a szamot # +36-1/123-4567'
t_number = re.sub(r'\D', '',telefon)
print(t_number)

text = 'árvíztűrő tükörfúrógép'

# text = re.sub(r'[Áá]''a', text) ez amúgy jó csak nem akarjuk egyesével végigírni

nfd = unicodedata.normalize('NFD', text)
clean = re.sub(r'[\u0300-\u036F]','', nfd)
print(clean)