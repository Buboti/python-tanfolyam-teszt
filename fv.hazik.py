def gombv(r):
    pi = 3.14159
    terfogat = (4/3)*pi*(r**3)
    return terfogat
sugar = float(input("Add meg a gomb sugarat:"))
print('A gomb terfogata:',gombv(sugar))


# róbert megoldása:
def globe_volume2(radius: float) -> float:
    """
    This function is returning globe volume
    :param radius: The radius of the globe
    :return: The globe volume
    """
    # if radius > 0:
    #   return (4 / 3) * 3,14 * (radius ** 3)
    # return -1
    if radius <= 0:
        raise ValueError(f'Radius must be a positive number. The current radius is {radius}')
    return (4 / 3) * 3, 14 * (radius ** 3)
print(globe_volume2(2))
#print(globe_volume2(-2))