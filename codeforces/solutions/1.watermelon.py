def watermelon(kilos: int):
    if kilos > 2 and kilos % 2 == 0:
        print('YES')
    else:
        print('NO')

kilos = int(input())
watermelon(kilos)