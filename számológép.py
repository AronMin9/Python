# Beolvasunk két számot és az operátort
number1 = int(input('Adja meg az első számot: '))
number2 = int(input('Adja meg a második számot: '))
operator = input('Adja meg az operátort (+, -, x, :): ')

# Végrehajtjuk az operációt és elmentjük az eredményt
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == 'x':
    result = number1 * number2
elif operator == ':':
    result = number1 / number2

# Kiírjuk az eredményt
print(number1, operator, number2, "=", result)
