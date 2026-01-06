try:
    f = open('test.txt', 'r')
    f.write('valami')
except FileNotFoundError:
    print('nincs meg a fájl')
except IOError:
    print('Iras hiba')
except:
    print('Kritikus hiba tortent')
else:
    print('Siker eseten hajtodik vegre')
    f.close()
finally:
    print('minden esetben lefut')
