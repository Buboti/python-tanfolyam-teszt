var = input('Irjon be egy szot')
if var.lower() == var[::-1].lower():
    print('Ez a szo palindrom)')
else:
    print('A szo nem palindrom')
