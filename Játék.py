import random

# Generálunk egy véletlen számot 1 és 100 között
secret_number = random.randint(1, 100)

# Beolvasunk egy tippet a felhasználótól
while True:
    try:
        guess = int(input('Tippeljen egy számot 1 és 100 között: '))
        if guess < 1 or guess > 100:
            print('A számnak 1 és 100 között kell lennie!')
        elif guess < secret_number:
            print('A titkos szám nagyobb')
        elif guess > secret_number:
            print('A titkos szám kisebb')
        else:
            print('Talált! A titkos szám:', secret_number)
            break
    except ValueError:
        print('Csak számot írjon be!')
