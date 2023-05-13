import random

# Beállítjuk a tábla méretét és a számokat, amelyekkel gyakorolni szeretnénk
table_size = 12
numbers = [2, 3, 4, 5, 6, 7, 8, 9]

# Véletlenszerűen kiválasztunk egy számot és egy sor- és oszlopszámot
number = random.choice(numbers)
col = random.randint(1, table_size)

# Kiírjuk a feladatot
print(f'{number} x {col} = ?')

# Beolvasunk a felhasználótól a választ
while True:
    try:
        answer = int(input('Válasz: '))
        if answer == number * row * col:
            print('Helyes!')
            break
        else:
            print('Helytelen. Próbálja újra!')
    except ValueError:
        print('Csak számot írjon be!')
