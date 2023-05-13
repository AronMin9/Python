import random
num1 = int(input("Mondj egy számot"))
num2 = int(input("Mondj még egy számot"))
num3 = random.randint(num1, num2)
num4 = int(input("tippeljen egy számot a előző megadott számok között"))
while num3 != num4 :
    print("nem nyertél")
    num4 = int(input("tippeljen egy számot a előző megadott számok között"))
print("nyertél")
