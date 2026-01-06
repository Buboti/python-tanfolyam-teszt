text = input('adjon meg tetszoleges betuket es szamokat: ')
def remove_duplicates(text):
    seen = set()
    new_list=[]

    for item in text:
        if  item.isalpha():
            key= item.lower()
        elif item.isdigit():
            key = int(item)
        else:
            continue
        if key not in seen:
            new_list.append(item)
            seen.add(key)
    return new_list
result = remove_duplicates(text)
print('Lista duplikaciok nelkul: ', result)

# róbert:
def unique_list(list):
    items = []
    for item in list:
        if item not in items:
            items.append(item)
    return items
print(unique_list([1,1,1,2,3,5,45,6]))